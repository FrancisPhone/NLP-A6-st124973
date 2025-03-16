from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM
from transformers import BitsAndBytesConfig
from langchain import HuggingFacePipeline
import torch
from langchain.vectorstores import FAISS
from langchain import PromptTemplate
import os
import InstructorEmbedding
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.chains import LLMChain
from langchain.chains.conversational_retrieval.prompts import CONDENSE_QUESTION_PROMPT
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import ConversationalRetrievalChain


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

model_id = 'lmsys/fastchat-t5-3b-v1.0'
vector_path = 'vector-store'
db_file_name = 'nlp_ait'

prompt_template = """
Your name is Francis. You are a friendly chatbot designed to answer questions about Phone Myint Naing because you have all information about him.
Provide gentle and informative answers based on the context:

Context: {context}

Question: {question}

Answer:
""".strip()

PROMPT = PromptTemplate.from_template(
    template=prompt_template
)

tokenizer = AutoTokenizer.from_pretrained(
    model_id)


if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

bitsandbyte_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    model_id,
    quantization_config=bitsandbyte_config,
    device_map='auto',
    load_in_8bit=True
)

pipe = pipeline(
    task="text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=256,
    model_kwargs={
        "temperature": 0,
        "repetition_penalty": 1.5
    }
)

llm = HuggingFacePipeline(pipeline=pipe)


model_name = 'hkunlp/instructor-base'

embedding_model=HuggingFaceInstructEmbeddings(
    model_name=model_name,
    model_kwargs={"device": device}
)


vectordb = FAISS.load_local(
    folder_path=os.path.join(vector_path, db_file_name),
    embeddings=embedding_model,
    index_name='nlp'
)


retriever = vectordb.as_retriever()

question_generator = LLMChain(
    llm=llm,
    prompt=CONDENSE_QUESTION_PROMPT,
    verbose=False
)

doc_chain = load_qa_chain(
    llm=llm,
    chain_type='stuff',
    prompt=PROMPT,
    verbose=False
)

memory = ConversationBufferWindowMemory(
    k=3,
    memory_key="chat_history",
    return_messages=True,
    output_key='answer'
)

chain = ConversationalRetrievalChain(
    retriever=retriever,
    question_generator=question_generator,
    combine_docs_chain=doc_chain,
    memory=memory,
    verbose=False
)
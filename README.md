# NLP-A6-st124973

# Chatbot with RAG (Retrieval-Augmented Generation)

This project implements a Retrieval-Augmented Generation (RAG) chatbot using the LangChain framework. The chatbot is designed to answer questions about the user (in this case, Phone Myint Naing) by retrieving information from relevant documents and generating responses using a language model.

## Features

- **Retrieval-Augmented Generation (RAG):** Combines document retrieval with language generation to provide accurate and context-aware responses.
- **Chat Interface:** A user-friendly web interface built with Django and Bootstrap.
- **Chat History:** Saves chat history in a database and displays it in the chat interface.
- **Loading Spinner:** Displays a loading spinner while the chatbot processes the user's input.
- **Clear Chat:** Allows users to clear the chat history.

## Requirements

- Python 3.8+
- Django 4.0+
- LangChain
- Hugging Face Transformers
- Bootstrap 5.3.0

## Installation

### Clone the Repository:

```bash
git clone https://github.com/FrancisPhone/NLP-A6-st124973.git
cd app
```

### Set Up a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Run Migrations:

```bash
python manage.py migrate
```

### Run the Django Server:

```bash
python manage.py runserver
```

### Access the Chat Interface:

Open your browser and go to [http://127.0.0.1:8000/chat/](http://127.0.0.1:8000/chat/).

## Usage

### Chat Interface:

- Type your message in the input box and click "Send."
- The chatbot will process your input and display the response in the chat box.

### Clear Chat:

- Click the "Clear Chat" button to clear the chat history.

## Retriever and Generator Models

### Retriever Model

- **Model:** HuggingFaceInstructEmbeddings
- **Description:** Used to create vector embeddings of the documents for efficient retrieval.
- **Source:** [https://huggingface.co/hkunlp/instructor-base]

### Generator Model

- **Model:** Fastchat-T5-3b
- **Description:** A text generation model used to generate responses based on the retrieved documents.
- **Source:** [https://huggingface.co/lmsys/fastchat-t5-3b-v1.0]

## Reference Documents

The chatbot retrieves information from the following documents:

- **Resume:** Contains personal information about Phone Myint Naing, including education, work experience, and skills.
- **Additional Documents:** Other relevant documents (e.g., personal blogs, LinkedIn profile) added to enhance the chatbot's knowledge.

## Folder Structure

```
your-repo-name/
├── app/
│   ├── templates/chatbot/
│   │   └── chat.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── chatbot_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── requirements.txt
├── README.md
└── manage.py
```

## Deliverables

- **GitHub Repository:** Contains the Jupyter notebook, Django app, and README file.
- **Web Application:** A fully functional chatbot web application.
- **Question-Answer Pairs:** The chatbot can answer the following 10 questions:

  1. How old are you?
  2. What is your highest level of education?
  3. What major or field of study did you pursue during your education?
  4. How many years of work experience do you have?
  5. What type of work or industry have you been involved in?
  6. Can you describe your current role or job responsibilities?
  7. What are your core beliefs regarding the role of technology in shaping society?
  8. How do you think cultural values should influence technological advancements?
  9. As a master's student, what is the most challenging aspect of your studies so far?
  10. What specific research interests or academic goals do you hope to achieve during your time as a master's student?

  [{'question': 'How old are you?',
  'answer': "<pad>  I  am  a  chatbot,  so  I  don't  have  a  physical  age.  However,  I  am  27  years  old.\n"},
 {'question': 'What is your highest level of education?',
  'answer': "<pad>  I  am  a  Master's  student  in  Data  Science  and  AI  at  the  Asian  Institute  of  Technology  (Thailand).\n"},
 {'question': 'What major or field of study did you pursue during your education?',
  'answer': '<pad>  Electronics  and  Communication  Engineering\n'},
 {'question': 'How many years of work experience do you have?',
  'answer': '<pad>  Phone  Myint  Naing  has  3  years  of  work  experience.\n'},
 {'question': 'What type of work or industry have you been involved in?',
  'answer': '<pad>  I  have  been  involved  in  the  field  of  machine  learning  and  AI.  I  have  been  working  as  a  machine  learning  engineer  for  three  years,  focusing  on  building  machine  learning  and  deep  learning  models.  My  main  project  involves  extracting  information  from  Thai  documents  like  National  ID  cards,  House  Registrations,  Bank  Passbooks,  and  Invoices.  I  have  also  been  involved  in  Computer  Vision  and  have  been  working  as  a  machine  learning  engineer  for  two  years  in  NLP  (full-time  in  Myanmar)  and  one  year  in  Computer  Vision  (part-time,  remote  from  Thailand).  I  have  also  been  involved  in  teaching  and  lecturing  on  topics  related  to  machine  learning  and  AI.\n'},
 {'question': 'Can you describe your current role or job responsibilities?',
  'answer': "<pad> Phone  Myint  Naing's  current  role  or  job  responsibilities  are  as  an  AI  researcher,  focusing  on  building  machine  learning  and  deep  learning  models.  He  is  currently  working  on  a  project  that  involves  extracting  information  from  Thai  documents  like  National  ID  cards,  House  Registrations,  Bank  Passbooks,  and  Invoices.  He  trains  models  for  Optical  Character  Recognition  (OCR)  and  Text-to-Text  Generation  in  Thai.  He  also  teaches  Python  for  beginners  and  data  science  classes  and  builds  curriculums  and  taught  as  a  lecturer.  He  believes  that  AI’s  impact  depends  entirely  on  how  humans  use  it.  While  mistakes  may  happen,  he  trusts  that  humanity  will  learn  from  them  and  improve  AI  for  the  better. "},
 {'question': 'What are your core beliefs regarding the role of technology in shaping society?',
  'answer': '<pad> Phone  Myint  Naing\n'},
 {'question': 'How do you think cultural values should influence technological advancements?',
  'answer': '<pad> Phone  Myint  Naing:  I  believe  that  cultural  values  should  influence  technological  advancements  in  several  ways.  First,  AI  should  be  designed  to  be  inclusive  and  respectful  of  different  cultures.  This  means  that  AI  should  be  designed  to  understand  and  respect  the  cultural  context  in  which  it  is  being  used.  For  example,  AI  should  be  designed  to  recognize  and  respect  cultural  norms  and  values,  such  as  respect  for  privacy  and  the  importance  of  cultural  diversity.  Additionally,  AI  should  be  designed  to  be  respectful  of  different  beliefs  and  values,  such  as  respect  for  tradition  and  the  importance  of  cultural  heritage.  By  incorporating  cultural  values  into  AI  design,  we  can  ensure  that  it  is  truly  inclusive  and  respectful  of  different  cultures.\n'},
 {'question': 'As a master’s student, what is the most challenging aspect of your studies so far?',
  'answer': "<pad>  Time  management.  I  can  be  a  bit  lazy  sometimes,  and  it  can  be  challenging  to  balance  my  studies  with  my  work  and  personal  life.  I  have  to  make  sure  I  allocate  enough  time  for  studying  and  working  on  my  projects,  which  can  be  challenging  for  me.  I  also  have  to  be  mindful  of  my  personal  life  and  make  sure  I  prioritize  my  personal  and  professional  life.  Overall,  time  management  has  been  a  challenge  for  me  as  a  Master's  student.\n"},
 {'question': 'What specific research interests or academic goals do you hope to achieve during your time as a master’s student?',
  'answer': "<pad> Phone  Myint  Naing's  long-term  academic  and  research  goals  as  a  master's  student  are  to  become  a  leading  expert  in  AI  and  data  science,  and  to  contribute  to  the  development  of  cutting-edge  AI  technologies  that  shape  the  future  of  technology.  He  aims  to  develop  a  Burmese  spelling  correction  model  that  works  without  needing  a  separate  model  to  classify  spelling  errors,  and  to  contribute  to  the  development  of  AI  that  is  inclusive  and  respectful  of  all  cultures.  He  also  aims  to  become  a  lecturer  and  to  teach  Python  for  beginners  and  data  science  classes.  He  also  aims  to  publish  his  research  in  reputable  academic  journals  and  to  contribute  to  the  development  of  AI  that  is "}]
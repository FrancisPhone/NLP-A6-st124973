from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat
from .utils import chain


def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        # Get bot response from the RAG model
        response = chain({"question": user_input})
        bot_response = response['answer'].replace('<pad>', '').replace('< pad>', '').replace('pad>', '')

        # Save chat history to the database
        Chat.objects.create(user_input=user_input, bot_response=bot_response)

        return JsonResponse({'user_input': user_input, 'bot_response': bot_response})

    # Retrieve chat history from the database
    chat_history = Chat.objects.all().order_by('timestamp')
    return render(request, 'chat.html', {'chat_history': chat_history})


def clear_chat(request):
    if request.method == 'POST':
        Chat.objects.all().delete()
        return JsonResponse({'status': 'success'})
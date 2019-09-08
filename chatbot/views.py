from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from django.views.decorators.csrf import csrf_exempt
import json


chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

#trainer = ChatterBotCorpusTrainer(chatbot)

trainerB = ListTrainer(chatbot)

#trainer.train(
#    "C:/Users/Allan/DjChat/djadjachat/chatterbot_corpus/data/english/"
#    )

trainerB.train([
	    "How are you?",
	    "I'm Fine.",
	    "Hello.",
	    "Hello, How can I help?.",
	    "Hi",
	    "Hi, How can I help?",
	    "I am good.",
	    "That is good to hear.",
        "Thanks",
        "I am glad I could help",
	    "Thank you.",
	    "You are welcome.",
        "I need money",
        "You need to check your credit score first to see whether you qualify for a loan",
	    "How can I improve my credit score.",
	    "Do you have any current loans?",
        "Yes I have a loan",
        "You can start by paying your current loans slowly to completion and then later apply for one",
	    "How can I save money",
        "You can cut unnecessary expenditures, pay bills on time, keenly monitor your accounts and avoid bad investments",
	    "my credit score is low",
	    "You can work on that by paying pending loans gradually, monitoring your finances/bills and making payments on time.",
        "Can i get a loan",
	    "Yeah Sure, If your patascore credit score is good apply for one right away.",
	    "I don't qualify for a loan",
        "You can take certain steps in improving your finances and credit score.Do you have a loan?"
	    "How can I improve my credit score?",
        "You can improve your credit score by settling any pending loans you may have, Tracking your bill payments and reciepts for easier account management and accountability and by regularly checking your credit report to be aware of your credit situation",
        "I have a loan.",
	    "I'd advise you to repay any pending loans immediately with the resources you have now and work to improve on that in future.Unserviced loans can badly hurt your credit score.",
	    "I need a loan",
	    "You can take a patascore credit test to check if you have good credit and are elligble for a loan.",
	    "How can I save money",
	    "You can start by paying your bills in time, this will reduce accumulation of debt which affects your credit.",
	    "How can I make payments on time",
	    "You can set up automatic payment systems from your main account to pay your bills or calender reminders if you are not comfortable with automatic payment systems.",
	    "I would suggest you stop borrowing and work hard to lower your your loan balance first",
	    "When can I qualify for a loan",
	    "Once you take a patascore credit test and have good results you can give us a call anytime ;-)",
	    "How often should I take a loan?",
	    "If you need the money and have a system in place to pay back the money, You can consult with us and get one right away",
	    "When are you open?",
        "We are open from Monday to Friday 8:00 am - 5:00 pm and Saturdays from 8:00 am to 12:00 pm",
        "How can I save?",
	    "You can set up alerts to monitor you expenses and usage, this will help you handle your finances better and track profit/losses much more easily",
	    "How can I save?",
	    "You could cut off unnecessary expenditures and re-invest your profits into income-generating practices",
	    "Goodbye",
	    "Have A Good Day ;-)",
	])


@csrf_exempt

def get_response(request):
    response = {'status': None}
    
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data["message"]
        
        chat_response = chatbot.get_response(message).text
        response['message'] = {'text': chat_response, 'user' : False, 'chat_bot' : True}
        response['status'] = 'ok'
    else:
        response['error'] = 'no post data found'

    return HttpResponse(
        json.dumps(response),
                content_type = "application/json"
        )

def home(request, template_name="home.html"):
        context = {"title":'Chatbot v1.0'}
        return render_to_response(template_name,context)
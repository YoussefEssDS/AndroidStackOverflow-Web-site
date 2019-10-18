from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from bs4 import BeautifulSoup
import requests
from .models import Question, Thread
from django.utils.text import unescape_entities
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.

def homepage(request):
	return render(request=request,
				  template_name='main/home.html')


def signup(request):
	if request.method=='POST':
		form=UserCreateForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f"New Account Created: {username}")
			login(request,user)
			messages.info(request,f"Logged in as {username}")
			return redirect("main:homepage")
		else: 
			for msg in form.error_messages:
				messages.error(request,f"{msg}:{form.error_messages[msg]}")

	form=UserCreateForm
	return render(request,
				  'main/signup.html',
				   context={'form':form})


def logout_request(request):
	logout(request)
	messages.info(request,f"Logged out successufully!")
	return redirect('main:homepage')


def login_request(request):
	if request.method=='POST':
		form=AuthenticationForm(request,request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				messages.info(request,f"Logged in as {username}")
				return redirect('main:homepage')
			else:
				messages.error(request,'Invalid username or password')
		else:
				messages.error(request,'Invalid username or password')

	form=AuthenticationForm
	return render(request,'main/login.html',{"form":form})


def recent_quest(request):
	url='https://stackoverflow.com/questions/tagged/android'
	req=requests.get(url) 
	status=req.status_code # Status of the connection attempt if everything is good this should have a 200 value.
	encoding=req.encoding
	text=BeautifulSoup(req.text,'html.parser')
	titles=text.findAll('div',{'class':'summary'})
	votes=text.findAll('span',{'class':'vote-count-post'})
	answers=text.findAll('div',{'class':'status unanswered'})
	links=text.findAll('div',{'class':'summary'})
	i=0
	Ltitles=[]
	Lvotes=[]
	Lanswers=[]
	Llinks=[]
	for item in titles:
		title=item.find('a',{'class':'question-hyperlink'}).text
		Ltitles.append(title)
		i+=1
		if (i==10):
			break
	i=0
	for item in votes:
		Lvotes.append(item.text)
		i+=1
		if (i==10):
			break
	i=0
	for item in answers:
		Lanswers.append(item.find('strong').text)
		i+=1
		if (i==10):
			break
	i=0
	for item in links:
		Llinks.append('https://stackoverflow.com'+item.find('a',{'class':'question-hyperlink'},href=True)['href'])
		i+=1
		if (i==10):
			break

	#Mail notification:
	for q in Question.objects.all():
		q
		break
	if (q.quest_type==0 and Ltitles[0]!=q.quest_title):
		subject = 'New question has been published'
		message = "Hi,\n\n A new question has been published on tackOverflow, with regard to Android programming, the question is: \n"+Ltitles[0]+"\n. For more details visit our website now!"
		email_from = settings.EMAIL_HOST_USER
		users = User.objects.all()
		recipient_list =[]
		for user in users:
			recipient_list.append(user.email)    
		send_mail(subject, message, email_from , recipient_list) 


	Question.objects.all().delete()
	for i in range (10):
		quest=Question(quest_id=i+1,
					   quest_title=Ltitles[i],
					   quest_thread=Llinks[i],
					   quest_votes=Lvotes[i],
					   quest_answers=Lanswers[i],
					   quest_type=0)
		quest.save()
	return render(request=request,
				  template_name='main/recent.html',
				  context={"Questions":Question.objects.all})


def top_quest(request):
	Question.objects.all().delete()
	url='https://stackoverflow.com/questions/tagged/android?sort=MostVotes&edited=true'
	req=requests.get(url) 
	status=req.status_code # Status of the connection attempt if everything is good this should have a 200 value.
	encoding=req.encoding
	text=BeautifulSoup(req.text,'html.parser')
	titles=text.findAll('div',{'class':'summary'})
	votes=text.findAll('span',{'class':'vote-count-post'})
	answers=text.findAll('div',{'class':{'answered-accepted','status answered'}})
	links=text.findAll('div',{'class':'summary'})
	i=0
	Ltitles=[]
	Lvotes=[]
	Lanswers=[]
	Llinks=[]
	for item in titles:
		title=item.find('a',{'class':'question-hyperlink'}).text
		Ltitles.append(title)
		i+=1
		if (i==10):
			break
	i=0
	for item in votes:
		Lvotes.append(item.text)
		i+=1
		if (i==10):
			break
	i=0
	for item in answers:
		Lanswers.append(item.find('strong').text)
		i+=1
		if (i==10):
			break
	i=0
	for item in links:
		Llinks.append('https://stackoverflow.com'+item.find('a',{'class':'question-hyperlink'},href=True)['href'])
		i+=1
		if (i==10):
			break
	for i in range (10):
		quest=Question(quest_id=i+1,
					   quest_title=Ltitles[i],
					   quest_thread=Llinks[i],
					   quest_votes=Lvotes[i],
					   quest_answers=Lanswers[i],
					   quest_type=1)
		quest.save()
	return render(request=request,
				  template_name='main/top.html',
				  context={"Questions":Question.objects.all})


def view(request):
	Thread.objects.all().delete()
	l=request.build_absolute_uri()
	url=l.replace('http://localhost:8000/view?','')
	req=requests.get(url) 
	status=req.status_code # Status of the connection attempt if everything is good this should have a 200 value.
	encoding=req.encoding
	text=BeautifulSoup(req.text,'html.parser')
	title=text.find('a',{'class':'question-hyperlink'}).text
	code="".join([str(tag) for tag in text.find('div',{'class':'post-text'})]).replace('<code>','')
	thr=Thread(title=title,
			   html_code=code,
			   address=url)
	thr.save()
	return render(request=request,
				  template_name='main/view.html',
				  context={"thread":Thread.objects.all})
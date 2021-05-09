from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Complain,Response
from .forms import CreateUser,ComplainForm
from django.http import HttpResponse
from datetime import datetime

##processing responses from an AI response Bot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

##Pdf Printing Utilities
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter,landscape
from reportlab.lib.pagesizes import A4

def home(request):

	context = {}
	return render(request,'base.html',context)
	
#function is working appropriately
def register(request):
	form = CreateUser()
	if request.method == 'POST':
		form = CreateUser(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	context = {'form':form}
	return render(request,'register.html',context)
	
def user_login(request):
	if request.method == 'POST':
		#now verifying the logged in user from data provided by the user
		username1 = request.POST.get('username')
		password1 = request.POST.get('password')

		user = authenticate(request,username=username1,password=password1)
		if user is not None:
			login(request,user)
			return redirect('user')
		else:
			return redirect('login')
	return render(request,'login.html')

def  user(request):
	
	context = {}
	return render(request,'user.html',context)

def user_logout(request):

	logout(request)
	return redirect('login')
def Complain_data(request):
	form = ComplainForm()
	if request.method == 'POST':
		form = ComplainForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data

def complain_form(request,id):
	user = User.objects.get(id=id)
	form = ComplainForm(instance=user)
	#veryfying a post input only
	if request.method == 'POST':
		form = ComplainForm(request.POST)
		if form.is_valid():
			fs = form.save(commit=False)
			fs.user = request.user
			fs.save()
	else:
		form = ComplainForm()
	#reading user information from the database
	complains = user.complain_set.all()
	complain_count = complains.count()
	responses = user.response_set.all()
	countpending = responses.filter(status='pen ding').count()
	countresponded = responses.filter(status='responded').count()
	context = {'form':form,'complains':complains,'complain_count':complain_count,'responses':responses,'countpending':countpending,'countresponded':countresponded}
	return render(request,'complain.html',context)
	
#functionality working correctly 
def delete_complain(request,id):
	complain = Complain.objects.get(id=id)
	if complain == '':
		return HttpResponse('<h2>Complain Not Available</h2>')
	else:
		complain.delete()
		return HttpResponse('<h2>Complained has been Deleted</h2>')

def user_logout(request):
	#now logging out user session
	logout(request)
	return redirect('login')
	
def print_to_pdf(request,id):
	#getting Complain instances
	user = User.objects.get(id=id)
	#reading user information from the database
	complains = user.complain_set.all()
	responses = user.response_set.all()
	#open the pdf and print the Pages required to their desired pdf files
	response = HttpResponse(content_type='application/pdf')
	d = datetime.today().strftime('%Y-%m-%d')
	response['Content-Disposition'] = f'inline: filename="{d}".pdf'
	buffer = BytesIO()
	p = canvas.Canvas(buffer,pagesize=A4)
	#writing the data to output pdf
	#p.setFont("Helvetica",15,leading=None)
	p.setFillColorRGB(0.29296875,0.453125,0.609375) 
	p.drawString(260,800,"Complains Reports:")
	p.line(0,780,1000,780)
	p.line(0,788,1000,778)
	x1 = 50
	y1 = 750
	#now from the dictionary of data print the requiered data items.
	complocation = []
	complTo = []
	commentss = []
	data = {"location":complocation,"ComplainTo":complTo,"Comment":commentss}

	for comp in complains:
		complocation.append(comp.location)
		complTo.append(comp.complains)
		commentss.append(comp.comment)

	for k ,val in data.items():
		p.drawString(x1,y1-10,f"{k}")
		print("\n")
		for v in val:
			p.drawString(x1+20,y1-30,f"{v}")
			y1 = y1 - 60
	p.setTitle(f"Report on {d}")
	p.showPage()
	p.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response

def help_page(request):

	return render(request,'help.html')
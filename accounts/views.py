from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from sales.models import SalesReport

from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth.models import User, auth


def signup(request):
	print('Inside signup*********')
	if request.method == "POST":
			username = request.POST.get('username')
			email = request.POST.get('email') 
			password = request.POST.get('password')
			print(username)
			print(password)
			if User.objects.filter(username=username).exists():
				messages.info(request, 'User Exists')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'Email Exists')
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				user.save();
				return render(request, 'signin.html')
	else:
		return render(request, 'signup.html')

def signin(request):
	print('Entering signin ########')
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username)
		print(password)
		user = auth.authenticate(username=username, password=password)
		print(user)
		if user is not None:
			auth.login(request, user)
			print('user found %%%%%')
			#takes sales value from db
			#pass to index.html
			sales = SalesReport.objects.all()
			return render(request, 'index.html', {'sales':sales});
		else:
			messages.info(request, 'Credentials Incorrect')
			print('user not found')
	else:	
		return render(request, 'signin.html')

#def logout(request):

#    logout(request)
#	message="Logged out"
#    return render(request,'accounts/signin.html', {'message': message})


def logout(request):
	auth_logout(request)
	message="Logged out"
	return redirect('/')
#	return render(request,'accounts/signin.html', {'message':message})
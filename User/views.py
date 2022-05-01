from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
# Create your views here.
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from Phone.models import Phone
from Blog.models import Blog
from Accessory.models import Accessory

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		print(request.POST)
		print(form)
		print(form.is_valid())
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("register")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="pages/register.html", context={"register_form":form})



def login_request(request):
	errorMess = ""
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("./")
			else:
				errorMess = "Tên đăng nhập hoặc mật khẩu không tồn tại"
		else:
			errorMess = "Tên đăng nhập hoặc mật khẩu không tồn tại"
	form = AuthenticationForm()
	return render(request=request, template_name="pages/login.html", context={"errorMessage": errorMess})
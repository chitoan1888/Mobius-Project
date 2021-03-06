from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import NewUserForm
from Cart.models import Cart
from django.contrib import messages


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			Cart.objects.create(user=user)
			messages.success(request, "Registration successful." )
			return redirect("home_view")
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
				return redirect("home_view")
			else:
				errorMess = "Tên đăng nhập hoặc mật khẩu không tồn tại"
		else:
			errorMess = "Tên đăng nhập hoặc mật khẩu không tồn tại"
	form = AuthenticationForm()
	return render(request=request, template_name="pages/login.html", context={"errorMessage": errorMess})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("home_view")
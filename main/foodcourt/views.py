from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import User, Info,Order

def index(request):
	food_items= Info.objects.all()
	context = {"food_items":food_items}
	return render(request, 'foodcourt/index.html',context)

def base(request):
	return render(request, 'foodcourt/base.html')    

def signin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		try:
			user_obj = User.objects.get(username=username, password=password)
			print(user_obj)
			return redirect('/index/')
			
		except User.DoesNotExist:
			return redirect('/signin')

	
	return render(request, 'foodcourt/signin.html')
			


	
	
	


def signup(request):
	if request.method == 'POST':
		username=request.POST['username']
		email = request.POST['email']
		password=request.POST['password']

		user_obj=User()
		user_obj.username=username
		user_obj.email=email
		user_obj.password=password
		user_obj.save()
	else:
		return render(request, "foodcourt/signup.html")

	


def order(request, name_id):
		try:
			user_obj = Order.objects.get(pk=name_id)
			# context={
			# 	'user_obj':user_obj
			# }
			return render(request,"foodcourt/order.html")
		except User.DoesNotExist:
			return redirect('/order')
	
def myorder(request):
	return HttpResponse("this is myorder page")
	
	
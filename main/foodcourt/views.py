from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import User, Info, Order
from django.contrib.auth import authenticate
from django.urls import reverse


def index(request):
    food_items = Info.objects.all()
    context = {"food_items": food_items}
    return render(request, 'foodcourt/index.html', context)






def base(request):
    return render(request, 'foodcourt/base.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user_obj = authenticate(username=username, password=password)
            return redirect('/index/')
        except User.DoesNotExist:
            return redirect('/signin')

    return render(request, 'foodcourt/signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        #user_obj = User()
        data={"username":username,"email":email,"password":password}
        User.objects.create(**data)
        #User.objects.save()
        #user_obj.username = username
        #user_obj.email = email
        #user_obj.password = password
        #user_obj.save()
        return render(request, "foodcourt/signup.html")
    else:
        return render(request, "foodcourt/signup.html")


def order(request, name_id):
    try:
        user = User.objects.get(id=name_id)
        username=user.username
        name=Info.objects.all()
        price=[]
        count=0
        for item in name:
            if item.is_active:
                count= count+1
                price.append(int((item.price)))

        totalprice=sum(price)
        
        data = { 
            'username': username,
            'selecteditems':count,
            'totalamount':totalprice

        }
        context = { 
            'username': username,
            'name_obj':name,
            'totalprice':totalprice,
        }
        Order.objects.create(**data)
        return render(request, 'foodcourt/order.html', context)
    except Exception as e:
        return render(request, 'foodcourt/order.html', context)


def myorder(request):
    try:
        name_obj = User.objects.all()
        context = {'name_obj': name_obj,

                   }
        return render(request, 'foodcourt/myorder.html', context)
    except Info.DoesNotExist:
        return render(request, 'foodcourt/index.html')
from django.urls import path
from . import views


# app_name = foodcourt

urlpatterns=[
    path('',views.base, name='base'),
    path('index/',views.index, name='index'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('<int:name_id>/order/',views.order, name='order'),
    path('myorder/',views.myorder, name='myorder'),
]

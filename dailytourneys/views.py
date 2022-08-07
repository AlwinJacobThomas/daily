from django.shortcuts import render,redirect
from .models import BGMI
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def index(request):
  dests= BGMI.objects.all()
  
  return render (request, 'index.html',{'dests':dests})

def signin(request):
  if request.method == "POST":
     username = request.POST['username']
     password1 = request.POST['password1']

     user = authenticate(username=username,password=password1)

     if user  is not None:
       login(request,user)
       first_name=user.first_name
       return render (request,'index.html',{'first_name':first_name})

     else:
       messages.error(request,"bad credientials")
       return redirect (request,'index')
       
  return render (request, 'login.html',)

def signup(request):
  if request.method == "POST":
     username = request.POST['username']
     first_name = request.POST['first_name']
     orgname = request.POST['orgname']
     email = request.POST['email']
     password1 = request.POST['password1']
     password2 = request.POST['password2']
     about = request.POST['about']

     if User.objects.filter(username=username):
       messages.error(request,"aldreay taken")
       return redirect('index')

     if User.objects.filter(email=email):
       messages.error(request,"email aldreay taken")
       return redirect('index')

     if password1 != password2:
       messages.error(request,"password not matching")
       return redirect('index')


     myuser = User.objects.create_user(username=username,password=password1,first_name = first_name,email=email,orgname = orgname, about = about)
     #myuser.orgname = orgname,
     #myuser.about = about

     myuser.save()
  
     messages.success(request,"created")
  
     return redirect('index')
  return render (request, 'signup.html',)

def signout(request):
    logout(request)
    return redirect('index')

#def postanad(request):
  #if request.method == "POST":
    #user=request.user.username
    #image=request.FILES.get('uploadfile')
    #desc= request.POST['desc']
    #link= request.POST['link']
    #price= request.POST['price']

    #new_post = BGMI.objects.create(user=user,image=image,desc=desc)
    #new_post.save()

    #return redirect('index')

  #else:
    #return redirect('postanad')    
#@login_required(login_url='signin')
#@login_required()
def postanad(request):

    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES.get('img')
        desc = request.POST['desc']
        price = request.POST['price']
        link = request.POST['link']
      
        new_post = BGMI.objects.create(name=name, img=img, desc=desc,price=price,link = link)
        new_post.save()
        return HttpResponse("successful")
        return redirect('index')

    return render(request, 'postanad.html')

def details(request):
    details = BGMI.objects.get(id = id)
    data = {
      'details':details
    }
    return render (request,'details.html',data)


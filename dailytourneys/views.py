from django.shortcuts import render,redirect
from .models import BGMI
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
  dests= BGMI.objects.all()
  
  return render (request, 'index.html',{'dests':dests})

def signin(request):
  if request.method == "POST":
     username = request.POST['username']
     pass1 = request.POST['pass1']

     user = authenticate(username=username,password=pass1)

     if user  is not None:
       login(request,user)
       fname=user.first_name
       return render (request,"index.html",{'fname':fname})

     else:
       messages.error(request,"bad credientials")
       return render(request,'index')
       
  return render (request, 'login.html',)

def signup(request):
  if request.method == "POST":
     username = request.POST['username']
     fname = request.POST['fname']
     orgname = request.POST['orgname']
     email = request.POST['email']
     pass1 = request.POST['pass1']
     pass2 = request.POST['pass2']

     if User.objects.filter(username=username):
       messages.error(request,"aldreay taken")
       return redirect('index')

     if User.objects.filter(email=email):
       messages.error(request,"email aldreay taken")
       return redirect('index')

     if pass1 != pass2:
       messages.error(request,"password not matching")
       return redirect('index')


     myuser = User.objects.create_user(username,email,pass1)
     myuser.first_name = fname

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


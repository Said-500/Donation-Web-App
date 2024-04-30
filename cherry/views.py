from django.shortcuts import render,redirect
from .models import user_data
# Create your views here.
def Home(request):
    return render(request,'Home.html')
def Signup(request):
    return render(request,'Signup.html')
def about(request):
    return render(request,'about.html')
def contactus(request):
    return render(request,'contactus.html')
def login(request):
   print(request.method)
   if request.method == 'POST':
      print(request.POST)
      name = request.POST.get('username')
      user_email = request.POST.get('email')
      user_age = request.POST.get('age')
      user_password = request.POST.get('password')
      user_obj = user_data()
      user_obj.username = name
      user_obj.email = user_email
      user_obj.age = user_age
      user_obj.password = user_password
      user_obj.save()
   return render(request,'login.html')
def edit_fun(request,id):
    userapp = user_data.objects.get(id =id)
    if request.method == 'POST':
      print(request.POST)
      name = request.POST.get('username')
      user_email = request.POST.get('email')
      user_age = request.POST.get('age')
      user_address = request.POST.get('address')
      userapp.username = name
      userapp.email = user_email
      userapp.address = user_age
      userapp.address = user_address
      userapp.save()
      return redirect ('/')
    return render(request,'edit.html',{'user':userapp})
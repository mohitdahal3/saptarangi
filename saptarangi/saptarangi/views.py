from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

def firstpage(request):
   logout(request)
   return render(request , 'home/firstpage.html')

def handlelogin(request):
   if request.method == "POST":
      username = request.POST.get('lusername' , '')
      password = request.POST.get('lpassword' , '')
      user = authenticate(username=username, password=password)
      if user is not None:
         login(request , user)
         messages.success(request , 'You are successfully logged in!')
         return redirect('/home/available-products')
      else:
         messages.error(request , "Login failed")
         return redirect('/')  

   return HttpResponse('bad request')

def handlesignup(request):
   if request.method == "POST":
      fname = request.POST.get("fname" , '')
      lname = request.POST.get("lname" , '')
      username = request.POST.get("suname" , '')
      password1 = request.POST.get('spass1' , '')
      password2 = request.POST.get('spass2' , '')
      if password1!=password2:
         messages.error(request , 'Two passwords did not match!')
         return redirect('/')
      try:   
         user = User.objects.create_user(username=username , password = password1)
         user.first_name = fname
         user.last_name = lname
         user.save()
         login(request , user)
         messages.success(request , 'Account created successfully!')
         return redirect('/home/available-products')
      except Exception as e:
         messages.error(request , 'Error occured! Try changing some values.')
         return redirect('/')   

   return HttpResponse('bad request')        
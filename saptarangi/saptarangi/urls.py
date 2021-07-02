from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
   path('admin/', admin.site.urls),
   path('' , views.firstpage , name = "firstpage"),
   path('home/' , include('home.urls')),
   path('login/' , views.handlelogin , name="login"),
   path('signup/' , views.handlesignup , name="signup")
]

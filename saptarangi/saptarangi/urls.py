from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('admin/', admin.site.urls),
   path('' , views.firstpage , name = "firstpage"),
   path('home/' , include('home.urls')),
   path('login/' , views.handlelogin , name="login"),
   path('signup/' , views.handlesignup , name="signup")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

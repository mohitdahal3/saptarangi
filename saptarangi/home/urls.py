
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home , name="home"),
    path('available-products' , views.available , name = "available"),
    path('view-product-<str:slug>' , views.viewavailableproduct , name = 'viewproduct'),
    path('sold-products' , views.sold , name = "sold"),
    path('addavailable' , views.addavailable , name = "addavailable"),
    path('deleteproduct' , views.deleteproduct , name="delete"),
    path('sellproducts' , views.sellproducts , name="sellproducts"),
    path('search-<str:slug>' , views.search , name="search")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

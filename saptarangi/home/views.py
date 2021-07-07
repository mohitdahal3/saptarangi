from django.shortcuts import render , HttpResponse , redirect
from .models import Available_product , Sold_product
# Create your views here.
def home(request):
   return render(request , 'home/home.html')


def available(request):
   
   allproducts = Available_product.objects.all()
   context = {
      'items':allproducts
   }
   
   

   return render(request , 'home/available.html' , context)

def sold(request):
   allproducts = Sold_product.objects.all()
   context = {
      'items':allproducts
   }
   return render(request , 'home/sold.html' , context)


def addavailable(request):
   if request.method == "POST":
      name = request.POST.get('name' , '')
      added_date = request.POST.get('adate','')
      cost_price = int(request.POST.get('cp',''))
      marked_price = int(request.POST.get('mp' , ''))
      stock = int(request.POST.get('stock' , ''))
      buyed_party = request.POST.get('b-party' , '')
      extra_information = request.POST.get('info' , '')
      print((name) , (added_date) , (cost_price) , (marked_price) , (stock) , (buyed_party) , (extra_information))
      product = Available_product(name = name , added_date = added_date , marked_price = marked_price , cost_price = cost_price , buyed_party = buyed_party , extra_information = extra_information , stock = stock)
      product.save()
      return redirect('/home/available-products')
   return HttpResponse('bad request')   



def viewavailableproduct(request , slug):
   product = Available_product.objects.get(sno = int(slug))
   return render(request , 'home/viewprod.html' , {'item':product})

def deleteproduct(request):
   if request.method == 'POST':
      sno = int(request.POST.get('sno' , ''))
      ptype = request.POST.get('type' , '')
      if(ptype == "available"):
         prod = Available_product.objects.get(sno = sno)
         prod.delete()
         return redirect('/home/available-products')
      elif(ptype == "sold"):
         prod = Sold_product.objects.get(sno = sno)
         prod.delete()  
         return redirect('/home/sold-products') 
      
   return HttpResponse('bad request!')   


def sellproducts(request):
   if request.method == "POST":
      sno = int (request.POST.get('sno' , ''))
      date = request.POST.get('date' , '')
      sp = int(request.POST.get('sp' , ''))
      sold_party = request.POST.get('sold_party' , '')
      extra_information = request.POST.get('extra_information' , '')
      product = Available_product.objects.get(sno = sno)
      sproduct = Sold_product(name = product.name , added_date = product.added_date , sold_date = date , cost_price = product.cost_price , marked_price = product.marked_price , sold_price = sp , buyed_party = product.buyed_party , sold_party = sold_party , extra_information = extra_information)
      sproduct.save()
      if (product.stock > 1):
         product.stock = product.stock - 1
         product.save()
      else:
         product.delete()
      return redirect('/home/sold-products')      
   return HttpResponse('bad request')   


def search(request , slug):
   if request.method == "POST":
      query = request.POST.get('query' , '')
      if(slug == "available"):
         allprods = Available_product.objects.all()
         prods = []
         for item in allprods:
            if (query.lower() in item.name.lower() or query.lower() in item.buyed_party.lower() or query.lower() in item.extra_information.lower()):
               prods.append(item)
         print(query)      
         return render(request , 'home/search.html' , {'query':query , "items":prods , "slug" : 1})      
      elif slug == "sold":   
         allprods = Sold_product.objects.all()
         prods = []
         for item in allprods:
            if (query.lower() in item.name.lower() or query.lower() in item.buyed_party.lower() or query.lower() in item.extra_information.lower()):
               prods.append(item)
         print(query)      
         return render(request , 'home/search.html' , {'query':query , "items":prods , "slug" : 2})      
   return HttpResponse('bad request')

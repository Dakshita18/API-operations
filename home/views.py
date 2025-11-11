from django.shortcuts import render
from django.conf import settings
from django.db import models
import requests
from django.shortcuts import render,get_object_or_404,redirect
from .models import product
from .models import User
from django.http import HttpResponse


def fetch_product(request):
    api_url = "https://fakestoreapi.com/products"
   
    try:
        response = requests.get(api_url)
        response.raise_for_status()  

        data = response.json() 
        for products in data:
            rating_data = products.get('rating', {})
            rating = rating_data.get('rate', 0)
            count = rating_data.get('count', 0)

            product.objects.update_or_create(
                title=products['title'],
                defaults={
                    'price': products['price'],
                    'Description': products['description'],
                    'Image': products['image'],
                    'category': products['category'],
                     'rating': rating,
                    'count': count
                }
            )
            

    except requests.exceptions.RequestException as e:
      print(f"API request failed: {e}")

    # products=product.objects.all()

    # context = {'product':products}
    # return render(request, 'base.html',context)
    return HttpResponse("okay")

def fetch_user(request):
    api_url = "https://fakestoreapi.com/users"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        print(response,"rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
        data = response.json()
        print("data>>>>>>>>>>>>>>>>>>>>>>>",data)
        for item in data:
            User.objects.update_or_create(
                id=item['id'],
                defaults={
                    'email': item.get('email'),
                    'username': (item.get('username')).capitalize(),
                    'password': item.get('password'),
                    'phone': item.get('phone'),
                    'firstname': (item['name']['firstname']).capitalize(),
                    'lastname': (item['name']['lastname'].capitalize()),
                    'city': item['address']['city'],
                    'street': item['address']['street'],
                    'number': item['address']['number'],
                    'zipcode': item['address']['zipcode'],
                    'latitude': item['address']['geolocation']['lat'],
                    'longitude': item['address']['geolocation']['long'],
                }
            )
            print("11111111111111111111111111")

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")

    # users = User.objects.all()
    return HttpResponse("okay")
























from rest_framework import serializers
from .models import User,product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'firstname','lastname',
                   'street','city',  'number', 'zipcode', 'latitude']
        

class productSerializer(serializers.ModelSerializer):
    class Meta: 
         model = product
         fields = [ 'id' ,'title','price', 'Description','Image','category','rating','count']










      
        
   
   
  



















































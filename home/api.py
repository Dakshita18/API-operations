
from django.contrib.auth import get_user_model
from .models import  User,product
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from .serializers import (
UserSerializer,productSerializer)

class UserAPIView(APIView):
    print('inside api')
    def get(self, request, pk=None):
        if pk:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        serializer = UserSerializer(data=request.data)
        print("inside delete function")
        user = get_object_or_404(User, id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class productAPIView(APIView):
    print('inside api')
    def get(self, request, pk=None):
        if pk:
            products = get_object_or_404(product, pk=pk)
            serializer = productSerializer(products)
            return Response(serializer.data)
        else:
            products = product.objects.all()
            serializer = productSerializer(products, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        products = get_object_or_404(User, pk=pk)
        serializer = productSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        serializer = productSerializer(data=request.data)
        print("inside delete function")
        products = get_object_or_404(product,id=pk)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    def patch(self, request, pk):
        products = get_object_or_404(product, pk=pk)
        serializer = productSerializer(products, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)














































































































































































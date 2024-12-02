from django.shortcuts import render
from rest_framework.views import APIView
from bookapi.serializers import boolserializer
from bookapi.models import bookmodel
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from bookapi.permissions import isownerOrreadonly, isownerOrreadonlyobject
from rest_framework.generics import UpdateAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.throttling import AnonRateThrottle
from bookapi.throttling import customanaonthrotling, customuserSthrotling
from bookapi.pagenation import custompagepagination, customcursoepagination, customlimitpagination
# Create your views here.

class bookList(APIView):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        bookdata = bookmodel.objects.all()
        serialized = boolserializer(bookdata, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
   
    def post(self, request):
        serialized = boolserializer(data = request.data)
        if(serialized.is_valid()):
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
            
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
class updatebook(UpdateAPIView):
    queryset = bookmodel.objects.all()
    serializer_class = boolserializer
    permission_classes = [isownerOrreadonlyobject]

    
class bookDetails(APIView):
    permission_classes = [isownerOrreadonlyobject]
    def get(self, request, pk):
        bookdata = bookmodel.objects.get(pk =pk)
        self.check_object_permissions(request, bookdata)
        serialized = boolserializer(bookdata)
        return Response(serialized.data, status=status.HTTP_200_OK)
    def post(self, request, pk):
        bookdata = bookmodel.objects.get(pk =pk)
        serialized = boolserializer(bookdata, data= request.data)
        self.check_object_permissions(request, bookdata)
        if(serialized.is_valid()):
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        bookdata = get_object_or_404(bookmodel,pk =pk)
        self.check_object_permissions(request, bookdata)
        bookdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class bookoperations(APIView):
   def get(self, request):
       if request.query_params:
        #    data = bookmodel.objects.filter(**request.query_params.dict())
           data = bookmodel.objects.filter()
           serialized = boolserializer(data, many=True)
           return Response(serialized.data, status=status.HTTP_200_OK)
       return Response( status=status.HTTP_400_BAD_REQUEST)
   
    
class booksort(APIView):
    
   def get(self, request, pk):
           data = bookmodel.objects.order_by('-price')
           serialized = boolserializer(data, many=True)
           return Response(serialized.data, status=status.HTTP_200_OK)

   def post(self, request,pk):
           data = bookmodel.objects.order_by(-pk)
           serialized = boolserializer(data, many=True)
           return Response(serialized.data, status=status.HTTP_200_OK)
       
    
class Listbook(ListAPIView):
    queryset = bookmodel.objects.all()
    serializer_class = boolserializer
    permission_classes = [isownerOrreadonly]
    throttle_classes = [customuserSthrotling]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['langauge']
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['price','langauge' ]
    # # filter_backends = [filters.SearchFilter]
    # # ordering_fields = ['price','langauge' ]
    pagination_class = customlimitpagination
   

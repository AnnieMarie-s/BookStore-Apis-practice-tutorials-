from  bookapi.user.serializers import Registerationserializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import serializers
# from bookapi.user.models import create_auth_token
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def registration_view(request):
    account = Registerationserializer(data=request.data)
    data = {}
    if(account.is_valid()):
        account = account.save()
        data['response'] ='successfully registered'
        data['username'] = account.username
        # token = Token.objects.get(user = account ).key
        # data['token'] = token
        refresh = RefreshToken.for_user(account)
        data['token'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    else:
        data = account.errors

    return Response(data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logout_view(request):
    if request.method =='POST':
        request.user.auth_token.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
        
    

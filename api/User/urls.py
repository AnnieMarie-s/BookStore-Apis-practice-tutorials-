
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from bookapi.user.views import registration_view, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('account/token', obtain_auth_token),
    path('account/registration', registration_view),
    path('account/logout/', logout_view),
    path('account/jtoken/', TokenObtainPairView.as_view()),
    path('account/Resfresh/', TokenRefreshView.as_view()),
   
]

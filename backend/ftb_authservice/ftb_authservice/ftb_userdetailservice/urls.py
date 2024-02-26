from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import  views

base_path = "ftbscheduler/api/v1/"

urlpatterns = [
    path(base_path+'ping', views.ping, name="ping"),
    path(base_path+'register', views.register, name="register"),
    path(base_path+'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(base_path+'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
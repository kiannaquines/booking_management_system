from django.urls import path
from authentication.views import auth_login

urlpatterns = [
    path('login/',auth_login,name="auth_login")
]
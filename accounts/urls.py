from django.urls import path
from .views import signup, login, send_otp, verify_otp

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('send-otp/', send_otp),
    path('verify-otp/', verify_otp),
]
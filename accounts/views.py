from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import UserProfile
from django.http import JsonResponse
import json

@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        full_name = data.get("full_name")
        address = data.get("address")
        mobile_number = data.get("mobile_number")

        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # create profile
        UserProfile.objects.create(
            user=user,
            full_name=full_name,
            address=address,
            mobile_number=mobile_number
        )

        return JsonResponse({"message": "User created successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        return Response({"message": "Login successful"})
    else:
        return Response({"message": "Invalid credentials"})
    




import random
from django.core.mail import send_mail

otp_storage = {}

@api_view(['POST'])
def send_otp(request):
    data = request.data
    email = data.get("email")

    otp = str(random.randint(100000, 999999))
    print("OTP:", otp)

    otp_storage[email] = otp

    send_mail(
        "Your OTP Code",
        f"Your OTP is {otp}",
        "test@gmail.com",
        [email],
        fail_silently=False,
    )

    return Response({"message": "OTP sent"})


@api_view(['POST'])
def verify_otp(request):
    data = request.data
    email = data.get("email")
    otp = data.get("otp")

    if email in otp_storage and otp_storage[email] == otp:
        return Response({"message": "OTP verified"})
    else:
        return Response({"message": "Invalid OTP"}, status=400)

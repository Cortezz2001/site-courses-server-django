import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import  get_token


def get_token_csrf(request):
    token = get_token(request)
    json_response = {
        "status": "succesfully",
        "errors": "no_errors",
        "token": token,
    }
    return JsonResponse(json_response)

@csrf_exempt
def user_registration(request):

    json_response = {
        "status":"no_status",
        "errors":"no_errors",
    }

    json_data = request.body

    if json_data is None:
        json_response["status"] = "failed"
        json_response["errors"] = "Not found data"
        return JsonResponse(json_response)

    data = json.loads(json_data.decode('utf-8'))

    #Проверка сушествования пользователя
    mail_exist = User.objects.filter(email=data["email"]).exists()

    if mail_exist:
        json_response["status"] = "failed"
        json_response["errors"] = "User with this mail is exist"
    else:
        user = User.objects.create_user(data["email"], data["email"], data["password"])

        user.first_name = data["firstname"]
        user.last_name = data["lastname"]
        user.save()
        json_response["status"] = "succesfully"

    return JsonResponse(json_response)


@csrf_exempt
def user_authentification(request):

    json_response = {
        "status":"no_status",
        "errors":"no_errors",
    }

    json_data = request.body
    # Проверка сушествования json_data
    if json_data == None:
        json_response["status"] = "failed"
        json_response["errors"] = "Not found data"
        return JsonResponse(json_response)

    data = json.loads(json_data.decode('utf-8'))

    #Проверка сушествования пользователя
    user = authenticate(username=data["email"], password=data["password"])
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        json_response["status"] = "succesfully"
    else:
        # No backend authenticated the credentials
        json_response["status"] = "failed"
        json_response["errors"] = "wrong login or password"

    return JsonResponse(json_response)


@csrf_exempt
def check_user_authentification(request):

    json_response = {
        "status":"no_status",
        "errors":"no_errors",
    }
    json_data = request.body
    # Проверка сушествования json_data
    if json_data is None:
        json_response["status"] = "failed"
        json_response["errors"] = "Not found data"
        return JsonResponse(json_response)


    data = json.loads(json_data.decode('utf-8'))

    #Проверка сушествования пользователя
    user = User.objects.get(username=data["email"])

    if user.is_authenticated:
        # A backend authenticated the credentials
        json_response["status"] = "succesfully"
    else:
        # No backend authenticated the credentials
        json_response["status"] = "failed"
        json_response["errors"] = "user is not autentificated"

    return JsonResponse(json_response)

@csrf_exempt
def user_logout(request):

    json_response = {
        "status":"no_status",
        "errors":"no_errors",
    }

    json_data = request.body
    # Проверка сушествования json_data
    if json_data is None:
        json_response["status"] = "failed"
        json_response["errors"] = "Not found data"
        return JsonResponse(json_response)


    data = json.loads(json_data.decode('utf-8'))

    #Проверка сушествования пользователя
    user = User.objects.get(username=data["email"])

    if user is not None and  user.is_authenticated:
        # A backend authenticated the credentials
        logout(user)
        json_response["status"] = "succesfully"
    else:
        # No backend authenticated the credentials
        json_response["status"] = "failed"
        json_response["errors"] = "user is not autentificated or user not found"

    return JsonResponse(json_response)

# использование токена на фронте
# var
# token = '{{csrf_token}}';  # передаем токен из вью
#
# $.ajax({
#     headers: {"X-CSRFToken": token},  # добавляем его в наш запрос
#
#     type: "POST",
#     url: "/some_view/",
#     data: {
#         data
#     },
#     success: function() {
#         ...

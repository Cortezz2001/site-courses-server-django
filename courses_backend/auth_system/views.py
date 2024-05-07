from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class Logout(APIView):
    def get(selfself,request,format=None):
        request.user.auth_token.delete()
        json_response = {
            "status": "ok",
        }
        return JsonResponse(json_response)

class CheckAuth(APIView):
    permission_classes = [IsAuthenticated]
    def get(selfself,request,format=None):
        json_response = {
            "status": "ok",
        }
        return JsonResponse(json_response)


from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(selfself,request,format=None):
        request.user.auth_token.delete()
        return Response({'message': 'OK'}, status=200)

class CheckAuth(APIView):
    permission_classes = [IsAuthenticated]
    def get(selfself,request,format=None):
        return Response({'message': 'OK'}, status=200)


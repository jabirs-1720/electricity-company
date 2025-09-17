from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .permissions import GuestOnly
from .serializers import LoginSerializer

# Create your views here.

def provide_user_data(user):
    return {
        'username': user.username,
        'name': user.get_full_name(),
        'email': user.email,
    }

@ensure_csrf_cookie
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user(request):
    if request.user.is_authenticated:
        return Response(provide_user_data(request.user), status=200)
    return Response({}, status=204)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    auth_logout(request)
    response = Response({'message': 'Logged out successfully'}, status=200)
    response.delete_cookie('sessionid')
    return response

class Login(GenericAPIView):
    permission_classes = [GuestOnly]
    serialzier_class = LoginSerializer

# views.py

from rest_framework import generics, permissions, filters
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout
from .models import CustomUser, Category, Tag, Post, Comment
from .serializers import CustomUserSerializer, CategorySerializer, TagSerializer, PostSerializer, CommentSerializer


# Login view
class LoginView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            login(request, user)
            return Response({'detail': 'Login successful.'})
        else:
            return Response({'detail': 'Invalid credentials.'}, status=400)


# Logout view
class LogoutView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'detail': 'Logout successful.'})


# Existing code from views.py


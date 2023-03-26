from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from baseAPI.models import DesignModel
from baseAPI.serializers import DesignSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# New User Registration
class RegistrationView(APIView):
    # Post request
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['email'] = user.email
            data['username'] = user.username
            token = RefreshToken.for_user(user)
            data['refresh'] = str(token)
            data['access'] = str(token.access_token)
        else:
            data = serializer.errors
        return Response(data)

# Logout Class
class LogoutView(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Post request
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Design Detail class
class DesignDetail(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Get design by id
    def get_object(self, id):
        try:
            return DesignModel.objects.get(pk=id)
        except DesignModel.DoesNotExist:
            raise Http404
    # Get API design by id 
    def get(self, request, id):
        design = self.get_object(id)
        serializer = DesignSerializer(design)
        return Response(serializer.data)
    # Post API design by id 
    def post(self, request):
        serializer = DesignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete API design by id
    def delete(self, request, id):
        DesignModel.objects.all(pk=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # Put API design by id
    def put(self, request, id):
        design = DesignModel.objects.get(pk=id)
        serializer = DesignSerializer(design, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        
# Designs List class      
class DesignList(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Get all designs
    def get(self, request):
        designs = DesignModel.objects.all()
        serializer = DesignSerializer(designs, many=True)
        return Response(serializer.data)
        
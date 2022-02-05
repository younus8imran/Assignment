from django.shortcuts import render
from rest_framework import viewsets 

from .models import Profile
from .serializers import ProfileSerializer


## security authentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication






# viewsets for drf 
class ProfileViewSet(viewsets.ModelViewSet):
	## authentication_classes = [TokenAuthentication]
	## permission_classes = [IsAuthenticated]
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer


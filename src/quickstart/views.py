from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializers,GroupSerializers

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializers
    permission_classes=[permissions.IsAuthenticated]


class GroupViewSets(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset=Group.objects.all()
    serializer_class=GroupSerializers
    permission_classes=[permissions.IsAuthenticated]
    
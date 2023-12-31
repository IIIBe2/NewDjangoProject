#from django.shortcuts import render
#from rest_framework.views import APIView

from django.contrib.auth.models import User, Group
from appsite.models import UserCustom, Lesson, Product
from rest_framework import viewsets
from rest_framework import permissions
from appsite.serializers import UserSerializer, GroupSerializer, UserCustomLessonsSerializer, LessonUserSerializer, LessonUser2Serializer
from appuser.models import UserCustomPermission

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserCustomLessonsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = UserCustomLessonsSerializer
    permission_classes = [permissions.IsAuthenticated] 

class LessonUserSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserCustom.objects.all()
    serializer_class = LessonUserSerializer
    permission_classes = [permissions.IsAuthenticated] 

class LessonUser2SerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserCustomPermission.objects.all()
    serializer_class = LessonUser2Serializer
    permission_classes = [permissions.IsAuthenticated] 
import sqlite3
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from appsite.models import UserCustom, Lesson, Product
from appuser.models import UserCustomPermission

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class User:
    def __init__(self, username):
        self.username = username

#class LessonUser:
#    def __init__(self, name, TimeWatch, viewed, user: User):
#        self.name = name
#        self.TimeWatch = TimeWatch
#        self.viewed = viewed
#        self.user = user

class LessonUserSerializer(serializers.Serializer):
    name = serializers.CharField(source='nameuser', max_length=200)
    TimeWatch = serializers.IntegerField()
    viewed = serializers.CharField()
    Lessonname = serializers.CharField()

class LessonUser2Serializer(serializers.Serializer):
    name = serializers.CharField()
    OpenProduct = serializers.CharField()
    LessonsProd = serializers.CharField()
    #viewed = serializers.CharField()
    #Lessonname = serializers.CharField()

class UserCustomLessonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        db = sqlite3.connect('db.sqlite3')
        #cur = db.cursor()
        #lessonsGET = cur.execute(f'SELECT secondsLesson FROM appsite_lesson Where name = ').fetchone()[0]
        #cur.close
        fields = ['name']
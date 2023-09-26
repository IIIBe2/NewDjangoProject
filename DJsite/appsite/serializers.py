import sqlite3
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from appsite.models import UserCustom, Lesson, Product

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserCustomLessonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        db = sqlite3.connect('db.sqlite3')
        cur = db.cursor()
        lessonsGET = cur.execute(f'SELECT secondsLesson FROM appsite_lesson Where name = ').fetchone()[0]
        cur.close
        fields = ['name']
from django.contrib.auth.models import User
from oAuth.models import NewUser, Books
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['url', 'username', 'email', 'is_staff']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

from rest_framework import serializers
# files 是 app 的名字
from oAuth import models


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilesModel
        fields = '__all__'


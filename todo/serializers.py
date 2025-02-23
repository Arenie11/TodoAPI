from .models import Todo
from rest_framework import serializers
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields= '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username']

class RegistrationSerializer(serializers.Serializer):
        password1= serializers.CharField(write_only= True)
        password2= serializers.CharField(write_only= True)
        username= serializers.CharField(write_only =True)
        def validate(self,data):
            if data.get ['password1'] != data.get ['password2']:
                 raise serializers.ValidationError('password does not match')
            return data
        def create(self, validated_data):
             username= validated_data.pop ('username')
             password= validated_data.pop ('password1')
#creating user
             user= User.objects.create_user(username=username, password=password)
             return user
            

        

        

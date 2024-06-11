from rest_framework import serializers
from .models import Client
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate_registration_number(self, value):
        if Client.objects.filter(registration_number=value).exists():
            raise serializers.ValidationError("Client with this registration number already exists.")
        return value


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_login'] = self.fields['username']
        del self.fields['username']

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

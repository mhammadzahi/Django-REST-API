from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensures password is write-only
        }

    def create(self, validated_data):
        # Hash the password before saving the User instance
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            created_at=validated_data['created_at']
        )
        user.set_password(validated_data['password'])  # Hashes the password
        user.save()
        return user

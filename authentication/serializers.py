from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""
    password = serializers.CharField(min_length=5, write_only=True)
    aka = serializers.CharField(max_length=25, required=False)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name', 'last_name', 'aka')

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
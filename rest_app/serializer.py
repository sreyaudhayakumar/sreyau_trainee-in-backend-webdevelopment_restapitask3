from rest_framework import serializers
from .models import Role, User

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'status', 'role']

    def create(self, validated_data):
        role_data = validated_data.pop('role')
        role_instance = Role.objects.create(**role_data)
        user = User.objects.create(role=role_instance, **validated_data)
        return user

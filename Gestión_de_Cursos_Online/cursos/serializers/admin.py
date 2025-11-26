# users/serializers/admin.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UserAdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id','email','username','description','subtitulo','level','title',
            'code','is_active','costo','modal','date_inicio', 'time','pasword'
        )
        read_only_fields = ('id','username','modal')

class UserAdminWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = (
            'username','email','description','title','level'
            'is_active','date_inicio','time','password'
        )

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        user.set_password(password or User.objects.make_random_password())
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for k,v in validated_data.items():
            setattr(instance, k, v)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
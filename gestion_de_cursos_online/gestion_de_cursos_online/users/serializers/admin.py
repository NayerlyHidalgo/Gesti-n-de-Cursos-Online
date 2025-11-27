# users/serializers/admin.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UserAdminListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id','username','email','code','title','costo', 'module','date'
            'is_active','subtitulo','descriptions','level','time','password'
        )
        read_only_fields = ('id','title','module')

class UserAdminWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = (
            'username','email','code','title',
            'is_active','module','password'
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
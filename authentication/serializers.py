from django.contrib.auth import get_user_model, authenticate
from django.core.validators import validate_email

from rest_framework import serializers

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        write_only=True,
        label='البريد الإلكتروني'
    )
    password = serializers.CharField(
        write_only=True,
        label='كلمة المرور'
    )

    class Meta:
        fields = '__all__'

    def validate_email(self, value):
        try:
            validate_email(value)
        except serializers.ValidationError:
            raise serializers.ValidationError('صيغة خاطئة')

        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('بريد إلكتروني خاطئ')

        return value

    def validate(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
    
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('بيانات الدخول غير صحيحة')
        validated_data['user'] = user

        return validated_data

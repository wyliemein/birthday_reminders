from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'message', 'phone_number',
            'birthday', 'created_at', 'updated_at'
        )

from rest_framework import serializers


class SerializerTextReview(serializers.Serializer):
    text = serializers.CharField(required = True)

    def create(self, validated_data):
        return SerializerTextReview.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.text = validated_data.get('text',instance.text)
        instance.save()
        return instance

    def get_attribute(self, instance):
        return super().get_attribute(instance)

        
    def get_fields(self):
        return super().get_fields()
       
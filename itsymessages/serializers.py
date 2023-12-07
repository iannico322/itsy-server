from rest_framework import serializers
from itsymessages.models import ItsyMessage

class ItsyMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItsyMessage
        fields = ("messageID","userID","messageContent")

    def create(self, validated_data):
        message, created = ItsyMessage.objects.update_or_create(
            userID=validated_data.get('userID', None),
            defaults={'messageContent': validated_data.get('messageContent', None)},
        )
        return message

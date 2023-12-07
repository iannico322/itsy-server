from django.db import models

# Model for ItsyMessage

class ItsyMessage(models.Model):
    messageID = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    messageContent = models.CharField(max_length=10000)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

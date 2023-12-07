from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from itsymessages.models import ItsyMessage
from itsymessages.serializers import ItsyMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def itsymessages_by_user(request, userID):
    if request.method == 'GET':
        itsymessages = ItsyMessage.objects.filter(userID=userID)
        serializer = ItsyMessageSerializer(itsymessages, many=True)
        return Response(serializer.data)

class ItsyMessageListCreateApiView(ListCreateAPIView):
    serializer_class = ItsyMessageSerializer
    queryset = ItsyMessage.objects.all()
    
class ItsyMessageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItsyMessageSerializer
    queryset = ItsyMessage.objects.all()
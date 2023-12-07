from django.urls import path

from itsymessages.views import itsymessages_by_user,ItsyMessageRetrieveUpdateDestroyAPIView,ItsyMessageListCreateApiView
from . import views
urlpatterns = [
      path('all/', ItsyMessageListCreateApiView.as_view(),name=''),
      path('<int:pk>', ItsyMessageRetrieveUpdateDestroyAPIView.as_view(),name=''),
      path('user/<str:userID>', views.itsymessages_by_user),
]

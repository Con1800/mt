from django.urls import path
from .views import HelloappView

urlpatterns = [
    path('test/', HelloappView.as_view())
]

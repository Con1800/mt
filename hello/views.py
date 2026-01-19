from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Helloapp
from .serializers import HelloappSerializer

# Create your views here.

#def hello(request):
    #return HttpResponse("hello")

class HelloappView(APIView):
    def get(self,request):
        hello = Helloapp.objects.all().order_by('name')
        serializer = HelloappSerializer(hello, many=True)
        return Response(serializer.data)

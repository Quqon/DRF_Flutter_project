from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def hello_world(request):
    return render(request, "accountapp/temp.html")


@api_view()
def hello_world_drf(request):
    return Response({"message": "hello world!"})
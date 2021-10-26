from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


# @api_view()
# def hello_world(request):
#     return Response({'msg':"hello world"})


# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':"hello world"})



@api_view(['POST', 'GET'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'this is get response', 'data': request.data})


    if request.method == 'POST':
        print(request.data)
        return Response({"msg":"this is post method"})
    
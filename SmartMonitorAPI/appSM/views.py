from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def helloword(request):
    data = {"message": "Hello, world!"}
    return Response(data, status=status.HTTP_200_OK)

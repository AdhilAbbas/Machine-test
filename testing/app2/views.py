from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UploadSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Upload
# Create your views here.

class Uploadview(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def main_view(request):
#     obj = Upload.objects.get(id=9)
#     context = {'obj':obj}
#     return render(request,'app2/main.html',context)


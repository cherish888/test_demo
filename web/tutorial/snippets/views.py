from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

class SnippetList(APIView):
    def get(self,request,format=None):
            serializer = SnippetSerializer(Snippet.objects.all(),many=True)
            return Response(serializer.data)
    def post(self,request,format=None):
            serializer = SnippetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    def get_object(self,request, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
            serializer = SnippetSerializer(self.get_object(pk))
            return Response(serializer.data)
    def put(self,request,pk,format=None):
        serializer = SnippetSerializer(self.get_object(pk),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
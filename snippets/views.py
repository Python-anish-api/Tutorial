# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from rest_framework import status
# from rest_framework.response import Response

# from rest_framework.decorators import api_view

# from snippets.serializers import SnippetSerializer


# # Create your views here.
# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """list all code snippets and add create a new snippet"""
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         print(serializer)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)

#         return JsonResponse(serializer.errors, status=400)


# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """Retrieve, update or delete a code snippet."""
#     try:
#         snippet =Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         print(serializer)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         print(data)
#         print(type(data))
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

"""views finished and class base started"""

# from snippets.models import Snippet
# from rest_framework import status
# from rest_framework.response import Response
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView


# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         print(serializer.data)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         print(request.data)
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


# class SnippetDetail(APIView):
#     '''returns a SnippetDetail, and retrives , updates and delete the instance of snippet'''
#     def get_object(self ,pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except  Snippet.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk, format=None):
#         snippet =self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    
    
#     def put(self, request, pk, format=None):
#         print(request.data)
#         snippet =self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""class base with mixins started"""


# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework import mixins
# from rest_framework import generics


# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
    
    

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)    


"""using generic class based viewe"""


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    def get_queryset(self):
        """
        Optionally, apply filters or modifications to the queryset based on self.request or other conditions.
        """

        return Snippet.objects.filter(linenos=False)  # Directly return the queryset
    serializer_class = SnippetSerializer
    
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer    
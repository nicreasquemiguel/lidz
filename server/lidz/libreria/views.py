from django.shortcuts import render
from rest_framework import generics
from .serializers import AutorModelSerializer, LibroModelSerializer
from .models import Autor, Libro


class LibroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroModelSerializer


class LibroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroModelSerializer
    lookup_field = "id"



class AutorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorModelSerializer
    
    
class AutorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorModelSerializer
    lookup_field = "id"

    
from django.urls import path
from .views import AutorListCreateAPIView, AutorRetrieveUpdateDestroyAPIView, LibroListCreateAPIView, LibroRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('libros/', LibroListCreateAPIView.as_view()),
    path('libros/<id>', LibroRetrieveUpdateDestroyAPIView.as_view()),
    
    path('autores/', AutorListCreateAPIView.as_view()),
    path('autores/<id>/', AutorRetrieveUpdateDestroyAPIView.as_view()),

]

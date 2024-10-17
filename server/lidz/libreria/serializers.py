from rest_framework import serializers
from .models import Libro, Autor


class LibroModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = "__all__"
        # depth = 1
        
    def __init__(self, *args, **kwargs):
        super(LibroModelSerializer, self).__init__(*args, **kwargs)
        # Customize serialization depth based on the request method.
        request = self.context.get('request')
        if request and request.method == 'GET':
            # When creating a new product FAQ, set serialization depth to 0.
            self.Meta.depth = 1
        else:
            # For other methods, set serialization depth to 3.
            self.Meta.depth = 0
        
class AutorModelSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Autor
        fields = "__all__"
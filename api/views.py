from rest_framework import generics, status
from rest_framework.response import Response
from .models import MasterCategory, MasterService
from .serializers import MasterCategorySerializer, MasterServiceSerializer
from django.core.exceptions import ValidationError
from django.db import IntegrityError

    
class MasterCategoryListCreateView(generics.ListCreateAPIView):
    queryset = MasterCategory.objects.all().order_by('priority')
    serializer_class = MasterCategorySerializer
    filterset_fields = ['gender', 'name']

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        gender = request.data.get('gender')

        if MasterCategory.objects.filter(name=name, gender=gender).exists():
            return Response({"error": "This name for the specified gender already exists."}, status=status.HTTP_409_CONFLICT) 
        
        
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MasterCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MasterCategory.objects.all().order_by('priority')
    serializer_class = MasterCategorySerializer


class MasterServiceListCreateView(generics.ListCreateAPIView):
    queryset = MasterService.objects.all().order_by('priority')
    serializer_class = MasterServiceSerializer
    filterset_fields = ['gender', 'service_name', 'categories']


class MasterServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MasterService.objects.all().order_by('priority')
    serializer_class = MasterServiceSerializer

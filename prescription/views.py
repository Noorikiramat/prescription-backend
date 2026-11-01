from rest_framework import viewsets, filters
from .models import Medicine, Prescription
from .serializers import MedicineSerializer, PrescriptionSerializer


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'form']


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient_name']
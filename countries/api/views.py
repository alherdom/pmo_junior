from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from countries.models import Country
from countries.api.serializers import CountrySerializer

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
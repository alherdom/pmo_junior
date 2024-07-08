from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from sellers.models import Seller
from sellers.api.serializers import SellerSerializer


class SellerListView(generics.ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerDetailView(generics.RetrieveAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

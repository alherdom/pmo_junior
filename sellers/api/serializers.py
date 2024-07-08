from rest_framework import serializers
from sellers.models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = 'seller_id', 'language', 'team'

from rest_framework import serializers
from sales.models import Sale
from sellers.api.serializers import SellerSerializer


class SaleSerializer(serializers.ModelSerializer):
    sellers = SellerSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ('date', 'order_number', 'country', 'sellers', 'type', 'income')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        sellers = representation.pop('sellers')
        representation['order number'] = representation.pop('order_number')

        for seller in sellers:
            representation['seller id'] = seller['seller_id']
            representation['seller language'] = seller['language']
            representation['seller team'] = seller['team']
        return representation

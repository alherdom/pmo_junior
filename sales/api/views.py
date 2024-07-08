from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_csv.renderers import CSVRenderer
from rest_framework import generics
from sales.models import Sale
from sales.api.serializers import SaleSerializer
from django.http import HttpResponse


class SaleListView(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleDetailView(generics.RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class CustomCSVRenderer(CSVRenderer):
    header = [
        'date',
        'order number',
        'country',
        'seller id',
        'seller language',
        'seller team',
        'type',
        'income',
    ]


class SalesReportByDate(APIView):
    renderer_classes = [CustomCSVRenderer]

    def get(self, request, date):
        sales = Sale.objects.filter(date=date).order_by('date')
        serializer = SaleSerializer(sales, many=True)
        response = Response(serializer.data)

        if request.accepted_renderer.format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="sales_{date}.csv"'
            renderer = CustomCSVRenderer()
            response.content = renderer.render(serializer.data)

        return response


class SalesReportByMonth(APIView):
    renderer_classes = [JSONRenderer, CustomCSVRenderer]

    def get(self, request, year, month):
        sales = Sale.objects.filter(date__year=year, date__month=month).order_by('date')
        serializer = SaleSerializer(sales, many=True)
        response = Response(serializer.data)

        if request.accepted_renderer.format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="sales_{year}_{month:02}.csv"'
            renderer = CustomCSVRenderer()
            response.content = renderer.render(serializer.data)

        return response

from django.urls import path
from .views import SaleListView, SaleDetailView, SalesReportByDate, SalesReportByMonth

app_name = 'sales'

urlpatterns = [
    path('', SaleListView.as_view(), name='sale_list'),
    path('detail/<str:pk>/', SaleDetailView.as_view(), name='sale_detail'),
    path('date/<str:date>/', SalesReportByDate.as_view(), name='sale_report_by_date'),
    path(
        'month/<int:year>/<int:month>/', SalesReportByMonth.as_view(), name='sales_report_by_month'
    ),
]

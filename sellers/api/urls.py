from django.urls import path
from .views import SellerListView, SellerDetailView

app_name = 'sellers'

urlpatterns = [
    path('', SellerListView.as_view(), name='seller_list'),
    path('<str:pk>/', SellerDetailView.as_view(), name='seller_detail'),
]
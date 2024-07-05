from django.urls import path
from .views import CountryList, CountryDetail

app_name = 'countries'

urlpatterns = [
    path('', CountryList.as_view(), name='country_list'),
    path('<str:pk>/', CountryDetail.as_view(), name='country_detail'),
]
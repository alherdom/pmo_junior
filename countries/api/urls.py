from django.urls import path
from .views import CountryListView, CountryDetailView

app_name = 'countries'

urlpatterns = [
    path('', CountryListView.as_view(), name='country_list'),
    path('<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
]
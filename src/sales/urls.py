from django.urls import path
from .views import (
    home_view,
    SaleListView,
    SalesDetailView,
)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SaleListView.as_view(), name='list'),
    path('sales/<pk>/', SalesDetailView.as_view(), name='detail'),
]
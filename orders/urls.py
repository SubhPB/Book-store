#  byimaan

from .views import OrdersPageView, charge
from django.urls import path

urlpatterns = [
    path('charge/', charge, name='charge'),
    path('', OrdersPageView.as_view(), name='orders')
]
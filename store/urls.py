from django.urls import path
from . import views

urlpatterns = [
    # Root URL points to product_list
    path('', views.product_list, name='product_list'),
]

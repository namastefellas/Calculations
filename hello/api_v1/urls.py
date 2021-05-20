from django.urls import path
from api_v1.views import add, subtract, multiply, divide 

app_name = 'api_v1'

urlpatterns = [
    path('add/', add, name='test_add'),
    path('subtract/', subtract, name='test_subtract'),
    path('multiply/', multiply, name='test_multiply'),
    path('divide/', divide, name='test_divide')
] 
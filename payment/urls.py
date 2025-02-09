from django.urls import path
from .views import *

urlpatterns = [
    path('make_payment/<int:user_id>/', payment.as_view(), name='make_payment'),
    path('payment-success/<int:user_id>/', PaymentSuccessView.as_view(), name='payment-success'),
    path('payment-failed/<int:user_id>/', PaymentFailedView.as_view(), name='payment-failed'),
    path('status/<int:user_id>/', status, name="status"),
]

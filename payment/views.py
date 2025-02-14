from .models import *
from sslcommerz_lib import SSLCOMMERZ 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect, JsonResponse
from account.models import Profile
from rest_framework import viewsets
from .serializers import *
from job.models import AppliedJob

class CheckoutView(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class payment(APIView):
    def post(self, request, user_id, *args, **kwargs):
        user = User.objects.get(id=user_id)
        data = Checkout.objects.filter(sender=user, Order=False).first()
        settings = {
            'store_id': 'snapb6780925c46a95',
            'store_pass': 'snapb6780925c46a95@ssl',
            'issandbox': True,
        }
        sslcz = SSLCOMMERZ(settings)
        post_body = {
            'total_amount': data.total_amount,
            'currency': "BDT",
            'tran_id': data.tran_id,
            'success_url': f"https://nexthire-backend.vercel.app/payment/payment-success/{user_id}/",
            'fail_url': f"https://nexthire-backend.vercel.app/payment/payment-failed/{user_id}/",
            'cancel_url': f"https://nexthire-backend.vercel.app/payment/payment-failed/{user_id}/",
            'emi_option': 0,
            'cus_name': data.name,
            'cus_email': data.email,
            'cus_phone': "01700000000",
            'cus_add1': data.address,
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "",
            'num_of_item': 1,
            'product_name': "Test",
            'product_category': "Test Category",
            'product_profile': "general",
        }

        response = sslcz.createSession(post_body)
        return Response({'payment_url': response['GatewayPageURL']})


class PaymentSuccessView(APIView):
    def post(self, request, user_id, *args, **kwargs):  
        try:
            payment_data = request.data
            tran_id = payment_data.get('tran_id')
            checkout = Checkout.objects.filter(tran_id=tran_id, Order=False).first()
            
            applied = AppliedJob.objects.filter(id=checkout.job.id).first()
            if applied:
                applied.submit_status = "Approved"
                applied.save()
                print(checkout.job.id)
            
            if checkout:
                checkout.Order = True
                checkout.status = "COMPLETE"
                checkout.save()

                receiver_profile = Profile.objects.filter(user_id=checkout.receiver).first()
                if receiver_profile:
                    receiver_profile.balance += checkout.total_amount
                    receiver_profile.save()
                   
                return HttpResponseRedirect('https://nexthire-frontend.vercel.app/choisen_candidate')

            return Response({'error': 'Transaction not found or invalid.'})

        except Exception:
            return Response({'error': "Something went wrong"})




class PaymentFailedView(APIView):
    def post(self, request, user_id, *args, **kwargs):
        try:
            payment_data = request.data
            tran_id = payment_data.get('tran_id')
            checkout = Checkout.objects.filter(tran_id=tran_id, Order=False).first()

            if checkout:
                checkout.Order = True
                checkout.status = "FAILED"
                checkout.save()
            
            return HttpResponseRedirect('https://nexthire-frontend.vercel.app/choisen_candidate')
        
        except Exception:
            return Response({'error': "Something went wrong"})


def status(request, user_id):
    try:
        checkouts = Checkout.objects.filter(sender=user_id).only("id", "Order")
        
        for checkout in checkouts:
            if checkout.Order == False:
                return JsonResponse({'status': "YES", 'id': checkout.id})
            
        return JsonResponse({'status': "NO"})
    except User.DoesNotExist:
        return JsonResponse({"error": "Not found user"})
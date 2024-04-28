# byimaan

import stripe
from typing import Any
from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

# Create your views here.
class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context
    


def charge(request):
    if request.method == 'POST':

        print(" ---- Charge ---- ")
        print(request.POST)
        print(' ---- End Charge ---- ')

        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )

        return render(request, 'orders/charge.html')
    
    return HttpResponse("Not Authorized! need payment first")
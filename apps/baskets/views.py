from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.baskets.models import Basket
from apps.baskets.utils import product_can_sell
from apps.products.models import Product


@api_view(['POST'])
def add_product_to_basket(request):
    try:
        user_account = request.user.account
        data = request.data
        product_id = data['product_id']

        if product_can_sell is not True:
            raise Product.DoesNotExist

        Basket.objects.create(
            account=user_account,
            product_id=product_id
        )
    except KeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'product_id is missing from request.data'})

    except Product.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'product is not avaiable for sale'})


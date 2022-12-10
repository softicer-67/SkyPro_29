# -*- coding: utf8 -*-

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ads.permissions import SelectUpdatePermission
from ads.serializers import *
from rest_framework.viewsets import ModelViewSet
from ads.models import Ad


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# class Logout(APIView):
#     def post(self, request):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):

        ad_cat = request.GET.get('cat')
        if ad_cat:
            self.queryset = self.queryset.filter(category__id__in=ad_cat)

        ad_name = request.GET.get('text')
        if ad_name:
            self.queryset = self.queryset.filter(name__icontains=ad_name)

        ad_city = request.GET.get('location')
        if ad_city:
            self.queryset = self.queryset.filter(author__location__name__icontains=ad_city)

        price_from = request.GET.get('price_from', 0)
        price_to = request.GET.get('price_to', 100000)
        if price_from or price_to:
            self.queryset = self.queryset.filter(price__range=[price_from, price_to])

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serial = self.get_serializer(self.queryset, many=True)
        return Response(serial.data)


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated]

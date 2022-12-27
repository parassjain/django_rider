from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Requester, Riders,Category
from rest_framework.response import Response
from rest_framework import mixins, status
from rest_framework import permissions, viewsets
import json
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

class RequesterView(viewsets.ViewSet):

    def retrieve(self, request, *args, **kwargs):
        print(request.method)
        all_req = [x.seralise() for x in Requester.objects.all()]
        queryset=Requester.objects.all()
        try:
            paginator = Paginator(queryset, 2)
            images = paginator.page(1)
        except InvalidPage:
            paginator = Paginator(queryset, max(2, queryset.count()))
            images = paginator.page(1)


        res = dict()
        res["data"] = [x.seralise() for x in images]
        res["count"] = paginator.count
        res["num_pages"] = paginator.num_pages
        res["current_page_number"] = images.number
        return Response(res,status=status.HTTP_200_OK)
        return Response({"all_requests": all_req},status=status.HTTP_200_OK)
        
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        new_request = Requester()
        try:
            new_request.from_location = data["from_location"]
            new_request.to_location = data["to_location"]
            new_request.flexible_timing = data["flexible_timing"]
            new_request.travel_datetime = data["travel_datetime"]
            new_request.asset_type = data["asset_type"]
            new_request.asset_sentivity = data["asset_sentivity"]
            new_request.delivery_info = data["delivery_info"]
            new_request.asset_sentivity = data["asset_sentivity"]
            new_request.save()
            
            return Response({"message": "success", },status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)},status=status.HTTP_400_BAD_REQUEST)
    
    def matching_riders(self, request, *args, **kwargs):
        my_requests = Requester.objects.filter(from_location__in=Riders.objects.all().values('from_location'))
        # all_riders = Riders.objects.all()
        # matched_req = []

        matched_req = [x.seralise() for x in my_requests]
        return Response({"matched_req": matched_req},status=status.HTTP_200_OK)
    
    def assign_rider(self, request, *args, **kwargs):
        data = request.data.copy()
        requester=Requester.objects.get(id=data["requester_request_id"])
        assinged_rider=Riders.objects.get(id=data["rider_id"])
        requester.assigned_rider=assinged_rider
        requester.save()
    
        return Response({"message": "success", },status=status.HTTP_202_ACCEPTED)

    

class RiderView(viewsets.ViewSet):
    # serializer_class = RequesterSerializer

    def retrieve(self, request, *args, **kwargs):
        print(request.method)
        all_riders = [x.seralise() for x in Riders.objects.all()]
        return Response({"all_riders": all_riders},status=status.HTTP_200_OK)
        
    
    def create(self, request, *args, **kwargs):
        print(request.method)
        data = request.data.copy()
        new_request = Riders()
        try:
            new_request.rider_name = data.get("rider_name",None)
            new_request.rider_phone = data.get("rider_phone",None)
            new_request.from_location = data["from_location"]
            new_request.to_location = data["to_location"]
            new_request.travel_medium = data["travel_medium"]
            new_request.travel_datetime = data["travel_datetime"]
            new_request.flexible_timing = data["flexible_timing"]
            new_request.no_of_assets = data["no_of_assets"]
            new_request.save()
            
            return Response({"message": "success", },status=status.HTTP_201_CREATED,)
        except Exception as e:
            return Response({"message": str(e)},status=status.HTTP_400_BAD_REQUEST,)
   


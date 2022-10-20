import datetime
from email.policy import default

from django.db import models
from django.utils import timezone

class Riders(models.Model):
    rider_name = models.CharField(max_length=200, null=True)
    rider_phone = models.CharField(max_length=200, null=True)
    from_location = models.CharField(max_length=200)
    to_location = models.CharField(max_length=200)
    travel_medium = models.IntegerField(default=0)
    travel_datetime = models.DateTimeField('travel date time')
    flexible_timing = models.BooleanField(default=False)
    no_of_assets = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def seralise(self):
        seralised_data = {
            "rider_name": self.rider_name,
            "rider_phone": self.rider_phone,
            "from_location": self.from_location,
            "to_location": self.to_location,
            "travel_medium": Category.TRAVEL_MEDIUM[self.travel_medium],
            "travel_datetime": self.travel_datetime,
            "flexible_timing": self.flexible_timing,
            "no_of_assets": self.no_of_assets,
            "created_at": self.created_at,
        }
        return seralised_data


class Requester(models.Model):
    requester_name = models.CharField(max_length=200)
    from_location = models.CharField(max_length=200)
    to_location = models.CharField(max_length=200)
    flexible_timing = models.BooleanField(default=False)
    travel_datetime = models.DateTimeField('travel date time')
    no_of_assets = models.IntegerField(default=0)
    asset_type = models.IntegerField(default=0)
    asset_sentivity = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    delivery_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def seralise(self):
        seralised_data = {
            "requester_name": self.requester_name,
            "from_location": self.from_location,
            "to_location": self.to_location,
            "flexible_timing": self.flexible_timing,
            "travel_datetime": self.travel_datetime,
            "no_of_assets": self.no_of_assets,
            "asset_type": Category.ASSET_TYPE[self.asset_type],
            "asset_sentivity": Category.ASSET_SENSTIVITY[self.asset_sentivity],
            "delivery_info": self.delivery_info,
            "status": Category.STATUS[self.status],
            
        }
        return seralised_data

class Category:
    TRAVEL_MEDIUM = {
        0: 'BUS',
        1: 'CAR',
        2: 'TRAIN',
    }

    ASSET_TYPE = {
        0: 'LAPTOP',
        1: 'TRAVELBAG',
        2: 'PACKAGE'
    }

    STATUS={
        0: 'PENDING',
        1: 'Expired',
    }

    ASSET_SENSTIVITY={
        0: 'HIGHLY_SENSITIVE',
        1: 'SENSITIVE',
        2: 'NORMAL',
    }


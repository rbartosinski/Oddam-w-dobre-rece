from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


TYPE_OF_THING = (
    (1, "clothes-to-use"),
    (2, "clothes-useless"),
    (3, "toys"),
    (4, "books"),
    (5, "other"),
)

LOCALIZATION = (
    (1, "Warszawa"),
    (2, "Wrocław"),
    (3, "Poznań"),
    (4, "Gdańsk"),
)

HELPS_FOR = (
    (1, "children"),
    (2, "mothers"),
    (3, "homeless"),
    (4, "disabled"),
    (5, "old"),
)


class Organization(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    localization = ArrayField(
        models.CharField(max_length=16, choices=LOCALIZATION),
    )
    help_for = ArrayField(
        models.CharField(max_length=16, choices=HELPS_FOR),
    )
    address_street = models.CharField(max_length=256)
    address_city = models.CharField(max_length=256)
    address_post_code = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16)


class NewPickUp(models.Model):
    who_add = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    type_of_thing = ArrayField(
        models.CharField(max_length=16, choices=TYPE_OF_THING),
    )
    quantity = models.IntegerField()
    localization = models.IntegerField(choices=LOCALIZATION)
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    pick_up_phone_number = models.CharField(max_length=16)
    pick_up_date = models.DateField()
    pick_up_hour = models.TimeField()
    pick_up_address_street = models.CharField(max_length=256)
    pick_up_address_city = models.CharField(max_length=256)
    pick_up_address_post_code = models.CharField(max_length=256)
    notes = models.CharField(max_length=256, null=True)

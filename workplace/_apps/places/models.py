from django.db import models


class PlaceType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )


class Place(models.Model):
    type = models.ForeignField(
        PlaceType,
        related_name='places',
    )
    name = models.CharField(
        max_length=100,
    )


class PlaceAltName(models.Model):
    place = models.ForeignField(
        Place,
        related_name='place_alt_names'
    )
    alt_name = models.CharField(
        max_length=100,
    )

    class Meta:
        unique_together = (('place', 'alt_name',),)


# Place Type: Country -----------------------------------

class Country(models.Model):
    place = models.OneToOneField(
        Place,
        related_name='country',
    )

    tld = models.CharField(
        max_length=100,
    )
    cca2 = models.CharField(
        max_length=2,
    )
    cca3 = models.CharField(
        max_length=3,
    )
    ccn3 = models.CharField(
        max_length=3,
    )
    world_region = models.ForeignField(
        Place,
        related_name='countries_world_region',
    )
    world_sub_region = models.ForeignField(
        Place,
        related_name='countries_world_sub_region'
    )


class CountryCallingCode(models.Model):
    country = models.ForeignField(
        Country,
        related_name='country_calling_codes'
    )
    calling_code = models.CharField(
        max_length=100,
    )


class CountryCurrency(models.Model):
    country = models.ForeignField(
        Country,
        related_name='country_currencies'
    )
    currency = models.CharField(
        max_length=100,
    )
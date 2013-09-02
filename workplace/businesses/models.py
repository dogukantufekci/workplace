from django.db import models

from workplace.constants import MaxLengths


class Business(models.Model):
    SOLE_TRADER = 1
    ORGANIZATION = 2
    TYPE_CHOICES = (
        (SOLE_TRADER, 'Sole Trader'),
        (ORGANIZATION, 'Organization'),
    )

    workplace = models.ForeignKey('workplaces.Workplace', related_name='businesses')
    workplace_business = models.NullBooleanField()

    name = models.CharField(max_length=MaxLengths.BUSINESS_NAME)

    is_deleted = models.NullBooleanField()


class SoleTrader(models.Model):
    business = models.OneToOneKey(Business, related_name='sole_trader')
    person = models.OneToOneKey(Person, related_name='sole_trader')


class Organization(models.Model):
    registered_in = models.ForeignKey(
        Country,
        related_name='companies',
    )
    registration_number = models.CharField(
        max_length=40,
    )
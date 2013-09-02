from django.db import models

from countries.models import Country
from people.models import Person


# Models -----------------------------------------


class Company(models.Model):
    SOLE_TRADER = 1
    CORPORATION = 2
    TYPE_CHOICES = (
        (SOLE_TRADER, 'Sole Trader'),
        (CORPORATION, 'Corporation'),
    )
    name = models.CharField(
        max_length=100,
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICES,
    )


class SoleTrader(models.Model):
    person = models.OneToOneField(
        Person,
        related_name='sole_trader',
    )


class Corporation(models.Model):
    registered_in = models.ForeignKey(
        Country,
        related_name='companies',
    )
    registration_number = models.CharField(
        max_length=40,
    )

    class Meta:
        unique_together = (('registered_in', 'registration_number'),)


class CompanyEmail(models.Model):
    company = models.ForeignKey(
        Company,
        related_name='company_emails',
    )
    email = models.EmailField(
        max_length=254,
    )

    class Meta:
        unique_together = (('company', 'email',),)


class CompanyPhoneNumber(models.Model):
    company = models.ForeignKey(
        Company,
        related_name='company_phone_numbers',
    )
    phone_number = models.ForeignKey(
        PhoneNumber,
        related_name='company_phone_numbers',
    )


# Custom Models -----------------------------------------


class CustomCompany(models.Model):
    name = models.CharField(
        max_length=100,
    )
    type = models.PositiveSmallIntegerField(
        choices=Company.TYPE_CHOICES,
    )


class CustomSoleTrader(models.Model):
    person = models.OneToOneField(
        CustomPerson,
        related_name='custom_sole_trader',
    )


class CustomCorporation(models.Model):
    registered_in = models.ForeignKey(
        Country,
        related_name='custom_corporations',
    )
    registration_number = models.CharField(
        max_length=40,
    )

    class Meta:
        unique_together = (('registered_in', 'registration_number'),)


class CustomCompanyEmail(models.Model):
    custom_company = models.ForeignKey(
        CustomCompany,
        related_name='custom_company_emails',
    )
    email = models.EmailField(
        max_length=254,
    )

    class Meta:
        unique_together = (('company', 'email',),)


class CustomCompanyPhoneNumber(models.Model):
    company = models.ForeignKey(
        Company,
        related_name='company_phone_numbers',
    )
    phone_number = models.ForeignKey(
        PhoneNumber,
        related_name='company_phone_numbers',
    )
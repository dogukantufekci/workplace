from django.db import models


class Identification(models.Model):
    number = models.CharField(
        max_length=32,
    )
    issue_date = models.DateField(
        blank=True,
        null=True,
    )
    expiry_date = models.DateField(
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class NationalIdentityCard(Identification):
    person = models.ForeignKey(
        Person,
        related_name='national_identity_cards',
    )
    issued_by = models.ForeignKey(
        Country,
        related_name='national_identity_cards'
    )


class Passport(Identification):
    person = models.ForeignKey(
        Person,
        related_name='passports',
    )
    issued_by = models.ForeignKey(
        Country,
        related_name='passports'
    )


class DriversLicense(Identification):
    person = models.ForeignKey(
        Person,
        related_name='divers_licenses',
    )
    issued_by = models.ForeignKey(
        Country,
        related_name='divers_licenses'
    )
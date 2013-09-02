from django.db import models

# Create your models here.


class Role(models.Model):
    title = models.CharField(
        max_length=40,
        unique=True,
    )


class CompanyRolePerson(models.Model):
    company = models.ForeignKey(
        Company,
        related_name='company_role_persons',
    )
    role = models.ForeignKey(
        Role,
        related_name='company_role_persons',
    )
    person = models.ForeignKey(
        Person,
        related_name='company_role_persons',
    )
    date_from = models.DateField(
        blank=True,
        null=True,
    )
    date_to = models.DateField(
        blank=True,
        null=True,
    )
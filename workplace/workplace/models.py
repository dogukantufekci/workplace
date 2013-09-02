from django.conf import settings
from django.db import models

from workplace.constants import MaxLengths


class AbstractObject(models.Model):
    is_deleted = models.NullBooleanField()

    class Meta:
        abstract = True


class AbstractObjectAttribute(models.Model):
    is_deleted = models.NullBooleanField()

    class Meta:
        abstract = True
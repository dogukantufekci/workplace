from django.db import models


class ActivityType(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    name = models.CharField(
        max_length=100,
    )


class Activity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    created_via = models.ForeignKey(
        App,
        related_name='activities_created_via'
    )

    type = models.ForeignKey(
        ActivityType,
        related_name='activities',
    )
    date = models.DateField(
        blank=True,
        null=True,
    )
    time = models.TimeField(
        blank=True,
        null=True,
    )
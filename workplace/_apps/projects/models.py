from django.db import models


class ProjectType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )


class Project(models.Model):
    type = models.ForeignField(
        PlaceType,
        related_name='projects',
    )
    name = models.CharField(
        max_length=100,
    )
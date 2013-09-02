from django.conf import settings
from django.db import models

from workplace.constants import MaxLengths


class Person(models.Model):
    workplace = models.ForeignKey('workplaces.Workplace', related_name='people')

    first_name = models.CharField(max_length=MaxLengths.FIRST_NAME)
    last_name = models.CharField(max_length=MaxLengths.LAST_NAME)
    
    is_deleted = models.NullBooleanField()

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class PersonSummary(models.Model):
    person = models.OneToOneField('people.Person', related_name='summary')

    summary = models.TextField()

    is_deleted = models.NullBooleanField()


class PersonEmail(models.Model):
    PERSONAL = 1
    PROFESSIONAL = 2
    OTHER = 3

    TYPE_CHOICES = (
        (PERSONAL, 'Personal'),
        (PROFESSIONAL, 'Professional'),
        (OTHER, 'Other'),
    )

    person = models.ForeignKey('people.Person', related_name='emails')

    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    email = models.EmailField(max_length=MaxLengths.EMAIL)

    is_deleted = models.NullBooleanField()

    class Meta:
        unique_together = (('person', 'email',),)


class PersonPhoneNumber(models.Model):
    HOME = 1
    WORK = 2
    PERSONAL_MOBILE = 3
    PROFESSIONAL_MOBILE = 4
    OTHER = 5

    TYPE_CHOICES = (
        (HOME, 'Home'),
        (WORK, 'Work'),
        (PERSONAL_MOBILE, 'Personal Mobile'),
        (PROFESSIONAL_MOBILE, 'Professional Mobile'),
        (OTHER, 'Other'),
    )

    person = models.ForeignKey('people.Person', related_name='phone_numbers')

    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    phone_number = models.CharField(max_length=MaxLengths.PHONE_NUMBER)

    is_deleted = models.NullBooleanField()

    class Meta:
        unique_together = (('person', 'phone_number',),)


class PersonWebsite(models.Model):
    BLOG = 1
    PERSONAL = 2
    PORTFOLIO = 3
    OTHER = 4

    TYPE_CHOICES = (
        (BLOG, 'Blog'),
        (PERSONAL, 'Personal'),
        (PORTFOLIO, 'Portfolio'),
        (OTHER, 'Other'),
    )

    person = models.ForeignKey('people.Person', related_name='websites')

    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    url = models.CharField(max_length=MaxLengths.URL)

    is_deleted = models.NullBooleanField()

    class Meta:
        unique_together = (('person', 'url',),)


class PersonSocialMediaProfile(models.Model):
    FACEBOOK = 1
    GOOGLE_PLUS = 2
    LINKEDIN = 3
    TWITTER = 4
    OTHER = 5

    TYPE_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (GOOGLE_PLUS, 'Google Plus'),
        (LINKEDIN, 'LinkedIn'),
        (TWITTER, 'Twitter'),
        (OTHER, 'Other'),
    )

    person = models.ForeignKey('people.Person', related_name='social_media_profiles')

    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
    url = models.CharField(max_length=MaxLengths.URL)

    is_deleted = models.NullBooleanField()

    class Meta:
        unique_together = (('person', 'url',),)
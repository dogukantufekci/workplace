from rest_framework import serializers

from .models import (
    Person,
    PersonSummary,
    PersonEmail, 
    PersonPhoneNumber, 
    PersonWebsite, 
    PersonSocialMediaProfile,
)


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = Person


class PersonSummarySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonSummary


class PersonEmailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonEmail


class PersonPhoneNumberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonPhoneNumber


class PersonWebsiteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonWebsite


class PersonSocialMediaProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonSocialMediaProfile
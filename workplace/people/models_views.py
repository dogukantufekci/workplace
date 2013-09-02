from rest_framework import generics

from .models import (
    Person,
    PersonSummary,
    PersonEmail,
    PersonPhoneNumber,
    PersonWebsite,
    PersonSocialMediaProfile,
)
from .models_serializers import (
    PersonSerializer,
    PersonSummarySerializer,
    PersonEmailSerializer,
    PersonPhoneNumberSerializer,
    PersonWebsiteSerializer,
    PersonSocialMediaProfileSerializer,
)


# Person ##########################################################


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_fields = ('first_name', 'last_name',)


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


# PersonSummary ##########################################################


class PersonSummaryList(generics.ListCreateAPIView):
    queryset = PersonSummary.objects.all()
    serializer_class = PersonSummarySerializer
    filter_fields = ('person',)


class PersonSummaryDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PersonSummarySerializer
    queryset = PersonSummary.objects.all()


# PersonEmail ##########################################################


class PersonEmailList(generics.ListCreateAPIView):
    queryset = PersonEmail.objects.all()
    serializer_class = PersonEmailSerializer
    filter_fields = ('person', 'email',)


class PersonEmailDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PersonEmailSerializer
    queryset = PersonEmail.objects.all()


# PersonPhoneNumber ##########################################################


class PersonPhoneNumberList(generics.ListCreateAPIView):
    queryset = PersonPhoneNumber.objects.all()
    serializer_class = PersonPhoneNumberSerializer
    filter_fields = ('person', 'type', 'phone_number',)


class PersonPhoneNumberDetail(generics.RetrieveDestroyAPIView):
    queryset = PersonPhoneNumber.objects.all()
    serializer_class = PersonPhoneNumberSerializer


# PersonWebsite ##########################################################


class PersonWebsiteList(generics.ListCreateAPIView):
    queryset = PersonWebsite.objects.all()
    serializer_class = PersonWebsiteSerializer
    filter_fields = ('person', 'type', 'url',)


class PersonWebsiteDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PersonWebsiteSerializer
    queryset = PersonWebsite.objects.all()


# PersonSocialMediaProfile ##########################################################


class PersonSocialMediaProfileList(generics.ListCreateAPIView):
    queryset = PersonSocialMediaProfile.objects.all()
    serializer_class = PersonSocialMediaProfileSerializer
    filter_fields = ('person', 'type', 'url',)


class PersonSocialMediaProfileDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PersonSocialMediaProfileSerializer
    queryset = PersonSocialMediaProfile.objects.all()
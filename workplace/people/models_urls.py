from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',

    url(
        r'^/$', 
        views.people, 
        name='people'
    ),


# Person ##########################################################


    url(
        r'^/person/$', 
        views.PersonList.as_view(), 
        name='person-list'
    ),
    url(
        r'^/person/(?P<pk>[0-9]+)/$', 
        views.PersonDetail.as_view(), 
        name='person-detail'
    ),


# PersonSummary ##########################################################


    url(
        r'^/personsummary/$', 
        views.PersonSummaryList.as_view(), 
        name='personsummary-list'
    ),
    url(
        r'^/personsummary/(?P<pk>[0-9]+)/$', 
        views.PersonSummaryDetail.as_view(), 
        name='personsummary-detail'
    ),
    

# PersonEmail ##########################################################


    url(
        r'^/personemail/$', 
        views.PersonEmailList.as_view(), 
        name='personemail-list'
    ),
    url(
        r'^/personemail/(?P<pk>[0-9]+)/$', 
        views.PersonEmailDetail.as_view(), 
        name='personemail-detail'
    ),


# PersonPhoneNumber ##########################################################


    url(
        r'^/personphonenumber/$', 
        views.PersonPhoneNumberList.as_view(), 
        name='personphonenumber-list'
    ),
    url(
        r'^/personphonenumber/(?P<pk>[0-9]+)/$', 
        views.PersonPhoneNumberDetail.as_view(), 
        name='personphonenumber-detail'
    ),


# PersonWebsite ##########################################################


    url(
        r'^/personwebsite/$', 
        views.PersonWebsiteList.as_view(), 
        name='personwebsite-list'
    ),
    url(
        r'^/personwebsite/(?P<pk>[0-9]+)/$', 
        views.PersonWebsiteDetail.as_view(), 
        name='personwebsite-detail'
    ),


# PersonSocialMediaProfile ##########################################################


    url(
        r'^/personsocialmediaprofile/$', 
        views.PersonSocialMediaProfileList.as_view(), 
        name='personsocialmediaprofile-list'
    ),
    url(
        r'^/personsocialmediaprofile/(?P<pk>[0-9]+)/$', 
        views.PersonSocialMediaProfileDetail.as_view(), 
        name='personsocialmediaprofile-detail'
    ),

)

urlpatterns = format_suffix_patterns(urlpatterns)
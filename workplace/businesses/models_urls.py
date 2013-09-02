from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',

    url(
        r'^/$', 
        views.businesses, 
        name='businesses'
    ),


# Business ##########################################################


    url(
        r'^/business/$', 
        views.BusinessList.as_view(), 
        name='business-list'
    ),
    url(
        r'^/business/(?P<pk>[0-9]+)/$', 
        views.BusinessDetail.as_view(), 
        name='business-detail'
    ),

)

urlpatterns = format_suffix_patterns(urlpatterns)
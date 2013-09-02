from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(
        r'^create_workplace/$', 
        'auth.views.create_workplace', 
        name='create_workplace'
    ),
    url(
        r'^create_workplace/(?P<identifier>\w+)/$', 
        'auth.views.create_workplace_identifier', 
        name='create_workplace_identifier'
    ),
    url(
        r'^login/$', 
        'auth.views.login', 
        name='login'
    ),
    url(
        r'^logout/$', 
        'auth.views.logout', 
        name='logout'
    ),
)
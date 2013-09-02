from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


urlpatterns = patterns('',

    url(r'^$', 'workplace.views.workplace', name='workplace'),

    url(r'^auth/', include('auth.urls', namespace='auth')),

    # module models api
    url(r'^models/$', 'workplace.views.models', name='models'),
    url(r'^models/businesses/', include('businesses.urls', namespace='models_businesses')),
    url(r'^models/people/', include('people.urls', namespace='models_people')),
    url(r'^models/users/', include('users.urls', namespace='models_users')),
    url(r'^models/workplaces/', include('workplaces.urls', namespace='models_workplaces')),

)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
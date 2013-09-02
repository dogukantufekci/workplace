from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def people(request, format=None):
    return Response({
        'person': reverse('people:person-list', request=request, format=format),
        'personemail': reverse('people:personemail-list', request=request, format=format),
        'personsummary': reverse('people:personsummary-list', request=request, format=format),
        'personemail': reverse('people:personemail-list', request=request, format=format),
        'personphonenumber': reverse('people:personphonenumber-list', request=request, format=format),
        'personwebsite': reverse('people:personwebsite-list', request=request, format=format),        
        'personsocialmediaprofile': reverse('people:personsocialmediaprofile-list', request=request, format=format),        
    })
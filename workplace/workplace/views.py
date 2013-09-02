from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def workplace(request, format=None):
    return Response({
        'users': reverse('users:users', request=request, format=format),
        'people': reverse('people:people', request=request, format=format),
    })
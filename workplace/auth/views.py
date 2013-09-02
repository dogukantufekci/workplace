from django.contrib.auth import (
    authenticate,
    login as django_login, 
    logout as django_logout,
)
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import (
    get_object_or_404,
    render,
)

from workplace.decorators import anonymous_only

from .forms import (
    CreateWorkplaceForm,
    LoginForm,
    RegisterForm,
)


def welcome(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('workplace'))
    return render(request, 'welcome.html')


@anonymous_only
def create_workplace(request):
    if request.method == 'POST':
        form = CreateWorkplaceForm(request.POST)
        if form.is_valid():
            form.save()
            identifier = form.cleaned_data['identifier']
            redirect_url = reverse(
                'auth:create_workplace_identifier', 
                kwargs={'identifier': identifier,},
            ))
            return HttpResponseRedirect(redirect_url)
    else:
        form = CreateWorkplaceForm()
    return render(request, 'auth/create_workplace.html', {
        'form': form,
    })


@anonymous_only
def create_workplace_identifier(request, identifier):
    workplace = get_object_or_404(Workplace, identifier=identifier)
    return render(request, 'auth/create_workplace_identifier.html', {
        'workplace': workplace,
    })


@anonymous_only
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Register
            form.save()
            # Authenticate
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if not user:
                return HttpResponseRedirect(reverse('auth:login'))
            # Login
            django_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {
        'form': form,
    })


@anonymous_only
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            django_login(request, user)
            return HttpResponseRedirect(next or '/')
    else:
        form = LoginForm(initial={
            'next': request.GET.get('next', '')
        })
    return render(request, 'auth/login.html', {
        'form': form,
    })


def logout(request):
    next = request.GET.get('next')
    django_logout(request)
    return HttpResponseRedirect(next or '/')
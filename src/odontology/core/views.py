from django.shortcuts import  render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, Context, loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def login_user(request):
    if request.method == 'GET':
        return render_to_response(
            'core/login.html',
            RequestContext(request)
        )
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('core:home')
            else:
                #return to a disable account
                pass
        else:
            return render_to_response(
                'core/login.html',
                {
                    'login_error': True,
                    'username': username,
                    'password': password
                },
                RequestContext(request)
            )


@login_required
def home(request):
    return render_to_response(
        'core/home.html',
        {'template': 'home'},
        RequestContext(request)
    )


@login_required
def logout_user(request):
    logout(request)
    return redirect('core:login')


def error404(request):
     template = loader.get_template('404.html')
     context = Context({'message': 'All: %s' % request,})
     return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)
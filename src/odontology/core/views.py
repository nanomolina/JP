#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import  render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, Context, loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import mercadopago


def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect('core:home')
        else:
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
                try:
                    domain, next_q = request.META.get('HTTP_REFERER').split('?next=')
                    return redirect(next_q)
                except:
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
    from person.models import Patient, Dentist
    from datetime import datetime
    dentist = Dentist.objects.get(user=request.user)
    patients_birthday = dentist.get_patients_birthdays(datetime.now().month)
    return render_to_response(
        'core/home.html',
        {'template': 'home', 'list_patients_birthday': patients_birthday},
        RequestContext(request)
    )


@login_required
def logout_user(request):
    logout(request)
    return redirect('core:login')


@login_required
def version(request):
    return render_to_response(
        'core/version.html',
        {},
        RequestContext(request)
    )


@login_required
def mp(request):
    preference = {
        "items": [
            {
                "title": "Servidor de página dentalsoft.com.ar",
                "quantity": 1,
                "currency_id": "ARS", # Available currencies at: https://api.mercadopago.com/currencies
                "unit_price": 150.0
            }
        ]
    }
    mp = mercadopago.MP("1413986768414297", "NRFtu2EIIUzUOmAz5NJLd0UtORfvy6d5")
    preferenceResult = mp.create_preference(preference)
    url = preferenceResult["response"]["init_point"]
    return render_to_response(
        'core/mp.html',
        {'url': url},
        RequestContext(request)
    )


def error404(request):
     template = loader.get_template('404.html')
     context = Context({'message': 'All: %s' % request,})
     return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)

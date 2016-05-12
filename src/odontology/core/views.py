#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import  render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, Context, loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import mercadopago
from person.models import Dentist


def principal(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect('core:home')
        else:
            return redirect('account_login')


@login_required
def home(request):
    from person.models import Patient, Dentist
    from datetime import datetime
    from allauth.socialaccount.models import SocialAccount
    dentist, is_new = Dentist.objects.get_or_create(user=request.user)
    if is_new:
        dentist.save()
    patients_birthday = dentist.get_patients_birthdays(datetime.now().month)
    has_connection = SocialAccount.objects.filter(user=request.user).exists()
    return render_to_response(
        'core/home.html',
        {'template': 'home',
         'list_patients_birthday': patients_birthday,
         'has_connection': has_connection},
        RequestContext(request)
    )


@login_required
def logout_user(request):
    logout(request)
    return redirect('account_login')


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

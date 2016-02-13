from django.shortcuts import render_to_response
from django.template import RequestContext


def list_patients(request):
    return render_to_response(
        'patient/list_patients.html',
        {'template': 'patient'},
        RequestContext(request)
    )

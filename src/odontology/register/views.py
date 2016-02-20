from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from person.models import Patient, Dentist
from person.forms import PatientForm
from register.models import Apross
from register.forms import AprossForm, detailAprossForm
from datetime import date as Date


def new_benefit(request, patient_id):
    dentist = Dentist.objects.get(user=request.user)
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        date = request.POST.get('date', None)
        if date:
            month, year = date.split(' - ')
            date_exists = Apross.objects.filter(
                patient=patient, month=month, year=int(year)
            ).exists()
            benefit_form = AprossForm(request.POST)
            if not date_exists:
                if benefit_form.is_valid():
                    new_benefit = benefit_form.save(commit=False)
                    new_benefit.patient = patient
                    new_benefit.month = month
                    new_benefit.year = int(year)
                    new_benefit.real_date = Date(int(year), int(new_benefit.get_month_display()), 1)
                    new_benefit.save()
                    #return HttpResponseRedirect(reverse('person:patient_profile', kwargs={'id': patient_id}))
                    return JsonResponse({'status': 'OK'})
                else:
                    return JsonResponse({'status': 'ERROR', 'errors': benefit_form.errors})
            else:
                date_error = {'date': [u'Ingrese una fecha valida.']}
                if benefit_form.is_valid():
                    return JsonResponse({'status': 'ERROR', 'errors': date_error})
                else:
                    benefit_form.errors['date'] = [u'Ingrese una fecha valida.']
                    return JsonResponse({'status': 'ERROR', 'errors': benefit_form.errors})

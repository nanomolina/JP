from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import JsonResponse
from django.template import RequestContext
from person.models import Patient, Dentist
from person.forms import PatientForm
from register.models import Apross
from register.forms import AprossForm, detailAprossForm
from datetime import date as Date


def list_patients(request):
    dentist = Dentist.objects.get(user=request.user)
    if request.method == 'GET':
        rec_added = request.GET.get('add', None)
        form = PatientForm()
        patients = Patient.objects.filter(dentist=dentist)
        return render_to_response(
            'person/list_patients.html',
            {
                'template': 'patient',
                'patient_form': form,
                'patients': patients,
                'rec_added': rec_added
            },
            RequestContext(request)
        )
    else:
        form = PatientForm(request.POST)
        if form.is_valid():
            new_patient = form.save(commit=False)
            new_patient.dentist = dentist
            new_patient.save()
            return JsonResponse({'status': 'OK'})
        else:
            return JsonResponse({'status': 'ERROR', 'errors': form.errors})

def patient_profile(request, id):
    dentist = Dentist.objects.get(user=request.user)
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'GET':
        benefits = Apross.objects.filter(patient=patient).order_by('real_date')
        if benefits:
            last_benefit = benefits.last()
        else:
            last_benefit = None
        if patient.social_work == 2:
            benefit_form = AprossForm()
        else: #cambiar
            benefit_form = None
        detail_form = detailAprossForm()
        return render_to_response(
            'person/profile.html',
            {
                'template': 'patient',
                'dentist': dentist,
                'patient': patient,
                'benefits': benefits,
                'last_benefit': last_benefit,
                'benefit_form': benefit_form,
                'detail_form': detail_form,
            },
            RequestContext(request)
        )

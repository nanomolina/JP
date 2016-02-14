from django.shortcuts import render_to_response, redirect
from django.http import JsonResponse
from django.template import RequestContext
from person.models import Patient
from person.forms import PatientForm


def list_patients(request):
    if request.method == 'GET':
        rec_added = request.GET.get('add', None)
        form = PatientForm()
        patients = Patient.objects.all()
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
            form.save()
            return JsonResponse({'status': 'OK'})
        else:
            return JsonResponse({'status': 'ERROR', 'errors': form.errors})

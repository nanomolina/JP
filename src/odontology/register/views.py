from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from person.models import Patient, Dentist
from person.forms import PatientForm
from register.models import Apross, DetailApross, Benefit, DetailBenefit
from register.forms import AprossForm, detailAprossForm, BenefitForm, detailBenefitForm
from datetime import date as Date


def new_benefit(request, patient_id):
    dentist = Dentist.objects.get(user=request.user)
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        date = request.POST.get('date', None)
        if date:
            month, year = date.split(' - ')
            if patient.social_work and patient.social_work.initial == 'APROSS':
                date_exists = Apross.objects.filter(
                    patient=patient, month=month, year=int(year)
                ).exists()
                benefit_form = AprossForm(request.POST)
            else:
                date_exists = Benefit.objects.filter(
                    patient=patient, month=month, year=int(year)
                ).exists()
                benefit_form = BenefitForm(request.POST)
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


def edit_benefit(request, patient_id):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, id=patient_id)
        bf_id = request.POST.get('bf_id', None)
        get = request.POST.get('get')
        if get == '1':
            if patient.social_work and patient.social_work.initial == 'APROSS':
                benefit = Apross.objects.get(id=bf_id)
                bf_edit_form = AprossForm(instance=benefit)
                template = 'register/_edit_apross.html'
            else: #cambiar
                benefit = Benefit.objects.get(id=bf_id)
                bf_edit_form = BenefitForm(instance=benefit)
                template = 'register/_edit_benefit.html'
            return render_to_response(
                template,
                {
                    'bf': benefit,
                    'bf_edit_form': bf_edit_form,
                    'patient': patient
                },
                RequestContext(request)
            )
        else:
            date = request.POST.get('date', None)
            if date:
                month, year = date.split(' - ')
                if patient.social_work and patient.social_work.initial == 'APROSS':
                    benefit = Apross.objects.get(id=bf_id)
                    benefit_form = AprossForm(request.POST, instance=benefit)
                    date_exists = Apross.objects.filter(
                        patient=patient, month=month, year=int(year)
                    ).exclude(id=benefit.id).exists()
                else:
                    benefit = Benefit.objects.get(id=bf_id)
                    benefit_form = BenefitForm(request.POST, instance=benefit)
                    date_exists = Benefit.objects.filter(
                        patient=patient, month=month, year=int(year)
                    ).exclude(id=benefit.id).exists()
                if not date_exists:
                    if benefit_form.is_valid():
                        benefit = benefit_form.save(commit=False)
                        benefit.patient = patient
                        benefit.month = month
                        benefit.year = int(year)
                        benefit.real_date = Date(int(year), int(benefit.get_month_display()), 1)
                        benefit.save()
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


def edit_benefit_detail(request, patient_id, detail_id):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, id=patient_id)
        if patient.social_work and patient.social_work.initial == 'APROSS':
            detail = DetailApross.objects.get(id=detail_id)
            detail_form = detailAprossForm(request.POST, instance=detail)
            template = 'register/detail_apross.html'
        else:
            detail = DetailBenefit.objects.get(id=detail_id)
            detail_form = detailBenefitForm(request.POST, instance=detail)
            template = 'register/detail_benefit.html'

        if detail_form.is_valid():
            detail = detail_form.save()
            if patient.social_work and patient.social_work.initial == 'APROSS':
                detail_form = detailAprossForm(instance=detail)
            else:
                detail_form = detailBenefitForm(instance=detail)
            return render_to_response(
                template,
                {
                    'counter': request.POST.get('counter'),
                    'detail': detail,
                    'bf': detail.benefit,
                    'patient': patient
                },
                RequestContext(request)
            )
        else:
            print detail_form.errors
            return JsonResponse({'status': 'ERROR', 'errors': detail_form.errors})


def benefit_to_pdf(request, patient_id, bf_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if patient.social_work and patient.social_work.initial == 'APROSS':
        benefit = get_object_or_404(Apross, id=bf_id)
        template = 'register/pdf_apross.html'
    else:
        benefit = get_object_or_404(Benefit, id=bf_id)
        template = 'register/pdf_benefit.html'
    return render_to_response(
        template,
        {
            'patient': patient,
            'benefit': benefit,
        },
        RequestContext(request)
    )

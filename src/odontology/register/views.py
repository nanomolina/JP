from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from person.models import Patient, Dentist, Sector, Tooth
from person.forms import PatientForm, OdontogramForm
from register.models import Apross, DetailApross, Benefit, DetailBenefit, Radiography, Record
from register.forms import AprossForm, detailAprossForm, BenefitForm, detailBenefitForm, RadiographyForm, RecordForm
from datetime import date as Date
from django.contrib.auth.decorators import login_required


@login_required
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
                    return JsonResponse({'status': 'OK'})
                else:
                    return JsonResponse({'status': 'ERROR', 'errors': benefit_form.errors})
            else:
                benefit_form.errors['date'] = [u'Ingrese una fecha valida.']
                return JsonResponse({'status': 'ERROR', 'errors': benefit_form.errors})
        else:
            date_error = {'date': [u'Ingrese una fecha valida.']}
            if patient.social_work and patient.social_work.initial == 'APROSS':
                benefit_form = AprossForm(request.POST)
            else:
                benefit_form = BenefitForm(request.POST)
            if benefit_form.is_valid():
                return JsonResponse({'status': 'ERROR', 'errors': date_error})
            else:
                benefit_form.errors['date'] = [u'Ingrese una fecha valida.']
                return JsonResponse({'status': 'ERROR', 'errors': benefit_form.errors})


@login_required
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
                    benefit_form.errors['date'] = [u'Ingrese una fecha valida.']
                    return JsonResponse({'status': 'ERROR', 'errors': benefit_form.errors})
            else:
                date_error = {'date': [u'Ingrese una fecha valida.']}
                if patient.social_work and patient.social_work.initial == 'APROSS':
                    benefit_form = AprossForm(request.POST)
                else:
                    benefit_form = BenefitForm(request.POST)
                if benefit_form.is_valid():
                    return JsonResponse({'status': 'ERROR', 'errors': date_error})
                else:
                    benefit_form.errors['date'] = [u'Ingrese una fecha valida.']
                    return JsonResponse({'status': 'ERROR', 'errors': benefit_form.errors})


@login_required
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
            return JsonResponse({'status': 'ERROR', 'errors': detail_form.errors})


@login_required
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


@login_required
def edit_odontogram(request, patient_id):
    import json
    if request.method == 'POST':
        patient = get_object_or_404(Patient, id=patient_id)
        teeth_works = request.POST.get('teeth_works', None)
        if teeth_works is not None:
            teeth_works = json.loads(teeth_works)
        for tw in teeth_works:
            if tw['type'] == '':
                tooth = Tooth.objects.get(id=tw['id'])
                for sector in tooth.get_sectors():
                    sector.color = None
                    sector.stroke_blue = False
                    sector.save()
                tooth.color = None
                tooth.work_type = None
                tooth.save()
            if tw['type'] == 1:
                tooth = Tooth.objects.get(id=tw['id'])
                if tw['color'] == 'red':
                    tooth.color = 1
                elif tw['color'] == 'blue':
                    tooth.color = 2
                else:
                    tooth.color = None
                tooth.work_type = 1
                tooth.save()
            elif tw['type'] == 2:
                tooth = Tooth.objects.get(id=tw['id'])
                if tw['color'] == 'red':
                    tooth.color = 1
                elif tw['color'] == 'blue':
                    tooth.color = 2
                else:
                    tooth.color = None
                tooth.work_type = 2
                tooth.save()
            elif tw['type'] == 3:
                sector = Sector.objects.get(id=tw['id'])
                if tw['color'] == 'red':
                    sector.color = 1
                elif tw['color'] == 'blue':
                    sector.color = 2
                else:
                    sector.color = None
                sector.save()
                sector.tooth.work_type = 3
                sector.tooth.save()
            elif tw['type'] == 4:
                sector = Sector.objects.get(id=tw['id'])
                if tw['color'] == 'red':
                    sector.color = 1
                elif tw['color'] == 'blue':
                    sector.color = 2
                else:
                    sector.color = None
                sector.stroke_blue = True
                sector.save()
                sector.tooth.work_type = 4
                sector.tooth.save()
            elif tw['type'] == 5:
                sector = Sector.objects.get(id=tw['id'])
                if tw['color'] == 'red':
                    sector.color = 1
                elif tw['color'] == 'blue':
                    sector.color = 2
                else:
                    sector.color = None
                sector.save()
                sector.tooth.work_type = 5
                sector.tooth.save()
            elif tw['type'] == 6:
                tooth = Tooth.objects.get(id=tw['id'])
                if tw['color'] == 'red':
                    tooth.color = 1
                elif tw['color'] == 'blue':
                    tooth.color = 2
                else:
                    tooth.color = None
                tooth.work_type = 6
                tooth.save()

        odontogram_form = OdontogramForm(request.POST, instance=patient.odontogram)
        if odontogram_form.is_valid():
            odontogram = odontogram_form.save()
            date = request.POST.get('date_odontogram', None)
            if date:
                month, year = date.split(' - ')
                odontogram.month = month
                odontogram.year = year
                odontogram.save()
        return JsonResponse({'status': 'OK'})


@login_required
def acumulate_benefit(request, patient_id):
    from django.template.response import TemplateResponse
    if request.method == 'GET':
        patient = get_object_or_404(Patient, id=patient_id)
        return TemplateResponse(
            request, 'register/tab_total_details.html',
            {'patient': patient}
        )


@login_required
def edit_radiography(request, patient_id, bf_id):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, id=patient_id)
        if patient.social_work and patient.social_work.initial == 'APROSS':
            benefit = get_object_or_404(Apross, id=bf_id)
            radiography = Radiography.objects.get(apross=benefit)
        else:
            benefit = get_object_or_404(Benefit, id=bf_id)
            radiography = Radiography.objects.get(benefit=benefit)
        radiography_form = RadiographyForm(request.POST, instance=radiography)
        if radiography_form.is_valid():
            radiography = radiography_form.save()
            return JsonResponse({
                'status': 'OK',
                'rx_amount': radiography.rx_amount
            })
        else:
            return JsonResponse({'status': 'ERROR'})


@login_required
def new_record(request, patient_id):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, id=patient_id)
        form = RecordForm(request.POST)
        if form.is_valid():
            from django.template.response import TemplateResponse
            record = form.save(commit=False)
            record.patient = patient
            record.save()
            form.save_m2m()
            return TemplateResponse(
                request, 'register/record.html',
                {'patient': patient}
            )
        else:
            return JsonResponse({'status': 'ERROR', 'errors': form.errors})


@login_required
def edit_record(request, record_id):
    from django.template.response import TemplateResponse
    record = get_object_or_404(Record, id=record_id)
    if request.method == 'GET':
        form = RecordForm(instance=record)
        return TemplateResponse(
            request, 'register/_form_edit_record.html',
            {'r_edit_form': form}
        )
    else:
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return TemplateResponse(
                request, 'register/record.html',
                {'patient': record.patient}
            )
        else:
            return JsonResponse({'status': 'ERROR', 'errors': form.errors})

@login_required
def remove_record(request, record_id):
    from django.template.response import TemplateResponse
    if request.method == 'POST':
        record = get_object_or_404(Record, id=record_id)
        patient = Patient.objects.get(id=record.patient.id)
        record.delete()
        return TemplateResponse(
            request, 'register/record.html',
            {'patient': patient}
        )

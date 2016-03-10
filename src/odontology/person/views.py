from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import JsonResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from person.models import Patient, Dentist, Odontogram, Tooth, Sector, LOCATIONS, WORK_TYPES
from person.forms import PatientForm, OdontogramForm
from register.models import Apross, Benefit, ELEMENTS
from register.forms import AprossForm, detailAprossForm, BenefitForm, detailBenefitForm
from datetime import date as Date


def patients(request):
    from person.function import get_position
    dentist = Dentist.objects.get(user=request.user)
    if request.method == 'GET':
        rec_added = request.GET.get('add', None)
        form = PatientForm()
        patients = Patient.objects.filter(dentist=dentist).order_by('-id')
        paginator = Paginator(patients, 10)
        patients = paginator.page(1)
        return render_to_response(
            'person/patients.html',
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
        sub_num = request.POST.get('subsidiary_number', None)
        sub_num_exist = Patient.objects.filter(subsidiary_number=sub_num).exists()
        if sub_num == '' or not sub_num_exist:
            if form.is_valid():
                new_patient = form.save(commit=False)
                new_patient.dentist = dentist
                odontogram = Odontogram()
                odontogram.save()
                if not odontogram.get_teeth().exists():
                    for e1, e2 in ELEMENTS:
                        x, y = get_position(e2)
                        tooth = Tooth(odontogram=odontogram, number=e1, position_x=x, position_y=y)
                        tooth.save()
                        for l1, l2 in LOCATIONS:
                            Sector(tooth=tooth, location=l1, points=l1).save()
                new_patient.odontogram = odontogram
                new_patient.save()
                return JsonResponse({'status': 'OK'})
            else:
                return JsonResponse({'status': 'ERROR', 'errors': form.errors})
        else:
            form.errors['subsidiary_number'] = [u'Ya existe un/a Paciente con este/a Numero de afiliado.']
            return JsonResponse({'status': 'ERROR', 'errors': form.errors})


def search_patient(request):
    import operator
    from django.db.models import Q
    dentist = Dentist.objects.get(user=request.user)
    if request.method == 'GET':
        form = PatientForm()
        text_search = request.GET.get('text_search', None)

        if text_search is not None:
            terms = text_search.split(' ')
            qs1 = reduce(operator.or_, (Q(last_name__icontains=n) for n in terms))
            qs2 = reduce(operator.or_, (Q(first_name__icontains=n) for n in terms))
            qs3 = reduce(operator.or_, (Q(social_work__initial__icontains=n) for n in terms))
            qs4 = reduce(operator.or_, (Q(social_work__name__icontains=n) for n in terms))
            qs5 = reduce(operator.or_, (Q(subsidiary_number__icontains=n) for n in terms))

            patients = Patient.objects.filter(dentist=dentist)
            patients = patients.filter(Q(qs1) | Q(qs2) | Q(qs3) | Q(qs4) | Q(qs5) )

        return render_to_response(
            'person/list_patients.html',
            {
                'patients': patients,
                'text_search': text_search
            },
            RequestContext(request)
        )


def paginator_patient(request):
    if request.method == 'POST':
        dentist = Dentist.objects.get(user=request.user)
        patients = Patient.objects.filter(dentist=dentist).order_by('-id')

        paginator = Paginator(patients, 10)
        page = request.POST.get('page', 1)
        try:
            patients = paginator.page(page)
        except PageNotAnInteger:
            patients = paginator.page(1)
        except EmptyPage:
            patients = paginator.page(paginator.num_pages)
        data = {'patients': patients}
        pag_type = int(request.POST.get('type'))
        if pag_type == 1:
            return render_to_response(
                'person/list_patients.html',
                data,
                RequestContext(request)
            )
        elif pag_type == 2:
            return render_to_response(
                'person/paginator.html',
                data,
                RequestContext(request)
            )


def patient_profile(request, id):
    dentist = Dentist.objects.get(user=request.user)
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'GET':
        patient_info = PatientForm(instance=patient)
        if patient.social_work and patient.social_work.initial == 'APROSS':
            benefits = Apross.objects.filter(patient=patient).order_by('real_date')
            if benefits.exists():
                last_benefit = benefits.last()
            else:
                last_benefit = None
            benefit_form = AprossForm()
            detail_form = detailAprossForm()
        else:
            benefits = Benefit.objects.filter(patient=patient).order_by('real_date')
            if benefits.exists():
                last_benefit = benefits.last()
            else:
                last_benefit = None
            benefit_form = BenefitForm()
            detail_form = detailBenefitForm()
        odontogram_form = OdontogramForm(instance=patient.odontogram)
        rec_added = request.GET.get('add', None)
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
                'patient_info_form': patient_info,
                'work_types': WORK_TYPES,
                'odontogram_form': odontogram_form,
                'rec_added': rec_added
            },
            RequestContext(request)
        )


def edit_patient(request, id):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, id=id)
        patient_form = PatientForm(request.POST, instance=patient)
        if patient_form.is_valid():
            patient_form.save()
            return JsonResponse({'status': 'OK'})
        else:
            return JsonResponse({'status': 'ERROR', 'errors': patient_form.errors})

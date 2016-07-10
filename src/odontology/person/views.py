from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.response import TemplateResponse
from person.models import Patient, Dentist, Odontogram, Tooth, Sector, LOCATIONS, WORK_TYPES
from person.forms import PatientForm, OdontogramForm, UserChangeForm, DentistForm, PasswordForm, ImageUploadForm
from register.models import Apross, Benefit, ELEMENTS, MILK_TEETH
from register.forms import AprossForm, detailAprossForm, BenefitForm, detailBenefitForm, RadiographyForm, RecordForm, AccountingForm
from datetime import date as Date
from django.contrib.auth.decorators import login_required


@login_required
def patients(request):
    from person.function import get_position
    dentist = request.user.dentist
    if request.method == 'GET':
        patients = Patient.objects.filter(dentist=dentist, active=True).order_by('-id')

        import operator
        from django.db.models import Q
        text_search = request.GET.get('text_search', None)
        if text_search is not None:
            terms = text_search.split(' ')
            qs1 = reduce(operator.or_, (Q(last_name__icontains=n) for n in terms))
            qs2 = reduce(operator.or_, (Q(first_name__icontains=n) for n in terms))
            qs3 = reduce(operator.or_, (Q(social_work__initial__icontains=n) for n in terms))
            qs4 = reduce(operator.or_, (Q(social_work__name__icontains=n) for n in terms))
            qs5 = reduce(operator.or_, (Q(subsidiary_number__icontains=n) for n in terms))
            patients = patients.filter(Q(qs1) | Q(qs2) | Q(qs3) | Q(qs4) | Q(qs5) )

        page = request.GET.get('page', 1)
        nro_row = request.GET.get('nro_row', '10')
        paginator = Paginator(patients, nro_row)
        try:
            patients = paginator.page(page)
        except PageNotAnInteger:
            patients = paginator.page(1)
        except EmptyPage:
            patients = paginator.page(paginator.num_pages)

        if request.is_ajax():
            return TemplateResponse(
                request, 'person/patients/table.html',
                {
                    'patients': patients,
                    'nro_row': nro_row,
                }
            )
        else:
            form = PatientForm()
            return render_to_response(
                'person/patients.html',
                {
                    'template': 'patient',
                    'patient_form': form,
                    'patients': patients,
                    'text_search': text_search,
                    'nro_row': nro_row,
                },
                RequestContext(request)
            )
    else:
        form = PatientForm(request.POST)
        sub_num = request.POST.get('subsidiary_number', None)
        sub_num_exist = Patient.objects.filter(dentist=dentist, subsidiary_number=sub_num).exists()
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
                        if (e1, e2) in MILK_TEETH:
                            tooth.work_type = 1
                            tooth.color = 1
                        tooth.save()
                        for l1, l2 in LOCATIONS:
                            Sector(tooth=tooth, location=l1, points=l1).save()
                new_patient.odontogram = odontogram
                new_patient.code = 'P%04d' % (dentist.number_of_patients + 1)
                new_patient.save()
                return JsonResponse(
                    {'status': 'OK',
                     'url': reverse('person:profile_patient', kwargs={'id': new_patient.id})
                    }
                )
            else:
                return JsonResponse({'status': 'ERROR', 'errors': form.errors})
        else:
            form.errors['subsidiary_number'] = [u'Ya existe un/a Paciente con este/a Numero de afiliado.']
            return JsonResponse({'status': 'ERROR', 'errors': form.errors})


@login_required
def profile_patient(request, id):
    dentist = request.user.dentist
    patient = get_object_or_404(
        Patient, id=id,
        dentist=dentist
    )
    patient_info = PatientForm(instance=patient)
    rec_added = request.GET.get('add', None)
    img_upload_form = ImageUploadForm(instance=patient)
    return render_to_response(
        'person/profile.html',
        {
            'patient': patient,
            'patient_info_form': patient_info,
            'rec_added': rec_added,
            'img_upload_form': img_upload_form,
        },
        RequestContext(request)
    )


@login_required
def clinical_history(request, id):
    dentist = request.user.dentist
    patient = get_object_or_404(
        Patient, id=id,
        dentist=dentist
    )
    if request.method == 'GET':
        rform = RecordForm()
        return render_to_response(
            'person/clinical_history.html',
            {
                'dentist': dentist,
                'patient': patient,
                'rform': rform,
            },
            RequestContext(request)
        )


@login_required
def social_work(request, id):
    dentist = request.user.dentist
    patient = get_object_or_404(
        Patient, id=id,
        dentist=dentist
    )
    if request.method == 'GET':
        if patient.social_work and patient.social_work.initial == 'APROSS':
            benefits = Apross.objects.filter(patient=patient).order_by('-real_date')
            if benefits.exists():
                last_benefit = benefits.first()
            else:
                last_benefit = None
            benefit_form = AprossForm()
            detail_form = detailAprossForm()
        else:
            benefits = Benefit.objects.filter(patient=patient).order_by('-real_date')
            if benefits.exists():
                last_benefit = benefits.first()
            else:
                last_benefit = None
            benefit_form = BenefitForm()
            detail_form = detailBenefitForm()
        odontogram_form = OdontogramForm(instance=patient.odontogram)
        rec_added = request.GET.get('add', None)
        return render_to_response(
            'person/social_work.html',
            {
                'dentist': dentist,
                'patient': patient,
                'benefits': benefits,
                'last_benefit': last_benefit,
                'benefit_form': benefit_form,
                'detail_form': detail_form,
                'work_types': WORK_TYPES,
                'odontogram_form': odontogram_form,
                'rec_added': rec_added,
            },
            RequestContext(request)
        )


@login_required
def accounts(request, id):
    dentist = request.user.dentist
    patient = get_object_or_404(
        Patient, id=id,
        dentist=dentist
    )
    if request.method == 'GET':
        aform = AccountingForm()
        return render_to_response(
            'person/accounts.html',
            {
                'patient': patient,
                'aform': aform,
            },
            RequestContext(request)
        )


@login_required
def odontogram(request, id):
    if request.method == 'GET':
        dentist = request.user.dentist
        patient = get_object_or_404(
            Patient, id=id,
            dentist=dentist
        )
        odontogram_form = OdontogramForm(instance=patient.odontogram)
        return render_to_response(
            'person/odontogram.html',
            {
                'patient': patient,
                'odontogram_form': odontogram_form,
                'work_types': WORK_TYPES,
            },
            RequestContext(request)
        )


@login_required
def edit_patient(request, id):
    if request.method == 'POST':
        dentist = request.user.dentist
        patient = get_object_or_404(
            Patient, id=id,
            dentist=dentist
        )
        patient_form = PatientForm(request.POST, instance=patient)
        if patient_form.is_valid():
            patient_form.save()
            patient_info = PatientForm(instance=patient)
            return TemplateResponse(
                request, 'register/patient_data/_form.html',
                {'patient_info_form': patient_info, 'patient': patient}
            )
        else:
            return JsonResponse({'status': 'ERROR', 'errors': patient_form.errors})


@login_required
def upload_picture(request, id):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dentist = request.user.dentist
            patient = get_object_or_404(
                Patient, id=id,
                dentist=dentist
            )
            patient.picture.delete()
            patient.picture = form.cleaned_data['picture']
            patient.save()
            return TemplateResponse(
                request, 'register/patient_data/_form_picture.html',
                {'patient': patient}
            )


@login_required
def remove_patient(request, id):
    if request.method == 'POST':
        dentist = request.user.dentist
        patient = get_object_or_404(
            Patient, id=id,
            dentist=dentist
        )
        patient.active = False
        patient.save()
        return redirect('person:patient_list')


@login_required
def settings(request):
    dentist = request.user.dentist
    if request.method == 'GET':
        user_change_form = UserChangeForm(instance=request.user)
        dentist_form = DentistForm(instance=dentist)
        return render_to_response(
            'person/settings/content.html',
            {
                'user_change_form': user_change_form,
                'dentist_form': dentist_form,
            },
            RequestContext(request)
        )


@login_required
def settings_personal(request):
    if request.method == 'POST':
        user_change_form = UserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return TemplateResponse(
                request, 'person/settings/_form_personal.html',
                {'user_change_form': user_change_form},
                RequestContext(request)
            )
        else:
            return JsonResponse({'status': 'ERROR', 'errors': user_change_form.errors})


@login_required
def settings_dentist(request):
    if request.method == 'POST':
        dentist = request.user.dentist
        dentist_form = DentistForm(request.POST, instance=dentist)
        if dentist_form.is_valid():
            dentist_form.save()
            return TemplateResponse(
                request, 'person/settings/_form_dentist.html',
                {'dentist_form': dentist_form},
                RequestContext(request)
            )
        else:
            return JsonResponse({'status': 'ERROR', 'errors': dentist_form.errors})


@login_required
def reset_password(request):
    dentist = Dentist.objects.get(user=request.user)
    if request.method == 'GET':
        password_form = PasswordForm()
        return render_to_response(
            'person/reset_password/content.html',
            {
                'password_form': password_form,
            },
            RequestContext(request)
        )
    else:
        password_form = PasswordForm(request.POST)
        if password_form.is_valid():
            old_password = request.POST.get('old_password', '')
            user = authenticate(username=request.user.username, password=old_password)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    new_password = request.POST.get('new_password', '')
                    confirm_password = request.POST.get('confirm_password', '')
                    if new_password == confirm_password:
                        request.user.set_password(new_password)
                        request.user.save()
                        password_form = PasswordForm()
                        return TemplateResponse(
                            request, 'person/reset_password/_form.html',
                            {'password_form': password_form},
                            RequestContext(request)
                        )
                    else:
                        password_form.errors['new_password'] = 'Las dos claves no coinciden.'
                        password_form.errors['confirm_password'] = ''
                        return JsonResponse({'status': 'ERROR', 'errors': password_form.errors})
            else:
                password_form.errors['old_password'] = 'clave incorrecta.'
                return JsonResponse({'status': 'ERROR', 'errors': password_form.errors})
        else:
            return JsonResponse({'status': 'ERROR', 'errors': password_form.errors})


@login_required
def registers(request):
    if request.method == 'GET':
        return render_to_response(
            'person/registers.html',
            {
                'template': 'register',
            },
            RequestContext(request)
        )


@login_required
def accounts_registers(request):
    if request.method == 'GET':
        return render_to_response(
            'person/registers/account.html',
            {
                'template': 'register',
            },
            RequestContext(request)
        )


@login_required
def accounts_registers_data(request):
    if request.method == 'GET':
        from register.models import Record
        from datetime import datetime
        from django.db.models import Sum

        date_from = request.GET.get('date_from', None)
        date_to = request.GET.get('date_to', None)
        date_from = datetime.strptime(
            date_from,
            '%d/%m/%Y %H:%M'
        )
        date_to = datetime.strptime(
            date_to,
            '%d/%m/%Y %H:%M'
        )

        records = Record.objects.filter(
            patient__dentist=request.user.dentist,
            date__gte=date_from,
            date__lte=date_to,
            to_account=True,
        ).order_by('-date')
        total_debit_records = records.aggregate(total=Sum('debit'))['total']
        total_having_records = records.aggregate(total=Sum('havings'))['total']
        if total_debit_records is not None and total_having_records is not None:
            total_balance = total_debit_records - total_having_records
        else:
            total_balance = None
        return render_to_response(
            'person/registers/list.html',
            {
                'template': 'register',
                'records': records,
                'total_debit_records': total_debit_records,
                'total_having_records': total_having_records,
                'total_balance': total_balance,
            },
            RequestContext(request)
        )

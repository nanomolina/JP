$(document).ready(function() {
    $('#save-patient-info').on('click', function(event) {
        $('#save-patient-info').button('loading');
        $('#cancel-patient-info').addClass('hide');
        var data_form = $('#patient-info-form').serialize();
        var url = $('#patient-info-form').attr('action');
        $.ajax({
          type: "POST",
          url: url,
          data: data_form,
          success: function(data) {
              if (data.status === 'OK') {
                var url = $('#patient-form').attr('action');
                location.href = '';
              } else {
                $('#btn-save-patient').button('reset');
                if (data.errors.first_name !== undefined) {
                    $('#patient-form .form-group').first().addClass('has-error');
                    $('#patient-form .form-group').first().find('#helpBlock1').removeClass('hidden');
                    $('#patient-form .form-group').first().find('#helpBlock1').text(data.errors.first_name[0]);
                } else {
                    $('#patient-form .form-group').first().addClass('has-success');
                }
                if (data.errors.last_name !== undefined) {
                    $('#patient-form .form-group').first().next().addClass('has-error');
                    $('#patient-form .form-group').first().next().find('#helpBlock2').removeClass('hidden');
                    $('#patient-form .form-group').first().next().find('#helpBlock2').text(data.errors.last_name[0]);
                } else {
                    $('#patient-form .form-group').first().next().addClass('has-success');
                }
                if (data.errors.social_work !== undefined) {
                    $('#patient-form .form-group').last().addClass('has-error');
                    $('#patient-form .form-group').last().find('#helpBlock3').removeClass('hidden');
                    $('#patient-form .form-group').last().find('#helpBlock3').text(data.errors.social_work[0]);
                } else {
                    $('#patient-form .form-group').last().addClass('has-success');
                }
              }
          }
        });
    });
});

$(function() {
  $('#edit-patient-info').on('click', function() {
    $('.field-info').hide();
    $('.edit-info').removeClass('hide');
    $('#cancel-patient-info').removeClass('hide');
    $('#save-patient-info').removeClass('hide');
    $(this).addClass('hide');
    $('#patient-info-form .basic-info').removeClass('hide');
  });

  $('#cancel-patient-info').on('click', function() {
    $('.field-info').show();
    $('.edit-info').addClass('hide');
    $('#save-patient-info').addClass('hide');
    $('#edit-patient-info').removeClass('hide');
    $(this).addClass('hide');
    $('#patient-info-form .basic-info').addClass('hide');
  });

  $('#birth_date_picker').datetimepicker({
      format: 'DD/MM/YYYY',
      locale: 'es',
  });
});

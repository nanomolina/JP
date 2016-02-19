$(document).ready(function() {
    $('#btn-save-patient-info').on('click', function(event) {
        $('#btn-save-patient-info').button('loading')
        var data_form = $('#patient-form').serialize();
        var url = $('#patient-form').attr('action');
        $('#patient-form .form-group').removeClass('has-error');
        $('#patient-form .form-group').find('.help-block').addClass('hidden');
        $.ajax({
          type: "POST",
          url: url,
          data: data_form,
          success: function(data) {
              if (data.status === 'OK') {
                var url = $('#patient-form').attr('action');
                location.href = url + "?add=1";
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

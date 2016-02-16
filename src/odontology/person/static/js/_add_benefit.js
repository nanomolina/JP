$(document).ready(function() {
    $('#btn-save-benefit').on('click', function(event) {
        $('#btn-save-benefit').button('loading')
        var data_form = $('#benefit-form').serialize();
        $('#benefit-form .form-group').removeClass('has-error');
        $('#benefit-form .form-group').find('.help-block').addClass('hidden');
        var url = $('#benefit-form').attr('action');
        $.ajax({
          type: "POST",
          url: url,
          data: data_form,
          success: function(data) {
              if (data.status === 'OK') {
                location.href = url;
              } else {
                $('#btn-save-benefit').button('reset');
                if (data.errors.first_name !== undefined) {
                    $('#benefit-form .form-group').first().addClass('has-error');
                    $('#benefit-form .form-group').first().find('#helpBlock1').removeClass('hidden');
                    $('#benefit-form .form-group').first().find('#helpBlock1').text(data.errors.first_name[0]);
                } else {
                    $('#benefit-form .form-group').first().addClass('has-success');
                }
                if (data.errors.last_name !== undefined) {
                    $('#benefit-form .form-group').first().next().addClass('has-error');
                    $('#benefit-form .form-group').first().next().find('#helpBlock2').removeClass('hidden');
                    $('#benefit-form .form-group').first().next().find('#helpBlock2').text(data.errors.last_name[0]);
                } else {
                    $('#benefit-form .form-group').first().next().addClass('has-success');
                }
                if (data.errors.social_work !== undefined) {
                    $('#benefit-form .form-group').last().addClass('has-error');
                    $('#benefit-form .form-group').last().find('#helpBlock3').removeClass('hidden');
                    $('#benefit-form .form-group').last().find('#helpBlock3').text(data.errors.social_work[0]);
                } else {
                    $('#benefit-form .form-group').last().addClass('has-success');
                }
              }
          }
        });
    });
});

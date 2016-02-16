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
                if (data.errors.date !== undefined) {
                    $('#benefit-form .form-group').first().addClass('has-error');
                    $('#benefit-form .form-group').first().find('#helpBlock1').removeClass('hidden');
                    $('#benefit-form .form-group').first().find('#helpBlock1').text(data.errors.date[0]);
                } else {
                    $('#benefit-form .form-group').first().addClass('has-success');
                }
                if (data.errors.managment_code1 !== undefined) {
                    $('#benefit-form .form-group').first().next().addClass('has-error');
                    $('#benefit-form .form-group').first().next().find('#helpBlock2').removeClass('hidden');
                    $('#benefit-form .form-group').first().next().find('#helpBlock2').text(data.errors.managment_code1[0]);
                } else {
                    $('#benefit-form .form-group').first().next().addClass('has-success');
                }
                if (data.errors.managment_code2 !== undefined) {
                    $('#benefit-form .form-group').first().next().next().addClass('has-error');
                    $('#benefit-form .form-group').first().next().next().find('#helpBlock3').removeClass('hidden');
                    $('#benefit-form .form-group').first().next().next().find('#helpBlock3').text(data.errors.managment_code2[0]);
                } else {
                    $('#benefit-form .form-group').first().next().next().addClass('has-success');
                }
                if (data.errors.managment_code3 !== undefined) {
                    $('#benefit-form .form-group').last().prev().addClass('has-error');
                    $('#benefit-form .form-group').last().prev().find('#helpBlock3').removeClass('hidden');
                    $('#benefit-form .form-group').last().prev().find('#helpBlock3').text(data.errors.managment_code3[0]);
                } else {
                    $('#benefit-form .form-group').last().prev().addClass('has-success');
                }
                if (data.errors.rx_amount !== undefined) {
                    $('#benefit-form .form-group').last().addClass('has-error');
                    $('#benefit-form .form-group').last().find('#helpBlock3').removeClass('hidden');
                    $('#benefit-form .form-group').last().find('#helpBlock3').text(data.errors.rx_amount[0]);
                } else {
                    $('#benefit-form .form-group').last().addClass('has-success');
                }
              }
          }
        });
    });
});

$(function () {
    $('#datetimepicker1').datetimepicker({
      'format': 'DD/MM/YY'
    });
});

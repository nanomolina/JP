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
                    $('.date-group').addClass('has-error');
                    $('#helpBlock1').removeClass('hidden');
                    $('#helpBlock1').text(data.errors.date[0]);
                } else {
                    $('.first-inputs').first().addClass('has-success');
                }
                if (data.errors.rx_amount !== undefined) {
                    $('.rx_amount_group').addClass('has-error');
                    $('#helpBlock2').removeClass('hidden');
                    $('#helpBlock2').text(data.errors.rx_amount[0]);
                } else {
                    $('.rx_amount_group').addClass('has-success');
                }
                if (data.errors.managment_code1 !== undefined) {
                    $('.code1-group').addClass('has-error');
                    $('#helpBlock3').removeClass('hidden');
                    $('#helpBlock3').text(data.errors.managment_code1[0]);
                } else {
                    $('.code1-group').addClass('has-success');
                }
                if (data.errors.managment_code2 !== undefined) {
                    $('.code2-group').addClass('has-error');
                    $('#helpBlock4').removeClass('hidden');
                    $('#helpBlock4').text(data.errors.managment_code2[0]);
                } else {
                    $('.code2-group').addClass('has-success');
                }
                if (data.errors.managment_code3 !== undefined) {
                    $('.code3-group').addClass('has-error');
                    $('#helpBlock5').removeClass('hidden');
                    $('#helpBlock5').text(data.errors.managment_code3[0]);
                } else {
                    $('.code3-group').addClass('has-success');
                }
              }
          }
        });
    });
});

$(function () {
    var dateNow = new Date();
    $('#datetimepicker1').datetimepicker({
        viewMode: 'months',
        format: 'MMMM - YYYY',
        locale: 'es',
        defaultDate: dateNow,
    });
});

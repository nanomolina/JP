// --- BENEFIT ---
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
              if (data.status !== 'ERROR') {
                location.href = url_profile;
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

$(function () {
  $('#select-benefit').change(function () {
      $('.benefits').hide();
      var id = $( "#select-benefit option:selected" ).val();
      $('#benefit-'+id).show();
      $('#edit_bf').data('bf-id', id);
  }).change();
});

function edit_benefit() {
    var bf_id = $('#edit_bf').data('bf-id');
    var csrf = $('#edit_bf').data('csrf');
    $('#modal-edit-benefit').load(
      URL_EDIT_BF,
      {'bf_id': bf_id, 'csrfmiddlewaretoken': csrf, 'get': 1});
}
// --- BENEFIT DETAIL ---

function edit_benefit_detail(id) {
    var $row_detail = $('#bf-detail-'+id);
    $row_detail.find('.edit').removeClass('hide');
    $row_detail.find('.detail-info').addClass('hide');
    var $edit_button = $('#bf-detail-edit-'+id);
    $edit_button.addClass('hide');
    var $save_button = $('#bf-detail-save-'+id);
    $save_button.removeClass('hide');
}

function save_benefit_detail(id) {
    $('#bf-detail-save-'+id).button('loading');
    $detail = $('#bf-detail-'+id);
    var data_form = $detail.find('input, select').serialize();
    var url = $detail.attr('action');
    var posting = $.post( url, data_form );
    posting.done(function(data) {
        $detail.html($(data).children());
        var range = getMonthDateRange($(data).data('year'), $(data).data('month'));
        $('#day-'+$(data).data('id')).datetimepicker({
            viewMode: 'days',
            format: 'D',
            locale: 'es',
            minDate: range.start.toDate(),
            maxDate: range.end.toDate()
        });
        $('.selectpicker').selectpicker();

    });
}

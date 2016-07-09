// --- BENEFIT ---
$(document).ready(function() {
    $('#btn-save-benefit').on('click', function(event) {
        $('#btn-save-benefit').button('loading')
        var data_form = $('#benefit-form').serialize();
        var url = $('#benefit-form').attr('action');
        $('#benefit-form .has-error').removeClass('has-error');
        $('#benefit-form .has-success').removeClass('has-success');
        $('#alert-add-apross').addClass('hide')
        $.ajax({
          type: "POST",
          url: url,
          data: data_form,
          success: function(data) {
              if (data.status !== 'ERROR') {
                location.href = url_profile + '?add=1';
              } else {
                $('#btn-save-benefit').button('reset');
                $('#benefit-form .input-fields').addClass('has-success');
                $('#alert-add-apross').removeClass('hide')
                validate_errors('benefit-form', data.errors, 'alert-add-apross');
              }
          }
        });
    });

});

function validate_errors(name_form, json_errors, alert) {
  var alert_content = '';
  for (var key in json_errors) {
      $('#'+name_form).find('.'+key+'-group').addClass('has-error');
      alert_content += '<p>' + json_errors[key] + '</p>';
  }
  $('#'+alert).html(alert_content);
}

$(function () {
    var dateNow = new Date();
    $('#date_add_bf_picker').datetimepicker({
        viewMode: 'months',
        format: 'MMMM - YYYY',
        locale: 'es',
        defaultDate: dateNow,
    });

    $('#select-benefit').change(function () {
        $('.benefits').hide();
        var $selected = $( "#select-benefit option:selected" );
        var id = $selected.val();
        var text = $selected.text();
        $('#benefit-'+id).show();
        $('#edit_bf').data('bf-id', id);
        edit_url_pdf(id);
        edit_print_modal(text);
    }).change();

});

function print_benefit(){
  $('#button-print').button('loading');
  var url = $('#form-print').attr('action');
  url += '?' + $('#form-print').serialize();
  $.ajax({
    type: 'GET',
    url: url,
    success: function(data) {
      $('#block-to-print').html(data);
      $('#button-print').button('reset');
      $('#modal-print').modal('hide');
      setTimeout(function(){
        window.print();
      }, 500);
    }
  })
}

function edit_url_pdf(id) {
    var url_split = $('#form-print').attr('action').split('/');
    url_split[5] = id;
    $('#form-print').attr('action', url_split.join('/'));
}

function edit_print_modal(text){
    $('#modal-print .record-name').html(text);
}

function edit_benefit() {
    var bf_id = $('#edit_bf').data('bf-id');
    var csrf = $('#edit_bf').data('csrf');
    $('#benefit-edit-form .modal-body').addClass('hide');
    $('.loading').removeClass('hide');
    $('#benefit-edit-form .modal-footer button').addClass('hide');
    $('#benefit-edit-form').load(
      URL_EDIT_BF,
      {'bf_id': bf_id, 'csrfmiddlewaretoken': csrf, 'get': 1},
      function() {
        setTimeout(function(){
            $('#benefit-edit-form .modal-body').removeClass('hide');
            $('#benefit-edit-form .modal-footer button').removeClass('hide');
            $('.loading').addClass('hide');
        }, 750);
      }

    );
}

// --- END BENEFIT ---


// --- BENEFIT DETAIL ---
function edit_benefit_detail(id) {
    var $row_detail = $('#bf-detail-'+id);
    $row_detail.find('.edit').removeClass('hide');
    $row_detail.find('.detail-info').addClass('hide');
    var $edit_button = $('#bf-detail-edit-'+id);
    $edit_button.addClass('hide');
    var $save_button = $('#bf-detail-save-'+id);
    $save_button.removeClass('hide');
    $row_detail.find('.label-primary').removeClass('label-primary').addClass('label-success');
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
        $detail.find('.label-success').removeClass('label-success').addClass('label-primary');
    });
}

// --- END BENEFIT DETAIL ---

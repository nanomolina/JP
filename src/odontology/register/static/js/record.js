$(function () {
    $('#date_gral').datetimepicker({
        locale: 'es',
    });
    $('#date_period_so').datetimepicker({
        viewMode: 'months',
        format: 'MMMM - YYYY',
        locale: 'es',
    });
});

function save_record() {
  $('#btn-save-record').button('loading');
  var $form = $('#record-form');
  var data_form = $form.serialize();
  var url = $form.attr('action');
  $form.find('.has-error').removeClass('has-error');
  $form.find('.has-success').removeClass('has-success');
  $('#alert-add-record').addClass('hide');
  $.ajax({
    type: "POST",
    url: url,
    data: data_form,
    success: function(data) {
        if (data.status !== 'ERROR') {
          $('#tbody-record').html(data);
          $('#modal-record').modal('hide');
          toastr.success('Se ah agragado exitosamente.', 'REGISTRO AGREGADO');
        } else {
          $('#record-form .input-fields').addClass('has-success');
          $('#alert-add-record').removeClass('hide');
          validate_errors('record-form', data.errors, 'alert-add-record');
        }
        $('#btn-save-record').button('reset');
    }
  });
}

function reset_form() {
    $('#id_faces').selectpicker('val', '');
    $('#id_tooth').selectpicker('val', '');
}

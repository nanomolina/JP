$(function () {
    var dateNow = new Date();
    $('#modal-record #date_gral').datetimepicker({
        locale: 'es',
        defaultDate: dateNow,
    });
    $('#modal-record #date_period_so').datetimepicker({
        viewMode: 'months',
        format: 'MMMM - YYYY',
        locale: 'es',
    });
    $('.rec-popover').popover();
});

function init_form_edit(){
  var $modal = $('#modal-edit-record');
  var $dp_input = $modal.find('#id_date');
  year = $dp_input.data('year');
  month = $dp_input.data('month') - 1;
  day = $dp_input.data('day');
  hour = $dp_input.data('hour');
  minute = $dp_input.data('minute');
  var date = new Date(year, month, day, hour, minute);
  $modal.find('#date_gral').datetimepicker({
      locale: 'es',
      defaultDate: date,
  });
  $modal.find('#date_period_so').datetimepicker({
      viewMode: 'months',
      format: 'MMMM - YYYY',
      locale: 'es',
  });
  $modal.find('#id_faces').selectpicker('show');
  $modal.find('#id_tooth').selectpicker('show');
  $modal.find('#id_state').selectpicker('show');
  $modal.find('#id_assistance').selectpicker('show');
}

// function check_alert(){
//   show_alert = false;
//   $('#tbody-record tr').each(function(key, value){
//     if ($(this).hasClass('info')){
//       show_alert = true;
//       return false;
//     }
//   });
//   if (show_alert) {
//     $('#alert-obs').removeClass('hide');
//   } else {
//     $('#alert-obs').addClass('hide');
//   }
// }

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
          $('.rec-popover').popover();
          // check_alert();
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

function load_record_modal(url) {
  var $modal = $('#modal-edit-record');
  $modal.find('.loading').show();
  $modal.find('#form-edit-record').hide();
  $modal.modal('show');
  $modal.find('#form-edit-record').load(url, function(){
    init_form_edit();
    $modal.find('#form-edit-record').show();
    $('#modal-edit-record').find('.loading').hide();
  });
}

function edit_record(url) {
  $('#btn-edit-record').button('loading');
  var $form = $('#form-edit-record');
  var data_form = $form.serialize();
  $form.find('.has-error').removeClass('has-error');
  $form.find('.has-success').removeClass('has-success');
  $('#alert-edit-record').addClass('hide');
  $.ajax({
    type: "POST",
    url: url,
    data: data_form,
    success: function(data) {
        if (data.status !== 'ERROR') {
          $('#tbody-record').html(data);
          $('#modal-edit-record').modal('hide');
          $('.rec-popover').popover();
          // check_alert();
          toastr.success('Se ah editado exitosamente.', 'REGISTRO EDITADO');
        } else {
          $('#form-edit-record .input-fields').addClass('has-success');
          $('#alert-edit-record').removeClass('hide');
          validate_errors('form-edit-record', data.errors, 'alert-edit-record');
        }
        $('#btn-edit-record').button('reset');
    }
  });
}

function load_delete_modal(url) {
  var $modal = $('#modal-delete');
  $modal.modal('show');
  $modal.find('#btn-delete').attr('href', 'javascript: delete_record("'+url+'")');
}

function delete_record(url) {
  var $modal = $('#modal-delete');
  $modal.find('#btn-delete').button('loading');
  $.ajax({
    type: "POST",
    url: url,
    data: $('#csrf_token').serialize(),
    success: function(data) {
        if (data.status !== 'ERROR') {
          $('#tbody-record').html(data);
          $('#modal-delete').modal('hide');
          $('.rec-popover').popover();
          // check_alert();
          toastr.success('Se ah borrado exitosamente.', 'REGISTRO BORRADO');
        } else {
          toastr.error('', 'ERROR AL BORRAR');
        }
        $('#modal-delete').find('#btn-delete').button('reset');
    }

  });
}

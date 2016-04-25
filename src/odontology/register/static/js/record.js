$(function () {
    $('#date_gral').datetimepicker({
        locale: 'es',
    });
    $('#date_period_so').datetimepicker({
        viewMode: 'months',
        format: 'MMMM - YYYY',
        locale: 'es',
    });
    $('.rec-popover').popover();
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
          $('.rec-popover').popover();
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

function load_record(id) {
  var url = '/register/record/edit/'+id+'/';
  var $modal = $('#modal-edit-record');
  $modal.find('.loading').show();
  $modal.find('#form-edit-record').hide();
  $modal.modal('show');
  $modal.find('#form-edit-record').load(url, function(){
    $modal.find('#form-edit-record').show();
    $('#modal-edit-record').find('.loading').hide();
  });
}

function edit_record(id) {
  $('#btn-edit-record').button('loading');
  var $form = $('#form-edit-record');
  var data_form = $form.serialize();
  var url = '/register/record/edit/'+id+'/';
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

function load_delete(id) {
  var $modal = $('#modal-delete');
  $modal.modal('show');
  $modal.find('#btn-delete').attr('href', 'javascript: delete_record('+id+')');
}

function delete_record(id) {
  var $modal = $('#modal-delete');
  $modal.find('#btn-delete').button('loading');
  var url = '/register/record/remove/'+id+'/';
  $.ajax({
    type: "POST",
    url: url,
    data: $('#csrf_token').serialize(),
    success: function(data) {
        if (data.status !== 'ERROR') {
          $('#tbody-record').html(data);
          $('#modal-delete').modal('hide');
          $('.rec-popover').popover();
          toastr.success('Se ah borrado exitosamente.', 'REGISTRO BORRADO');
        } else {
          toastr.error('Se ah borrado exitosamente.', 'REGISTRO NO BORRADO');
        }
        $('#modal-delete').find('#btn-delete').button('reset');
    }

  })

}

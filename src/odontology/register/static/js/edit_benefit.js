$(document).ready(function() {
  $('#btn-edit-benefit').on('click', function(event) {
      $('#btn-edit-benefit').button('loading')
      var data_form = $('#benefit-edit-form').serialize();
      var url = $('#benefit-edit-form').attr('action');
      $('#benefit-edit-form .has-error').removeClass('has-error');
      $('#benefit-edit-form .has-success').removeClass('has-success');
      $('#alert-edit-apross').addClass('hide')
      $.ajax({
        type: "POST",
        url: url,
        data: data_form,
        success: function(data) {
            if (data.status !== 'ERROR') {
              location.href = url_profile + '?add=2';
            } else {
              $('#btn-edit-benefit').button('reset');
              $('#benefit-edit-form .input-fields').addClass('has-success');
              $('#alert-edit-apross').removeClass('hide')
              validate_errors('benefit-edit-form', data.errors, 'alert-edit-apross');
            }
        }
      });
  });
});

$(function () {
    $('#date_edit_bf_picker').datetimepicker({
        viewMode: 'months',
        format: 'MMMM - YYYY',
        locale: 'es',
    });
    $('#benefit-edit-form #id_date').val(DATE);
});

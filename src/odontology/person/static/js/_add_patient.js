$(document).ready(function() {
    $('#btn-save-patient').on('click', function(event) {
        $('#btn-save-patient').button('loading')
        var data_form = $('#patient-form').serialize();
        var url = $('#patient-form').attr('action');
        $('#patient-form .form-group').removeClass('has-error has-success');
        $('#alert-add-patient').addClass('hide')
        $.ajax({
          type: "POST",
          url: url,
          data: data_form,
          success: function(data) {
              if (data.status === 'OK') {
                location.href = data.url + '?add=1';
              } else {
                $('#btn-save-patient').button('reset');
                $('#patient-form .form-group').addClass('has-success');
                $('#alert-add-patient').removeClass('hide')
                validate_errors('patient-form', data.errors, 'alert-add-patient');
              }
          }
        });
    });
});

$(function(){
  $('#id_social_work').change(function(){
    $('#id_social_work option:selected').each(function() {
        if ($(this).val() == '') {
          $('#id_subsidiary_number').parent().hide('fast');
          $('#modal-patient').find('.modal-body').css('padding-bottom', '85px');
        } else {
          $('#id_subsidiary_number').parent().show('fast');
          $('#modal-patient').find('.modal-body').css('padding-bottom', '0px');
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

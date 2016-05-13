$(document).ready(function(){
  $('.loader').on('click', function(){
    $("#fakeLoader").fakeLoader({
        timeToHide: 10000000,
        bgColor:"#3498db",
        spinner:"spinner4"
    });
  });
});

$(function(){
  toastr.options = {
    "closeButton": true,
    "positionClass": "toast-bottom-right",
    "preventDuplicates": true,
    // "progressBar": true,
  }
});

function validate_errors(name_form, json_errors, alert) {
  var alert_content = '';
  for (var key in json_errors) {
      $('#'+name_form).find('.'+key+'-group').addClass('has-error');
      alert_content += '<p>' + json_errors[key] + '</p>';
  }
  $('#'+alert).html(alert_content);
}

function logout() {
  $('#form-logout').submit();
}

$(document).ready(function(){
  setTimeout(function(){
    $('#id_patient').selectpicker('setStyle', 'btn-lg');
    $('#id_patient').selectpicker('refresh');
  }, 250);

  $('.patient-dependence').on('click', function(){
    var patient_id = $('#id_patient').val();
    $('.parent-patient-dependence').removeClass('active');
    $(this).parent().addClass('active');
    if (patient_id == '') {
      $('#id_patient').selectpicker('toggle');
    } else {
      start_fake_loader();
      location.href = $(this).data('href') + patient_id + '/';
    }
  });

  $('#id_patient').on('change', function(){
    var $panel_active = $('.parent-patient-dependence.active');
    var patient_id = $('#id_patient').val();
    if (patient_id != '') {
      if ($panel_active.length == 1) {
        var href = $panel_active.find('.patient-dependence').data('href');
        start_fake_loader();
        location.href = href + patient_id + '/';
      }
    }
  });
});

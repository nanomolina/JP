// $(document).ready(function() {
//     $('#save-patient-info').on('click', function(event) {
//         $('#save-patient-info').button('loading');
//         $('#cancel-patient-info').addClass('hide');
//         var data_form = $('#patient-info-form').serialize();
//         var url = $('#patient-info-form').attr('action');
//         $.ajax({
//           type: "POST",
//           url: url,
//           data: data_form,
//           success: function(data) {
//               if (data.status != 'ERROR') {
//                 var url = $('#patient-form').attr('action');
//                 $('#info .content').html(data);
//                 $('#save-patient-info').button('reset').addClass('hide');
//                 $('#edit-patient-info').removeClass('hide');
//                 toastr.success('La información del paciente ah sido editada correctamente', 'INFORMACION EDITADA');
//               } else {
//                 $('#save-patient-info').button('reset').addClass('hide');
//                 $('#edit-patient-info').removeClass('hide');
//                 validate_errors('patient-info-form', data.errors, '');
//                 toastr.error('Hubo un error tratando de editar los datos.', 'DATOS ERRONEOS');
//               }
//           }
//         });
//     });
// });

$(function() {
  $('#edit-radiography').on('click', function() {
    var $form = $('#radiography-form');
    $form.find('.field-info').hide();
    $form.find('.edit-info').removeClass('hide');
    $('#cancel-radiography').removeClass('hide');
    $('#save-radiography').removeClass('hide');
    $(this).addClass('hide');
    $form.find('.label-primary').removeClass('label-primary').addClass('label-success');
  });

  $('#cancel-radiography').on('click', function() {
    var $form = $('#radiography-form');
    $form.find('.field-info').show();
    $form.find('.edit-info').addClass('hide');
    $('#save-radiography').addClass('hide');
    $('#edit-radiography').removeClass('hide');
    $(this).addClass('hide');
    $form.find('.label-success').removeClass('label-success').addClass('label-primary');
  });
});

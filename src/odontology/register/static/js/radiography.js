function save_radiography(id) {
    $btn_save = $('#save-radiography-'+id);
    $btn_edit = $('#edit-radiography-'+id);
    $btn_cancel = $('#cancel-radiography-'+id);
    $btn_save.button('loading');
    $btn_cancel.addClass('hide');
    $form = $('#radiography-form-'+id);
    form_name = 'radiography-form-'+id;
    var data_form = $form.serialize();
    var url = $form.attr('action');
    $.ajax({
      type: "POST",
      url: url,
      data: data_form,
      success: function(data) {
          if (data.status != 'ERROR') {
            $btn_save.button('reset').addClass('hide');
            $btn_edit.removeClass('hide');
            $btn_cancel.click();
            $form.find('.edit-info').each(function() {
              var value = $(this).find('select option:selected').val();
              var text = $(this).find('select option:selected').text();
              if (value != '') {
                $(this).prev().text(text);
              }
            });
            toastr.success('Datos de radiografia editados correctamente', 'RADIOGRAFIA EDITADA');
          } else {
            $btn_save.button('reset').addClass('hide');
            $btn_edit.removeClass('hide');
            validate_errors(form_name, data.errors, '');
            toastr.error('Hubo un error tratando de editar los datos.', 'DATOS ERRONEOS');
          }
      }
    });
}

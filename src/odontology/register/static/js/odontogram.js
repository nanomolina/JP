$(function() {
    $('#edit-odontogram').on('click', function() {
      $('#save-odontogram, #cancel-odontogram, #button-red, #button-blue, #select-work-type').removeClass('hide');
      $('.edit-odont').removeClass('hide');
      $('.field-odont').addClass('hide');
      $(this).addClass('hide');
    });

    $('#cancel-odontogram').on('click', function() {
      $('#save-odontogram, #button-red, #button-blue, #select-work-type').addClass('hide');
      $(this).addClass('hide');
      $('#edit-odontogram').removeClass('hide');
      $('#select-work-type select').selectpicker('val', '');
      $('.edit-odont').addClass('hide');
      $('.field-odont').removeClass('hide');
      clean_options();
    });

    $('#save-odontogram').on('click', function(event) {
        $('#save-odontogram').button('loading');
        $('#cancel-odontogram, #button-red, #button-blue, #select-work-type').addClass('hide');
        $('#select-work-type select').selectpicker('val', '');

        DATA_ODONT['teeth_works'] = JSON.stringify(TEETH_WORKS);
        DATA_ODONT['teeth_number'] = $('#id_teeth_number').val();
        DATA_ODONT['date_odontogram'] = $('#id_date_odontogram').val();
        DATA_ODONT['observations'] = $('#id_observations').val();
        $.ajax({
          type: "POST",
          url: URL_EDIT_ODONT,
          data: DATA_ODONT,
          success: function(data) {
              if (data.status === 'OK') {
                $('#save-odontogram').button('reset');
                $('#save-odontogram').addClass('hide');
                $('#edit-odontogram').removeClass('hide');
                $('polygon.sector-selected').removeClass('sector-selected');
                $('g.tooth.extraction').removeClass('extraction');
                $('#text-teeth').html($('#id_teeth_number').val());
                $('#text-observation').html($('#id_observations').val());
                $('.edit-odont').addClass('hide');
                $('.field-odont').removeClass('hide');
                $('#text-odontogram').text($('#id_date_odontogram').val());
                toastr.success('Los datos se han guardado correctamente.', 'ODONTOGRAMA MODIFICADO');
                console.log('OK---->');
              } else {
                console.log('error---->');
              }
          },
          dataType: "json",
        });
    });

    $('#date_odontogram').datetimepicker({
        viewMode: 'months',
        format: 'MMMM - YYYY',
        locale: 'es',
    });
    $('#id_date_odontogram').val(DATE_OD);
});

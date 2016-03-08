$(function() {
    $('#edit-odontogram').on('click', function() {
      $('#save-odontogram, #cancel-odontogram, #button-red, #button-blue, #select-work-type').removeClass('hide');
      $(this).addClass('hide');
    });

    $('#cancel-odontogram').on('click', function() {
      $('#save-odontogram, #button-red, #button-blue, #select-work-type').addClass('hide');
      $(this).addClass('hide');
      $('#edit-odontogram').removeClass('hide');
      $('#select-work-type select').selectpicker('val', '');
      clean_options();
    });

    $('#save-odontogram').on('click', function(event) {
        $('#save-odontogram').button('loading');
        $('#cancel-odontogram, #button-red, #button-blue, #select-work-type').addClass('hide');
        $('#select-work-type select').selectpicker('val', '');

        DATA_ODONT['extractions'] = JSON.stringify(extractions);
        DATA_ODONT['endodoncias'] = JSON.stringify(endodoncias);
        DATA_ODONT['restoration'] = JSON.stringify(restoration);
        DATA_ODONT['filtered_restoration'] = JSON.stringify(filtered_restoration);
        DATA_ODONT['caries'] = JSON.stringify(caries);
        DATA_ODONT['corona'] = JSON.stringify(corona);
        DATA_ODONT['eraser'] = JSON.stringify(eraser);
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
                console.log('OK---->');
              } else {
                console.log('error---->');
              }
          },
          dataType: "json",
        });
    });
});

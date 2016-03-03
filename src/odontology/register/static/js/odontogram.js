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
        clean_options();
        //--------datas----------
        var data = {'csrfmiddlewaretoken': CSRF};

        //--------CARIES---------
        var caries = []
        $('polygon.sector-selected').each(function(key){
            var sector = {'id': $(this).data('sector-id'), 'color': $(this).data('sector-color')};
            caries.push(sector);
        });
        data['caries'] = JSON.stringify(caries);

        //-------EXTRACTION------
        var extractions = []
        $('g.tooth.extraction').each(function(key){
            var tooth = {'id': $(this).data('tooth-id'), 'color': $(this).data('color')};
            extractions.push(tooth);
        });
        data['extractions'] = JSON.stringify(extractions);

        $.ajax({
          type: "POST",
          url: URL_EDIT_ODONT,
          data: data,
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

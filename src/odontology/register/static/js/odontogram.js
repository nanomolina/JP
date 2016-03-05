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
        //-------ENDODONCIA------
        var endodoncias = []
        $('g.tooth.endodoncia').each(function(key){
            var tooth = {'id': $(this).data('tooth-id'), 'color': $(this).data('color')};
            endodoncias.push(tooth);
        });
        data['endodoncias'] = JSON.stringify(endodoncias);

        //--------RESTORATION---------
        var restoration = []
        $('polygon.restoration').each(function(key){
            var sector = {'id': $(this).data('sector-id'), 'color': $(this).data('sector-color')};
            restoration.push(sector);
        });
        data['restoration'] = JSON.stringify(restoration);

        //--------RESTORATION---------
        var filtered_restoration = []
        $('polygon.filtered-restoration').each(function(key){
            var sector = {'id': $(this).data('sector-id'), 'color': $(this).data('sector-color')};
            filtered_restoration.push(sector);
        });
        data['filtered_restoration'] = JSON.stringify(filtered_restoration);

        //---------CORONA--------
        var corona = []
        $('g.tooth.corona').each(function(key){
            var tooth = {'id': $(this).data('tooth-id'), 'color': $(this).data('color')};
            corona.push(tooth);
        });
        data['corona'] = JSON.stringify(corona);

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

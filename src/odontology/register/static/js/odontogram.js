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
      clean_color_caries();
    });

    $('#save-odontogram').on('click', function(event) {
        $('#save-odontogram').button('loading');
        $('#cancel-odontogram, #button-red, #button-blue, #select-work-type').addClass('hide');
        $('#select-work-type select').selectpicker('val', '');
        clean_color_caries();        
        var data = {'csrfmiddlewaretoken': CSRF};
        var changes = []
        $('polygon.sector-selected').each(function(key){
            var sector_edition = {'id': $(this).data('sector-id'), 'color': $(this).data('sector-color')}
            changes.push(sector_edition);
        });
        data['sector_changes'] = JSON.stringify(changes)
        $.ajax({
          type: "POST",
          url: URL_EDIT_ODONT,
          data: data,
          success: function(data) {
              if (data.status === 'OK') {
                $('#save-odontogram').button('reset');
                $('#save-odontogram').addClass('hide');
                $('#edit-odontogram').removeClass('hide');
                console.log('OK---->');
              } else {
                console.log('error---->');
              }
          },
          dataType: "json",
        });
    });
});

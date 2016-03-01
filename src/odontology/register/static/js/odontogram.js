$(function() {
    $('#edit-odontogram').on('click', function() {
      $('#save-odontogram, #cancel-odontogram, #button-red, #button-blue').removeClass('hide');
      $(this).addClass('hide');
    });

    $('#cancel-odontogram').on('click', function() {
      $('#save-odontogram, #button-red, #button-blue').addClass('hide');
      $(this).addClass('hide');
      $('#edit-odontogram').removeClass('hide');
      $('polygon').off('mouseover');
      $('polygon').off('mouseout');
      $('polygon').off('click');
      $('polygon').css('cursor', 'auto');
    });

    $('#save-odontogram').on('click', function(event) {
        $('#save-odontogram').button('loading');
        $('#cancel-odontogram, #button-red, #button-blue').addClass('hide');
        var data = {'sector_changes': []};
        $('polygon.sector-selected').each(function(key){
            var sector_edition = {'id': $(this).data('sector-id'), 'color': $(this).data('sector-color')}
            data['sector_changes'].push(sector_edition);
        });
        var url = URL_EDIT_ODONT;
        $.ajax({
          type: "POST",
          url: url,
          data: data_form,
          success: function(data) {
              if (data.status === 'OK') {
                console.log('OK---->');
              } else {
                console.log('error---->');
              }
          }
        });
    });
});

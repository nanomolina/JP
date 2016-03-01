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

//-----------------------EXTRACTION --ENDODONCIA--CORONA-----------------------------------------
function generate_option(id, wt, type, my_class){
  $('g.tooth').mouseover(function (evt) {
      $('#'+id+' '+type).css('stroke', COLOR_SELECTED);
      $('#'+id+' '+type).css('cursor', 'pointer');
      var tooth = $(evt.target).parent();
      tooth.css('cursor', 'pointer');
      var pos = get_translation(tooth.attr('transform'));
      $('#'+id).attr('transform', 'translate('+pos[0]+', '+pos[1]+')');
      $('#'+id).removeClass('hide');
      $('#'+id).data('tooth-id', $(this).data('tooth-id'));
  });
  $('#'+id).mouseover(function(){
      $(this).removeClass('hide');
  })

  $('g.tooth').mouseout(function (evt) {
      $('#'+id).addClass('hide');
  });

  $('g.tooth').on('click', function (evt) {
      var tooth = $(evt.currentTarget);
      if (tooth.data('work-type') != wt) {
        $('#gmain').append($('#'+id).clone().attr('id', 'draw-'+tooth.data('tooth-id')));
        tooth.data('work-type', wt);
        tooth.data('color', COLOR_NAME);
        tooth.addClass(my_class);
        var data = {
            'id': tooth.data('tooth-id'),
            'color': tooth.data('color'),
            'type': wt,
        };
        TEETH_WORKS.push(data);
        if (wt == 1 && COLOR_NAME == 'red') {
            var teeth_count = $('#text-teeth').text();
            $('#text-teeth span').text(parseInt(teeth_count) - 1);
        }
      }
  });
  $('#'+id+' '+type).on('click', function(evt){
      // console.log($(this).parent().data('tooth-id'));
      var t_id = $(this).parent().data('tooth-id');
      var tooth = $("g").find("[data-tooth-id='" + t_id + "']");
      // console.log(tooth);
      tooth.click();
  });
}
//----------------------------END----------------------------------------------------------------

//------------------------------------RESTAURACION-----------------------------------------------
function option_restoration() {
    $('polygon').mouseover(function (evt) {
        var sector = $(evt.target);
        sector.css('cursor', 'pointer');
        sector.attr('fill', RED);
    });

    $('polygon').mouseout(function (evt) {
        var sector = $(evt.target);
        if (sector.data('sector-color') == 'red') {
          sector.attr('fill', RED);
        } else if (sector.data('sector-color') == 'blue') {
          sector.attr('fill', BLUE);
        } else {
          sector.attr('fill', WHITE);
        }
        sector.css('cursor', 'default');
    });

    $('polygon').click(function (evt) {
        var sector = $(evt.target);
        if (sector.data('sector-color') != 'red') {
            sector.addClass('sector-selected');
            sector.attr('fill', RED);
            sector.data('sector-color', 'red');
            sector.parent().data('work-type', 3);
            var data = {
              'id': sector.data('sector-id'),
              'color': sector.data('sector-color'),
              'type': 3,
            };
            TEETH_WORKS.push(data);
        }
    });
}
//----------------------------------------END----------------------------------------------------

//--------------------------RESTAURACION--FILTRADA  ---------------------------------------------
function option_filtered_restoration() {
    $('polygon').mouseover(function (evt) {
        var sector = $(evt.target);
        sector.css('cursor', 'pointer');
        sector.attr('fill', RED);
        sector.attr('stroke', BLUE);
        sector.attr('stroke-width', '1.5');
    });

    $('polygon').mouseout(function (evt) {
        var sector = $(evt.target);
        if (sector.data('sector-color') == 'red') {
          sector.attr('fill', RED);
        } else if (sector.data('sector-color') == 'blue') {
          sector.attr('fill', BLUE);
        } else {
          sector.attr('fill', WHITE);
        }
        if (sector.data('stroke-color') != 'blue') {
          sector.attr('stroke', GREY);
          sector.attr('stroke-width', '0.5');
        }
        sector.css('cursor', 'default');
    });

    $('polygon').click(function (evt) {
        var sector = $(evt.target);
        if (sector.data('stroke-color') != 'blue') {
            sector.addClass('filtered-restoration');
            sector.attr('fill', RED);
            sector.attr('stroke', BLUE);
            sector.attr('stroke-width', '1.5');
            sector.data('sector-color', 'red');
            sector.data('stroke-color', 'blue');
            sector.parent().data('work-type', 4);
            var data = {
                'id': sector.data('sector-id'),
                'color': sector.data('sector-color'),
                'type': 4,
            };
            TEETH_WORKS.push(data);
        }
    });
}
//----------------------------------------END----------------------------------------------------

//---------------------------CARIES--------------------------------------------------------------
function option_caries() {
    $('polygon').mouseover(function (evt) {
        var sector = $(evt.target);
        sector.css('cursor', 'pointer');
        sector.attr('fill', BLUE);
    });

    $('polygon').mouseout(function (evt) {
        var sector = $(evt.target);
        if (sector.data('sector-color') == 'red') {
          sector.attr('fill', RED);
        } else if (sector.data('sector-color') == 'blue') {
          sector.attr('fill', BLUE);
        } else {
          sector.attr('fill', WHITE);
        }
        sector.css('cursor', 'default');
    });

    $('polygon').click(function (evt) {
        var sector = $(evt.target);
        if (sector.data('sector-color') != 'blue') {
            sector.addClass('sector-selected');
            sector.attr('fill', BLUE);
            sector.data('sector-color', 'blue');
            sector.parent().data('work-type', 5);
            var data = {
              'id': sector.data('sector-id'),
              'color': sector.data('sector-color'),
              'type': 5,
            };
            TEETH_WORKS.push(data);
        }
    });
}
//-----------------------------END-CARIES-------------------------------------------------------

//----------------------------------------LIMPIAR-----------------------------------------------
function option_eraser() {
  $('g.tooth').mouseover(function (evt) {
      var tooth = $(evt.target).parent();
      if (tooth.data('work-type') != 'None') {
          tooth.css('cursor', 'pointer');
          tooth.find('polygon').each(function(key){
              $(this).attr('fill', WHITE);
              $(this).attr('stroke', GREY);
              $(this).attr('stroke-width', '0.5');
          });
          $('#draw-'+tooth.data('tooth-id')).hide();
          tooth.find('line, circle').addClass('hide');
      }
  });

  $('g.tooth').mouseout(function (evt) {
      var tooth = $(evt.target).parent();
      tooth.find('polygon').each(function(){
          if ($(this).data('sector-color') == 'red') {
            $(this).attr('fill', RED);
          } else if ($(this).data('sector-color') == 'blue') {
            $(this).attr('fill', BLUE);
          } else {
            $(this).attr('fill', WHITE);
          }
          if ($(this).data('stroke-blue') != 'True') {
            $(this).attr('stroke', GREY);
            $(this).attr('stroke-width', '0.5');
          } else {
            $(this).attr('stroke', BLUE);
            $(this).attr('stroke-width', '1.5');
          }
      });
      tooth.css('cursor', 'default');
      tooth.find('line, circle').removeClass('hide');
      $('#draw-'+tooth.data('tooth-id')).show();
  });

  $('g.tooth').on('click', function (evt) {
      var tooth = $(evt.target).parent();
      if (tooth.data('work-type') != 'None') {
          var blank = $('#PBlank');
          var num = tooth.find('text').html();
          tooth.html(blank.html());
          if (tooth.data('work-type') == 1 && tooth.data('color') == 'red') {
              var teeth_count = $('#text-teeth').text();
              $('#text-teeth span').text(parseInt(teeth_count) + 1);
          }
          tooth.attr('data-work-type', blank.attr('data-work-type'));
          tooth.attr('data-color', blank.attr('data-color'));
          tooth.find('text').html(num);
          $('#draw-'+tooth.data('tooth-id')).remove();
          var data = {
              'id': tooth.data('tooth-id'),
              'color': tooth.data('color'),
              'type': '',
          };
          TEETH_WORKS.push(data);
      }
  });
}

//----------------------------------------END----------------------------------------------------

//--------------------------BASE----------------------------------------------------------------
COLOR_SELECTED = 'rgba(0, 0, 255, 0.63)';
COLOR_NAME = 'blue';
RED = 'rgba(255, 0, 0, 0.63)';
BLUE = 'rgba(0, 0, 255, 0.63)';
WHITE = 'white';
GREY = '#555555';
DATA_ODONT = {'csrfmiddlewaretoken': CSRF}
TEETH_WORKS = [];

$('#button-red').on('click', function(){
    $('#button-blue').removeClass('active');
    COLOR_SELECTED = $(this).find('span').css('background-color');
    COLOR_NAME = $(this).find('span').data('color');
    $(this).addClass('active');
});
$('#button-blue').on('click', function(){
    $('#button-red').removeClass('active');
    COLOR_SELECTED = $(this).find('span').css('background-color');
    COLOR_NAME = $(this).find('span').data('color');
    $(this).addClass('active');
});


function get_translation(obj){
    obj = obj.split(', ');
    pos_x = obj[0].split('translate(')[1];
    pos_y = obj[1].split(')')[0];
    return [pos_x, pos_y];
}


function clean_options() {
    //--------CARIES------------------------
    $('polygon').off('mouseover');
    $('polygon').off('mouseout');
    $('polygon').off('click');

    //--------EXTRACTION--------------------
    $('g.tooth').off('mouseover');
    $('#tooth-extraction').off('mouseover');
    $('g.tooth').off('mouseout');
    $('g.tooth').off('click');
    $('#tooth-extraction line').off('click');
}

$('#select-work-type select').on('change', function(){
    var option = $('#select-work-type select option:selected').val();
    console.log('option '+option);

    clean_options();
    switch (option) {
      case '1':
        generate_option('tooth-extraction', 1, 'line', 'extraction');
        break;
      case '2':
        generate_option('tooth-endodoncia', 2, 'line', 'endodoncia');
        break;
      case '3':
        option_restoration();
        break;
      case '4':
        option_filtered_restoration();
        break;
      case '5':
        option_caries();
        break;
      case '6':
        generate_option('tooth-corona', 6, 'circle', 'corona');
        break;
      case '7':
        option_eraser();
        break;
    }
});

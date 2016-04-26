function init_paginator(){
  var $nodes = $('#pagination').find('li').not('.disabled, .active').find('a');
  $nodes.each(function(index){
      href = $(this).attr('href');
      $(this).attr('href', 'javascript: load_page("'+href+'");');
  });
}

$(document).ready(function(){
    $('#text_search').keypress(function( event ) {
        if ( event.which == 13 ) {
           event.preventDefault();
           $(this).next().click();
        }
    })
    init_paginator();
});

function loading_state() {
    var $body = $('#body-list-patients');
    $body.find('tr').hide();
    $body.find('#loading').show().removeClass('hide');
}


function load_page(href) {
  loading_state();
  var url = href;
  $('#list-patients').find('.panel-body').load(url, function(){
    init_paginator();
  });
}

function search() {
    loading_state();
    var url = $('#filter').attr('action');
    var data = $('#filter').serialize();
    $('#list-patients').find('.panel-body').load(url, data);
}

function load_delete_modal(url) {
  var $modal = $('#modal-delete');
  $modal.modal('show');
  $modal.find('#btn-delete').attr('href', 'javascript: delete_patient("'+url+'")');
}

function delete_patient(url) {
  var $modal = $('#modal-delete');
  $modal.find('#btn-delete').button('loading');
  $.ajax({
    type: "POST",
    url: url,
    data: $('#csrf_token').serialize(),
    success: function(data) {
        if (data.status !== 'ERROR') {
          $('#tbody-record').html(data);
          $('#modal-delete').modal('hide');
          $('.rec-popover').popover();
          toastr.success('Se ah borrado exitosamente.', 'REGISTRO BORRADO');
        } else {
          toastr.error('', 'ERROR AL BORRAR');
        }
        $('#modal-delete').find('#btn-delete').button('reset');
    }

  });
}

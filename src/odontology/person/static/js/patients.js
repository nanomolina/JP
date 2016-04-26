function search() {
    var url = $('#filter').attr('action');
    var data = $('#filter').serialize();
    var $body = $('#body-list-patients');
    $body.find('tr').hide();
    $body.find('#loading').show().removeClass('hide');
    $body.load(url, data);
}

$(function() {
    $('#text_search').keypress(function( event ) {
        if ( event.which == 13 ) {
           event.preventDefault();
           $(this).next().click();
        }
    })
});

function paginator(page) {
    var $body = $('#body-list-patients');
    $body.find('tr').hide();
    $body.find('#loading').show().removeClass('hide');
    var $pagination = $('#pagination')
    $pagination.load(
        URL_PAGINATOR,
        {'page': page, 'csrfmiddlewaretoken': CSRF, 'type': 2}
    );
    $body.load(
        URL_PAGINATOR,
        {'page': page, 'csrfmiddlewaretoken': CSRF, 'type': 1}
    );
}

function load_delete_modal(url) {
  var $modal = $('#modal-delete');
  $modal.modal('show');
  $modal.find('#btn-delete').attr('href', 'javascript: delete_patient("'+url+'")');
}

function delete_patient(url) {
  
}

function search() {
    var url = $('#filter').attr('action');
    var data = $('#filter').serialize();
    var $body = $('#body-list-patients');
    $body.find('tr').hide();
    $body.find('#loading').show().removeClass('hide')
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

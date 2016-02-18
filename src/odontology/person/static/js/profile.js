function edit_benefit_detail(id) {
  var $row_detail = $('#bf-detail-'+id);
  $row_detail.find('.edit').removeClass('hide');
  $row_detail.find('.detail-info').addClass('hide');
  var $edit_button = $('#bf-detail-edit-'+id);
  $edit_button.addClass('hide');
  var $save_button = $('#bf-detail-save-'+id);
  $save_button.removeClass('hide');
}

$(function () {
    $('.day-picker').datetimepicker({
        viewMode: 'days',
        format: 'D',
        locale: 'es',
    });
});

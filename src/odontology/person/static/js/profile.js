function edit_benefit_detail(id) {
    var $row_detail = $('#bf-detail-'+id);
    $row_detail.find('.edit').removeClass('hide');
    $row_detail.find('.detail-info').addClass('hide');
    var $edit_button = $('#bf-detail-edit-'+id);
    $edit_button.addClass('hide');
    var $save_button = $('#bf-detail-save-'+id);
    $save_button.removeClass('hide');
}

function getMonthDateRange(year, month) {
    var startDate = moment([year, month - 1]);
    var endDate = moment(startDate).endOf('month');
    // console.log(startDate.toDate());
    // console.log(endDate.toDate());
    return { start: startDate, end: endDate };
}

function getMonthDateRange(year, month) {
    var startDate = moment([year, month - 1]);
    var endDate = moment(startDate).endOf('month');
    // console.log(startDate.toDate());
    // console.log(endDate.toDate());
    return { start: startDate, end: endDate };
}

$(function() {
  $('#tab-info a, #tab-detail a, #tab-odontogram a').click(function (e) {
    $(this).tab('show');
  });
  $('#tab-total-detail a').click(function(e) {
    $('#total-detail').load(URL_ACC_BF, function(){
      $('#tab-total-detail a').tab('show');
    });
  });
});

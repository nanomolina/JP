function getMonthDateRange(year, month) {
    var startDate = moment([year, month - 1]);
    var endDate = moment(startDate).endOf('month');
    // console.log(startDate.toDate());
    // console.log(endDate.toDate());
    return { start: startDate, end: endDate };
}

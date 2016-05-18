function edit_account(record_id) {
    var $acc = $('#account-'+record_id);
    $acc.find('.field-info').addClass('hide');
    $acc.find('.edit-info').removeClass('hide');
    $('#btn-acc-edit-'+record_id).addClass('hide');
    $('#btn-acc-save-'+record_id).removeClass('hide');
}

function save_account(record_id) {
    var $acc = $('#account-'+record_id);
    var data = $acc.find('input').serialize();
    $.ajax({
      type: 'POST',
      url: $acc.data('url'),
      data: data,
      success: function(data) {
          if (data.status == 'OK') {
            var $acc = $('#account-'+record_id);
            $acc.find('.debit').html(data.debit);
            $acc.find('.havings').html(data.havings);
            $acc.find('.balance').html(data.balance);

            var $acc_total = $('#account-total');
            $acc_total.find('.debit').html(data.total_debit);
            $acc_total.find('.havings').html(data.total_havings);
            $acc_total.find('.balance').html(data.total_balance);

            $acc.find('.field-info').removeClass('hide');
            $acc.find('.edit-info').addClass('hide');
            $('#btn-acc-edit-'+record_id).removeClass('hide');
            $('#btn-acc-save-'+record_id).addClass('hide');
          } else {
            var $acc = $('#account-'+record_id);
            for (var key in data.errors) {
                $acc.find('.'+key).next().addClass('has-error');
            }
          }
      }
    })
}

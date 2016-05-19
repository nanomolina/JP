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
            $acc.find('.debit').html('$ '+data.debit);
            $acc.find('.havings').html('$ '+data.havings);
            var $balance = $acc.find('.balance');
            $balance.html('$ '+data.balance);
            if (data.balance.replace(',', '.') < 0) {
              $balance.css('color', 'crimson');
            } else {
              $balance.css('color', '');
            }


            var $acc_total = $('#account-total');
            $acc_total.find('.debit').html('$ '+data.total_debit);
            $acc_total.find('.havings').html('$ '+data.total_havings);
            var $total_balance = $acc_total.find('.balance');
            $total_balance.html('$ '+data.total_balance);
            if (data.total_balance.replace(',', '.') < 0) {
              $total_balance.css('color', 'crimson');
            } else {
              $total_balance.css('color', '');
            }

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

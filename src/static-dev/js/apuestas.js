function open_modal_register(){
  $('#modal_register').modal('show');
}

function cancel_modal_register(){
  $('#modal_register').find('#id_username').val('');
  $('#modal_register').find('#id_password1').val('');
  $('#modal_register').find('#id_password2').val('');
  $('#modal_register').modal('hide');
}

function send_register_form(){
  $.each('.is-invalid', function(index, objects_i){
      $('#id_' + objects_i[0].removeClass('is-invalid'));
  })
  $.ajax({
    type: "POST",
    url: $('#id_form_register').attr('action'),
    data: $('#id_form_register').serialize(),
    success: function(response){
      if (response.status == 'ok'){
        alert('Congratulaciones')
      }
      else{
        $.each(response.errors, function(index, objects_i){
            $('#id_' + objects_i[0].addClass('is-invalid'));
        })
      }
    }
  })
}

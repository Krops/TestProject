$(document).ready(function () {
$(document).on('hidden.bs.modal', function (e) {
    $(e.target).removeData('bs.modal').find(".modal-content").html('');
});
jQuery('#modal').on('shown.bs.modal',
    function(e) 
    {
        if(document.getElementById('loggout_content')){
            document.getElementById('logtit').innerHTML = 'Login as: Anon';
            document.getElementById('authbut').innerHTML = 'Login';
            $('#authbut').attr('href','/login/');
            $('#authbut').attr('title','Login');
        }
    });
    var options = {

        beforeSend: function(form, options) {
            setTimeout(function() {
                    $("#success").hide();
                    $("#warning").hide();
                    $("#fail").hide();
                    $("#in_progress").fadeIn(300);
                    $('.modal-body').attr("disabled","enabled");
                    $('.modal-footer').attr("disabled","enabled");

         },
                300)
        },

        success: function(responseText) {
            setTimeout(function() {
                    $('.modal-body').removeAttr("disabled");
                    $('.modal-footer').removeAttr("disabled");
                   if (responseText['login'] == true) {
                        $("#in_progress").hide();
                        $("#fail").hide();
                        $("#success").fadeIn(1000);
                        document.getElementById('logtit').innerHTML = 'Login as: ' +responseText['username'];
                        document.getElementById('authbut').innerHTML = 'Logout';
                        $('#authbut').attr('title','Logout');
                        $('#authbut').attr('href','/logout/');
                        setTimeout(function () {
                        jQuery('#modal').modal('hide');
                        $("#success").hide();
                        $("#warning").show();
                    }, 1000);
                        
                    }else {
                        $("#success").hide();
                        $('#in_progress').hide();
                        document.getElementById('fail').innerHTML = responseText['errors'];
                        $("#fail").fadeIn(1000);
                    }
                },
                1000)
        },

         error:  function(xhr, str){
             $("#success").hide();
             $('#in_progress').hide();
             $("#fail").fadeIn(1000);
             $('.modal-body').removeAttr("disabled");
            $('.modal-footer').removeAttr("disabled");
            }
        };
    jQuery('#login_form').ajaxForm(options);
});
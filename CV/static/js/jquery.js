
function display_error(type_error) {
    $('#tchat').append('<div id="avatar2"></div><br><br>' + '<reponse>' + "Je n'ai pas compris, réessayez "
        + '</reponse>');
    $("#fontchat").animate({ scrollTop: $("#tchat").height() }, 1000); }


$(function() {
    $('#msg_id').keypress(function(e) {
        var key = e.which;
        if (key == 13) {
            $('#boutenvoyer').click();
            return false;
        }
    });
    $('#boutenvoyer').click(function() {
        $('#alert').css("display", "none");
        var msg = '<img src="https://img.icons8.com/bubbles/60/000000/user-male.png"/>' + '<br><msg>' +
            $('#msg_id').val() + '</msg>';
        var request = $('input');
        if ($('#input_form').val() == '') {
            return;
        }
        $('#tchat').append(msg);
        $('#contain_loader').css("display", "block");
        $.ajax({
            url: '/get_user_request',
            data: $(request).serialize(),
            type: 'GET',
            success: function (response) {
                $('#contain_loader').css("display", "none");
                $("#fontchat").animate({scrollTop: $("#tchat").height()}, 2000);
                var response_json = JSON.parse(response);
                var type = response_json['type_search'];
                var prenom = response_json['name'];
                if (type == 'name' ) {
                    $('#tchat').append('<br><div id="avatar2"></div>' + '<reponse>' + 'Enchanté ' +
                        prenom + "&nbsp;!&nbsp;" + (response_json['nice']) + '</reponse>');
                    $("#fontchat").animate({scrollTop: $("#tchat").height()}, 2000);
                }
                else {
                    $('#tchat').append('<br><div id="avatar2"></div>' + '<reponse>' +
                        (response_json['resp']) + '</reponse>');
                    $("#fontchat").animate({scrollTop: $("#tchat").height()}, 2000);
                }
            },
            error: function (error) {
                $('#contain_loader').css("display", "none");
                display_error();
            }
        });
    });
});
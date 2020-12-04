
function display_error(type_error) {
    $('#tchat').append('<div id="avatar2"></div><br><br>' + '<reponse>' + "Je n'ai pas compris, réessayez "
        + '</reponse>');
    $("#fontchat").animate({ scrollTop: $("#tchat").height() }, 1000); }


$(function() {
    $('#boutenvoyer').click(function() {
        $('#alert').css("display", "none");
        var msg = '<img src="https://img.icons8.com/officel/40/000000/user.png" style="margin:10px"/>' + '<br><msg>' +
            $('#msg_id').val() + '</msg><br><br>';
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
                $("#fontchat").animate({scrollTop: $("#tchat").height()}, 1000);
                var response_json = JSON.parse(response);
                var type = response_json['type_search'];
                var prenom = response_json['name'];
                var info = response_json['information'];
                if (type == 'son profil' || type == 'son expérience' || type == 'sa formation' || type == 'ses skills') {
                    $('#tchat').append('<div id="avatar2"></div><br><br>' + '<reponse>' +
                        (response_json['sentance_type']) + type +'</reponse><reponse>' +
                        (response_json['ask_for_name']) + '</reponse>');
                    $("#fontchat").animate({scrollTop: $("#tchat").height()}, 1000);
                }
                else if (type == 'name' ) {
                    $('#tchat').append('<div id="avatar2"></div><br><br>' + '<reponse>' + 'Enchanté ' +
                        prenom + "&nbsp;!&nbsp;" + (response_json['nice']) + '</reponse>');
                    $("#fontchat").animate({scrollTop: $("#tchat").height()}, 1000);
                }
                else {
                    $('#tchat').append('<div id="avatar2"></div><br><br>' + '<reponse>' +
                        (response_json['sentance_type']) + info + response_json['resp'] + '</reponse>');
                    $("#fontchat").animate({scrollTop: $("#tchat").height()}, 1000);
                }
            },
            error: function (error) {
                $('#contain_loader').css("display", "none");
                display_error();
            }
        });
    });
    $('#msg_id').keypress(function(e) {
        var key = e.which;
        if (key == 13) // the enter key code
        {
            $('#boutenvoyer').click();
            return false;
        }
    });
});
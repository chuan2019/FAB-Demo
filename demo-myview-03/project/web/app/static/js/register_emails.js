
function ajaxDelete(del_url) {
    var email_address = $("#email_address").val();
    $.ajax({
        type: 'DELETE',
        url: del_url,
        success: function(result) {
            $("#email_address").val('');
            alert(email_address + ' is unregistered!');
        },
        error: function(result) {
            $("#email_address").val('');
            alert(result.responseJSON["message"]);
        }
    });
}

$(document).ready(function() {
    $("#register").click(function(event) {
        event.preventDefault();
        var email_address = $("#email_address").val();
        $.ajax({
            type: 'POST',
            url: '/api/v1/recipients/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'email_address': $("#email_address").val()
            }),
            success: function(result) {
                $("#email_address").val('');
                alert(email_address + ' is registered!');
            },
            error: function(result) {
                $("#email_address").val('');
                alert(result.responseJSON["message"]);
            }
        });
    });

    $("#unregister").click(function() {
        var email_address = $("#email_address").val();
        $.ajax({
            type: 'GET',
            url: '/api/v1/recipients/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                'email_address': $("#email_address").val()
            }),
            success: function(result) {
                console.log(result.result);
                console.log(result.ids);
                var found = false;
                var id = 0;
                for (var i = 0; i < result.count; i++) {
                    if (result.result[i]['email_address'] == email_address) {
                        id = result.ids[i];
                        var url = '/api/v1/recipients/' + id.toString();
                        console.log(id, "::", email_address);
                        console.log(url);
                        ajaxDelete(url);
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    $("#email_address").val('');
                    alert("Error: " + email_address + " not found!");
                }
            },
            error: function(result) {
                $("#email_address").val('');
                alert(result.responseJSON["message"]);
            }
        });
    });
});

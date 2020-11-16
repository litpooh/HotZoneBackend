function generateJson() {
    var virusJson = {};
    virusJson["name"] = $("#name").val();
    virusJson["commonName"] = $("#commonName").val();
    virusJson["maxInfectiousPeriod"] = $("#maxInfectiousPeriod").val();
    console.log((virusJson));
    return JSON.stringify(virusJson);
}

$(document).ready(function() {
    $("#createButton").on('click', function() {
        var virusData = generateJson();
        // console.log(virusData);
        $.ajax({
            type: "POST",
            url: "/post_create_virus/",
            data: virusData,
            dataType: "json",
            contentType: "application/json;charset=utf-8",
            success: function(result) {
                console.log(result);
                $("#createStatus").text("Virus Record Added!");
                $("#createVirusForm")[0].reset();
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status, errmsg, err);
                $('#createStatus').text(errmsg);

            }
        });
    })
});

function resetForm() {
    $("#createVirusForm")[0].reset();
}
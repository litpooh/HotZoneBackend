function getFormData($form) {
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};
    $.map(unindexed_array, function(n, i) {
        indexed_array[n['name']] = n['value'];
    });
    return indexed_array;
}

function generateJson() {
    var p = {};
    p["name"] = $("#name").val();
    p["idNumber"] = $("#idNumber").val();
    p["dateOfBirth"] = $("#dateOfBirth").val();
    var caseJson = {};
    caseJson["patient"] = p;
    caseJson["virus"] = $("#virus_input").val();
    caseJson["dateOfConfirm"] = $("#dateOfConfirm").val();
    caseJson["localOrImported"] = $('input[name=localOrImported]:checked', "#createCaseForm").val();
    console.log((caseJson));
    return JSON.stringify(caseJson);
}

$(document).ready(function() {
    $("#createButton").on('click', function() {
        // var caseData = getFormData($("#createCaseForm"));
        var caseData = generateJson();
        console.log(caseData);
        $.ajax({
            type: "POST",
            url: "/post_caserecord/",
            data: caseData,
            dataType: "json",
            contentType: "application/json;charset=utf-8",
            success: function(result) {
                console.log(result);
                $("#createStatus").text("Case Record Added!");
                $("#createCaseForm")[0].reset();
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status, errmsg, err);
                $('#createStatus').text(errmsg);

            }
        });
    })
});
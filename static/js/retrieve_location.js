var retrievedResult;

function retrieve() {
    $.ajax({
        type: "GET",
        dataType: "json",
        crossDomain: true,
        url: "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=",
        data: $("#location").serialize(),
        success: function(result) {
            console.log(result);
            retrievedResult = result;
            $("#retrieveStatus").text("Retrieved Success!");
            updateResult();
            $('#confirmButton').attr("disabled", false);
            if (result.resultCode == 200) {
                alert("SUCCESS");
            };
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown);
            $("#locationRadio").text("");
            $("#retrieveStatus").text("Retrieved Falied!");
        }
    })
}

function retrieve_fake() {
    console.log($("#retrieveFrom").serialize());
    console.log();
}

function updateResult() {
    var rLocation = "";
    $.each(retrievedResult, function(i, val) {
        cleanJsonKey(val);
        rLocation += '<input type="radio" id="text' + i + '"name="location" value=' + "'" + JSON.stringify(val) + "'" + '><label for="text' + i + '">' + val.name + '<br>(' + val.address + ')</label><br><br>'
    });
    $("#locationRadio").html(rLocation);
}

$(document).ready(function() {
    $("#confirmButton").on('click', function() {
        var vlData = generateJson();
        $.ajax({
            type: "POST",
            url: "/create_visitedlocation_post/",
            data: vlData,
            dataType: "json",
            contentType: "application/json;charset=utf-8",
            success: function(result) {
                console.log(result);
                $("#confirmStatus").text("Location Added!");
                $("#addLocationForm")[0].reset();
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status, errmsg, err);
                $('#confirmStatus').text(errmsg);

            }
        });
    })
});

function displayLocations() {
    console.log($("#addLocationForm"));
}

function renameKey(obj, oldKey, newKey) {
    obj[newKey] = obj[oldKey];
    delete obj[oldKey];
}

function cleanJsonKey(obj) {
    renameKey(obj, "nameEN", "name");
    renameKey(obj, "addressEN", "address");
    renameKey(obj, "x", "xcoord");
    renameKey(obj, "y", "ycoord");
    delete obj["addressZH"];
    delete obj["nameZH"];
}

function checkSelectedLocation() {
    var radios = document.getElementsByName('location');

    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            console.log(JSON.parse(radios[i].value));
            break;
        }
    }
}

function simulatePOSTfrom() {
    var formData = JSON.stringify($("#addLocationForm").serializeArray());
    console.log(formData);
}

function generateLocationJson() {
    var radios = document.getElementsByName('location');

    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            return JSON.parse(radios[i].value);
        }
    }
}

function checkCaseID() {
    console.log($("#caseID").text());
}

function generateJson() {
    var lv = {};
    lv["location"] = generateLocationJson();
    lv["dateFrom"] = $("#dateFrom").val();
    lv["dateTo"] = $("#dateTo").val();
    lv["caseID"] = $("#caseID").text();
    lv["category"] = $('input[name=category]:checked', "#addLocationForm").val();
    console.log(lv);
    return JSON.stringify(lv);
}
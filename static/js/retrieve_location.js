var retrievedResult;

function retrieve() {
    $.ajax({
        type: "POST",
        dataType: "json",
        crossDomain: true,
        url: "../search_location_post/",
        data: retrievedata(),
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

function retrievedata(){
    return {'keyword': $("#location").val()};
}

function retrieve_fake() {
    console.log($("#retrieveFrom").serialize());
    console.log();
}

function updateResult() {
    var table = $('#locationTable').DataTable();
    table.clear();
    $.each(retrievedResult, function(i, val) {
        cleanJsonKey(val);
        table.row.add([val.name,val.address,val.xcoord,val.ycoord]).draw( false );;
    });
}

$(document).ready(function() {
    var table = $('#locationTable').DataTable(
        {
            "scrollY":        "500px",
            "scrollCollapse": true,
            "paging":         false,
            "searching": false,
            "aaSorting": [],
            "ordering": false
        }
    );

    $('#locationTable tbody').on( 'click', 'tr', function () {
        if ( $(this).hasClass('selected') ) {
            $(this).removeClass('selected');
        }
        else {
            table.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
        }
    } );

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
    var table = $('#locationTable').DataTable();
    var tmp = table.row('.selected').data();
    var tmpobj = {'name':tmp[0], 'address':tmp[1], 'xcoord': tmp[2], 'ycoord':tmp[3]};
    return tmpobj;
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
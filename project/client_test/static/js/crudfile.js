$(document).ready(function(){

        bindEvents();

        if(localStorage.getItem("Status"))
        {
            $("#Message").addClass("alert alert-success");
            $("#Message").html("User Added Successfully.");
            localStorage.clear();
        }
        if(localStorage.getItem("DeleteStatus"))
        {
            $("#Message").addClass("alert alert-success");
            $("#Message").html("User Deleted Successfully.");
            localStorage.clear();
        }
        if(localStorage.getItem("UpdateStatus"))
        {
            $("#Message").addClass("alert alert-success");
            $("#Message").html("User Updated Successfully.");
            localStorage.clear();

        }
});

function bindEvents(){


        $('[data-toggle="tooltip"]').tooltip();
        $("#myTable").tablesorter();
        $("table th").addClass("headerSortUp");


//        $( function() {
//            $( "#datepicker" ).datepicker({
//
//            });
//        } );

        $("a").on("click", function(event){


            var getId = $(this).attr("id");
            if(getId == "js-deleteUser"){

                deleteUser($(this));

            }
            else if(getId == "js-add-button"){

                addUpdateUser($(this),getId);

            }
            else if(getId == "js-editUser"){

                addUpdateUser($(this),getId);

            }
        });

}


function deleteUser(object){

    console.log(object);
    var url = object.attr("href");
    var pk = object.attr("data-value");
    var ans = confirm("Are you sure you want to delete !");
    if (ans == true) {
        $.ajax({
            url: url,
            type: 'delete',
            success: function(data){

                localStorage.setItem("DeleteStatus","True")
                location.reload();

            },
            error: function(error){

                console.log("e",error);

            }
        });
    }

}

function addUpdateUser(object, id){

    console.log(object);
    var modalName = "";
    var url = "";
    var title="";
    $.ajax({
        url: object.attr("href"),
        type: 'get',
        dataType: 'json',
        success: function(data){

            if(id == "js-add-button"){

                title = "Add User";
                modalName = "#myModal";
                url = $("#myForm").attr("data-action");

            }
            else{

                title = "Update User";
                modalName = "#myModalUpdate";
                url = $("#myForm").attr("data-action-update");

            }

            $(modalName + " .modal-dialog").html(data['html_form']);
            $("h4").html(title);


            //$("#myForm").on("submit", function(event){
            $(document).on("submit", "#myForm", function(event){
                event.preventDefault();
                var form = $("#myForm");
                if(id == "js-add-button"){

                    url = $("#myForm").attr("data-action");

                }
                else{

                    url = $("#myForm").attr("data-action-update");

                }

                $.ajax({
                    url: url,
                    type: 'post',
                    data: form.serialize(),
                    dataType: 'json',
                    success: function(data){



                        if(data['form_is_valid'] = "false")
                        {

                            $(modalName + " .modal-dialog").html(data['html_form']);

                        }
                    },
                    error: function(error){

                        console.log("form error",error);

                        if(error.status == 200)
                        {
                            if(modalName == "#myModal"){
                               localStorage.setItem("Status","True");
                               location.reload();
                            }
                            else{
                                localStorage.setItem("UpdateStatus","True");
                                location.reload();
                            }

                        }
                        else
                        {
                            $("#Message").addClass("alert alert-danger");
                            $("#Message").html(error.responseText);
                        }
                    }
                });
            });



        },
        error: function(error){
            $("#Message").addClass("alert alert-danger");
            $("#Message").html(error.responseText);
        }
    });

}



if(typeof $('#id_country').val() !== 'undefined'){

    getCountryChainedDropDownValues();

}

$(document).on('change', '#id_country', function(){


    getCountryChainedDropDownValues();

});


function getCountryChainedDropDownValues()
{
    var country = $('#id_country').val();
    $.ajax({
            url: $('#id_country').attr("data-get-state"),
            type: 'get',
            data: {'country':country},
            dataType: 'json',
            success: function(data){
                console.log(data);
            },
            error: function(error){

                console.log(error);

                if(error.status == 200){

                    $('#id_state').html(error.responseText);

                    $(document).on('change', '#id_state', function(){
                        var state = $('#id_state').val();
                        $.ajax({
                            url: $('#id_country').attr("data-get-city"),
                            type: 'get',
                            data: {'state':state},
                            dataType: 'json',
                            success: function(data){
                                console.log(data);
                            },
                            error: function(error){
                                console.log(error);
                                if(error.status==200){
                                    $('#id_city').html(error.responseText);
                                }
                                else {
                                    $("#Message").addClass("alert alert-danger");
                                    $('#Message').html(error.responseText);
                                }
                            }
                        });
                    });
                }

            }
    });
}






//$(document).on("click", '.js-add-button', function(event){

/*    $.ajax({
        url: $(this).attr("href"),
        type: 'get',
        dataType: 'json',
        success: function(data){

            $("#myModal .modal-dialog").html(data['html_form'])

            $("#myForm").on("submit", function(event){
                event.preventDefault();
                var form = $("#myForm");
                console.log("form",form);
                $.ajax({
                    url: $("#myForm").attr("data-action"),
                    type: 'post',
                    data: form.serialize(),
                    dataType: 'json',
                    success: function(data){

                        if(data['form_is_valid'] = "false")
                        {
                            console.log("form data",data);
                            $("#myModal .modal-dialog").html(data['html_form'])

                        }
                    },
                    error: function(error){

                        console.log("form error",error);

                        if(error.status == 200)
                        {
                           localStorage.setItem("Status","True")
                           location.reload();

                        }
                        else
                        {
                            $("#Message").addClass("alert alert-danger");
                            $("#Message").html(error.responseText);
                        }
                    }
                });
            });



        },
        error: function(error){
            $("#Message").addClass("alert alert-danger");
            $("#Message").html(error.responseText);
        }
    });*/
//});

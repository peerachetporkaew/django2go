var current_page = 1;

function next_page(){
    load_data(current_page + 1);
}

function previous_page(){
    if (current_page > 1)
        load_data(current_page - 1);
    else
        alert("This is the first page.");
}

function search_pattern(e){
    $.get("/app_chunking/function_word/search_text/",{pattern : $(e).html()},
        function(data){
            var output = getResponse(data);
            $("#search_result").html(output);
        }
    );
}

function load_data(pageno){
    $.get("/app_chunking/function_word/load_word_list/",{page : pageno},
        function(data){
            var output = getResponse(data);
            var result = "";
            for(var i=0; i < output.length; i++){
                result += "<span style='text-decoration:underline; cursor : pointer;' onclick='search_pattern(this);'>" + output[i] + "</span><br/>";
            }
            $("#word_list").html(result);
            current_page = pageno;
        }
    );
}

$(document).ready(
    function (){
        load_data(1);
    }
);
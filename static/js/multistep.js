$(document).ready(function () {
    // swith on the progrss bar here.
    $.get("/source_plag/multistep/",
        {'step': 'pre_process'},
        function (resp) {
            /* the first step in the multistep process is ok, now for the second one */
            console.log('1');
            $.get("/source_plag/multistep", {'step': 'ngram'},
                function (resp) {
                    $("#ngram").html(resp.result);

                    //chain the third request

                    /// inside that function chain the fourth.

                    // last chained item., switch off the progress bar
                });
        });

});
console.log("0");
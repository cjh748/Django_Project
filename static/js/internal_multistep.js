i = 2;
$(document).ready(function () {
    $.get("/internal_plag/multistep/", {'step': 'pre_process'}, function (resp) {
        $.get("/internal_plag/multistep", {'step': 'ngram'}, function (resp) {
            $("#ngram").html(resp.result);

            progress();

            $.get("/internal_plag/multistep/", {'step': 'pre_process_tfidf'}, function (resp) {
                $.get("/internal_plag/multistep", {'step': 'tfidf'}, function (resp) {
                    $("#tfidf").html(resp.tfidf_result);

                    progress();

                    $.get("/internal_plag/multistep/", {'step': 'pre_process_wordnet'}, function (resp) {
                        $.get("/internal_plag/multistep", {'step': 'wordnet'}, function (resp) {
                            $("#wordnet").html(resp.wordnet_result);

                            progress();

                            $.get("/internal_plag/multistep/", {'step': 'pre_process_lcs'}, function (resp) {
                                $.get("/internal_plag/multistep", {'step': 'lcs'}, function (resp) {
                                    $("#lcs").html(resp.lcs_result);

                                    progress();
                                });
                            });
                        });
                    });
                });
            });
        });
    });

    function progress() {
        var progress_number = i * 12.5;
        document.getElementById("progress").style.width = progress_number + "%";
        i += 2
    }
});


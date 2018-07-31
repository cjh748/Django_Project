$(document).ready(function () {
    // swith on the progrss bar here.
    $.get("/source_plag/multistep/", {'step': 'pre_process'}, function (resp) {
        $.get("/source_plag/multistep", {'step': 'ngram'}, function (resp) {
            $("#ngram").html(resp.result);

            $.get("/source_plag/multistep/", {'step': 'pre_process_tfidf'}, function (resp) {
                $.get("/source_plag/multistep", {'step': 'tfidf'}, function (resp) {
                    $("#tfidf").html(resp.tfidf_result);

                    $.get("/source_plag/multistep/", {'step': 'pre_process_wordnet'}, function (resp) {
                        $.get("/source_plag/multistep", {'step': 'wordnet'}, function (resp) {
                            $("#wordnet").html(resp.wordnet_result);

                            $.get("/source_plag/multistep/", {'step': 'pre_process_lcs'}, function (resp) {
                                $.get("/source_plag/multistep", {'step': 'lcs'}, function (resp) {
                                    $("#lcs").html(resp.lcs_result);


                                    //chain the third request

                                    /// inside that function chain the fourth.

                                    // last chained item., switch off the progress bar
                                });
                            });
                        });
                    });
                });
            });
        });
    });
});
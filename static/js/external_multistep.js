i = 2;
$(document).ready(function () {
    $.get("/external_plag/multistep/", {'step': 'pre_process'}, function (resp) {
        $.get("/external_plag/multistep", {'step': 'ngram_oop'}, function (resp) {
            $("#ngram_oop").html(resp.result_oop);
            $.get("/external_plag/multistep", {'step': 'ngram_pagerank'}, function (resp) {
                $("#ngram_pagerank").html(resp.result_pagerank);
                $.get("/external_plag/multistep", {'step': 'ngram_vector'}, function (resp) {
                    $("#ngram_vector").html(resp.result_vector);
                    $.get("/external_plag/multistep", {'step': 'ngram_bayes'}, function (resp) {
                        $("#ngram_bayes").html(resp.result_bayes);
                        $.get("/external_plag/multistep", {'step': 'ngram_dynamic'}, function (resp) {
                            $("#ngram_dynamic").html(resp.result_dynamic);

                            progress();

                            $.get("/external_plag/multistep/", {'step': 'pre_process_tfidf'}, function (resp) {
                                $.get("/external_plag/multistep", {'step': 'tfidf'}, function (resp) {
                                    $("#tfidf-ext").html(resp.tfidf_result);

                                    progress();

                                    $.get("/external_plag/multistep/", {'step': 'pre_process_wordnet'}, function (resp) {
                                        $.get("/external_plag/multistep", {'step': 'wordnet'}, function (resp) {
                                            $("#wordnet-ext").html(resp.wordnet_result);

                                            progress();

                                            $.get("/external_plag/multistep/", {'step': 'pre_process_lcs'}, function (resp) {
                                                $.get("/external_plag/multistep", {'step': 'lcs-substring'}, function (resp) {
                                                    $("#lcs-string").html(resp.lcs_result);

                                                    $.get("/external_plag/multistep", {'step': 'lcs-subsequence'}, function (resp) {
                                                        $("#lcs-sequence").html(resp.lcs_result);

                                                        progress();

                                                    });
                                                });
                                            });
                                        });
                                    });
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


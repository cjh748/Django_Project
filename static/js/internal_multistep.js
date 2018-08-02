i = 2;
$(document).ready(function () {
    $.get("/internal_plag/multistep/", {'step': 'pre_process'}, function (resp) {
        $.get("/internal_plag/multistep", {'step': 'ngram1'}, function (resp) {
            $("#ngram1").html(resp.result1);
            $.get("/internal_plag/multistep", {'step': 'ngram2'}, function (resp) {
                $("#ngram2").html(resp.result2);
                $.get("/internal_plag/multistep", {'step': 'ngram3'}, function (resp) {
                    $("#ngram3").html(resp.result3);
                    $.get("/internal_plag/multistep", {'step': 'ngram4'}, function (resp) {
                        $("#ngram4").html(resp.result4);
                        $.get("/internal_plag/multistep", {'step': 'ngram5'}, function (resp) {
                            $("#ngram5").html(resp.result5);

                            progress();

                            $.get("/internal_plag/multistep/", {'step': 'pre_process_tfidf'}, function (resp) {
                                $.get("/internal_plag/multistep", {'step': 'tfidf'}, function (resp) {
                                    $("#tfidf-int").html(resp.tfidf_result);

                                    progress();

                                    $.get("/internal_plag/multistep/", {'step': 'pre_process_wordnet'}, function (resp) {
                                        $.get("/internal_plag/multistep", {'step': 'wordnet'}, function (resp) {
                                            $("#wordnet-int").html(resp.wordnet_result);

                                            progress();

                                            $.get("/internal_plag/multistep/", {'step': 'pre_process_lcs'}, function (resp) {
                                                $.get("/internal_plag/multistep", {'step': 'lcs-substring'}, function (resp) {
                                                    $("#lcs-string").html(resp.lcs_result);

                                                    $.get("/internal_plag/multistep", {'step': 'lcs-subsequence'}, function (resp) {
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


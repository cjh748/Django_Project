$(document).ready(function () {


    $(".delete-original").on("click", function (evt) {
            evt.preventDefault();
            if (confirm("Are you sure you want to delete that file?")) {
                var item = $(this);
                $.post("/source_plag/delete-original/", {'pk': item.data('pk')}, function (resp) {
                    item.parent().hide()
                })
            }
            return false
        }
    );

    $(".delete-suspicious").on("click", function (evt) {
            evt.preventDefault();
            if (confirm("Are you sure you want to delete that file?")) {
                var item = $(this);
                $.post("/source_plag/delete-suspicious/", {'pk': item.data('pk')}, function (resp) {
                    item.parent().hide()
                })
            }
            return false
        }
    );

    $(".delete-suspicious-internal").on("click", function (evt) {
            evt.preventDefault();
            if (confirm("Are you sure you want to delete that file?")) {
                var item = $(this);
                $.post("/internal_plag/delete-suspicious-internal/", {'pk': item.data('pk')}, function (resp) {
                    item.parent().hide()
                })
            }
            return false
        }
    );

    $(".delete-suspicious-external").on("click", function (evt) {
            evt.preventDefault();
            if (confirm("Are you sure you want to delete that file?")) {
                var item = $(this);
                $.post("/external_plag/delete-suspicious-external/", {'pk': item.data('pk')}, function (resp) {
                    item.parent().hide()
                })
            }
            return false
        }
    );

});
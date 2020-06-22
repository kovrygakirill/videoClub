$(document).ready(function () {

    $(".like").click(function (event) {
        var id_movie = $(this).attr('name');
        // alert(id_movie);
        $.ajax({
            type: 'POST',
            url: "/add_like/",
            data: {
                pk: id_movie
            },
            dataType: 'json',
            success: function (data) {
                // alert("hello");
                $("#movie_likes_" + id_movie).text(data.count_like);
            },
            error: function (rs, r) {
                alert(rs.responseText);
            }
        });
    });

    $(".dislike").click(function (event) {
        var id_movie = $(this).attr('name');
        // alert(id_movie);

        $.ajax({
            type: "POST",
            url: '/add_dislike/',
            data: {
                pk: id_movie
            },
            dataType: 'json',
            success: function (data) {
                // alert(data.count_like);
                $("#movie_dislikes_" + id_movie).text(data.count_like);
            },
            error: function (rs, r) {
                alert(rs.responseText);
            }
        });
    });
});

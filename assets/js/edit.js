
function updateLike(url) {
    $.get(url, function (data, status) {
        if(data.liked){
            document.getElementById('likeicon').className = "glyphicon glyphicon-thumbs-up";
        } else {
            document.getElementById('likeicon').className = "glyphicon glyphicon-thumbs-down";
        }
        document.getElementById('likeicon').textContent= " " + data.rate;
    })
}
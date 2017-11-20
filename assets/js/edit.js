
function updateLike() {
    $.get("/product/iphonex/vote", function (data, status) {
        //document.getElementById('likebut').innerHTML = "Like " + data.rate;
        //document.getElementById('likebut').style.backgroundColor = "#cd001d";
        if(document.getElementById('likeicon').className=='glyphicon glyphicon-thumbs-up'){
            document.getElementById('likeicon').className = "glyphicon glyphicon-thumbs-down";
        } else {
            document.getElementById('likeicon').className = "glyphicon glyphicon-thumbs-up";
        }
        document.getElementById('likebut').textContent+=data.rate;
        //document.getElementById('likeicon').className = "glyphicon glyphicon-thumbs-up";
        //$('#likebut').attr('background-color',"#cd001d");
        //ata.rate
        console.log(data);
        console.log(status);
    })
}
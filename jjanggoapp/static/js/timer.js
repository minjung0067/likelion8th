var time = 60;
var min = "";
var sec = "";
let friend =document.querySelectorAll("#friend");
for (let i =0; friend.length; i+=1){
    friend[i].addEventListener('click',function(){
var x = setInterval(function(){
    min = parseInt(time/60);
    sec = time%60;

    document.getElementById("timer").innerHTML = min + "분 " + sec + "초";
    time--;

    if(time<0){
        clearInterval(x);
        document.getElementById("timer").innerHTML = "시간초과";
        var modal = document.getElementById('myModal');
        // Get the <span> element that closes the modal
        var span = document.getElementsByClassName("close")[0];                                          

        modal.style.display = "block";
        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
            modal.style.display = "none";
        }
 
        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }


    }
},1000);
})
}
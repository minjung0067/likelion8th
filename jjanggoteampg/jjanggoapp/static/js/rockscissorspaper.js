
var draw=0;
var win=0;
var lose=0;
function Player(p) {

    if (!p) {

        p = 0;

    }



    this.point = p;

}

Player.prototype.toString = function() {

    switch(this.point) {

        case 0:

            return "가위";

        case 1:

            return "바위";

        case 2:

            return "보";

    }

};



//이벤트핸들러여서 evt가 넘어오게 되어있다.

function playRockScissorsPaper(evt) {



        //alert(evt);//마우스 이벤트내

    var source = getEventSource(evt);//source는 buttonElement다

    var player = new Player();

    var computer = new Player(Math.floor(Math.random() * 3));//0,1,2가 발생

    var resultElement = document.getElementById('result');//이해 완료


 
    

    switch(source.id) {//evt.target.id가 즉 buttonElement의 id가 아래와 같으면

        case 'btnScissors':

            player.point = 0;

            break;

        case 'btnRock':

            player.point = 1;

            break;

        case 'btnPaper':

            player.point = 2;

            break;

        default:

            return;

    }



    if (player.point == computer.point) {//같으면 비기고
        draw++;
        resultElement.innerHTML = 'YOU: ' + player + ' vs 짱구: ' + computer + ' => DRAW' + '<br/>'+ '* 현재 초코비 ' + win + '개 *';
        strTest.replace(/\n/g, '<br/>');
    } else {//여긴 알고리즘부분

        if ((player.point + 1) % 3 == computer.point) {
            lose++;
            resultElement.innerHTML = 'YOU: ' + player + ' vs 짱구: ' + computer + ' => LOSE'+ '<br/>' + '* 현재 초코비 ' + win + '개 *';
            strTest.replace(/\n/g, '<br/>');
        } else {
            win++;
            resultElement.innerHTML = 'YOU: ' + player + ' vs 짱구: ' + computer + ' => WIN' + '<br/>'+ '* 현재 초코비 ' + win + '개 *';
            strTest.replace(/\n/g, '<br/>');
        }

    };



}



function clearResult(){

        var resultElement = document.getElementById("result");
        draw =0;
        win =0;
        lose=0;
        resultElement.innerHTML = "준비";

}



function init() {

        var btnRockElement = document.getElementById("btnRock");

        var btnScissorsElement = document.getElementById("btnScissors");


 
        var btnPaperElement = document.getElementById("btnPaper");

        var btnResetElement = document.getElementById("btnReset");

        

        addListener(btnRockElement, 'click', playRockScissorsPaper);

        addListener(btnScissorsElement, 'click', playRockScissorsPaper);

        addListener(btnPaperElement, 'click', playRockScissorsPaper);

        addListener(btnResetElement, 'click', clearResult);

}



//세번째는 call back

function addListener(el, ev, handler) {

        //alert(el);

        //크롬 파이어폭스용

    if (el.addEventListener) {//el에 gameElement임

        el.addEventListener(ev, handler, false);

    } else {//익스플로러 8버전 이하용

        el.attachEvent('on' + ev, handler);

    }

}0



//여기 매개변수 부분 이해 잘 안됨

function getEventSource(evt) {

        

        //alert(evt.target);//evt.target은 Button엘레먼트

    if (evt.target)

        return evt.target;

    else

        return window.event.srcElement;

}



addListener(window, 'load', init);

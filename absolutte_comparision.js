//절대 비교 기법 --> 함수
function is_equal(a, b){
    return Math.abs(a-b) <= 1e-10;
}

function is_equal2(a, b, allowed=0){
    var ep = Math.pow(2, -52);
    return Math.abs(a-b)<= Math.max(Math.abs(a), Math.abs(b)) * ep * Math.pow(2, allowed)
}


function main(){
    var sum=0;

    for(var i=0; i<100; i++){
        sum+=0.01;
    }
    
    if( is_equal2(sum, 1.0, 1.584963)){
        console.log("THE SAME");
    }
    else console.log("NOT THE SAME");
}
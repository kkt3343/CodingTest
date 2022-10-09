const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
var str = input[0];

/* 도움 준 사이트 : 
*https://www.jdoodle.com/execute-nodejs-online/
*https://codecollector.tistory.com/937
*/

var box = new Array();
var result = new Array();

function check(c){
	if(c == '('){
		box.push(c);
		return;
	}
	if(c == ')'){
		while(true){
			if(box.length === 0){
				break;
			}
			if(box[box.length-1] === '('){
				break;
			}
			result.push(box.pop());
		}
		box.pop();
		return;
	}
	if(c == '*' || c == '/'){
		while(true){
			if(box.length == 0 || (box[box.length-1] != '*' && box[box.length-1] != '/')){
				break;
			}
			result.push(box.pop());
		}
	}
	else{
		while(true){
			if(box.length == 0 || box[box.length-1] == '('){
				break;
			}
			result.push(box.pop());
		}
	}
	box.push(c);	
}
function pr(){
	console.warn("result상태");
	console.log(result);
	console.warn("box상태");
	console.log(box);
}

for(var i=0;i<str.length;i++){
    if(str[i] == '+' || str[i] == '-' || str[i] == '*' || str[i] == '/' || str[i] == '(' || str[i] == ')' ){
		check(str[i]);
    }
	else{
		result.push(str[i]);
	}
}

while(true){
	result.push(box.pop());
	if(box.length == 0){
		break;
	}
}
var res ="";
for(var i=0;i<result.length;i++){
	if(typeof result[i]!="undefined"){
		res = res + result[i];
	}
}
console.log(res);
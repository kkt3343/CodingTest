const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

var arr = new Array();
for(var a = 1; a <= input[0]; a++){
    arr.push(Number(input[a]))
}

const max_count = 8001;
var freq = new Array(max_count);
for(var i = 0; i<freq.length;i++){
	freq[i] = 0;
}

//오름차순정렬
arr.sort(function(a, b) { 
    return a - b;
});

//1.산술평균
var sum = 0;
for(var i = 0; i<arr.length;i++){
	sum = sum + arr[i];
}
var res = Math.round(sum / arr.length, 0);
if(res == -0){
	res = 0;
}
console.log(res);

//2.중앙값
console.log(arr[Math.floor(arr.length / 2)]);

//3.최빈값
for(var i = 0; i<arr.length;i++){
	freq[arr[i]+4000]++;
}
var maxnum = new Array(2);
var index = new Array(2);
maxnum[0] = -1, maxnum[1] = -1;
index[0] = 0, index[1] = 0;

var lock = false;
for(var i = 0; i<freq.length;i++){
	if(maxnum[0] < freq[i]){
		maxnum[0] = freq[i];
		index[0] = i;
		lock = false;
		continue;
	}
	if(freq[i] == maxnum[0] && lock == false){
		maxnum[1] = freq[i];
		index[1] = i;
		lock = true;
	}
}
var res3 = 0;
if(maxnum[0] == maxnum[1]){
	res3 = index[1];
}
else{
	res3 = index[0];
}
console.log(res3-4000);
//4.범위
console.log(arr[arr.length-1]-arr[0]);
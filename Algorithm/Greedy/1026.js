const fs = require("fs")
const input = fs.readFileSync("./input.txt").toString().split("\n");

function solution(arr) {
    const [num, ...data] = arr;
    const [a, b] = data.map(d => d.split(' ').map(Number));
  
    a.sort((a, b) => a - b);
    b.sort((a, b) => b - a);
  
    let sum = 0;
    for (let i = 0; i < a.length; i++) sum += a[i] * b[i];
  
    return sum;
  }
  
  console.log(solution(input));

const fs = require("fs");
const file = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync("./input.txt").toString().trim().split("\n").map((item)=> Number(item));
console.log(input[0]+input[1])

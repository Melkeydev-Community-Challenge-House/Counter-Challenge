const rl=require("readline").createInterface({input:process.stdin,output:process.stdout});
const startCounting=()=>{return new Promise(r=>{rl.question("start counting ya? [y]:",i=>r(i==="y"))})}
const toWhatNumBRUH=()=>{return new Promise(r=>{rl.question("what number shall we count to? [0 to ??]",n=>r(n))});}
const enterKey=()=>{return new Promise(r=>{rl.question("",i=>r(++num));});}
let num = 0;
let shit = async()=>{
  num = 0;
  while (!(answer = await startCounting())){}
  while (isNaN(number= await toWhatNumBRUH())){console.log('thats not a number you tard', number);}
  console.log('press enter fucking key to count!');
  while(( r = await enterKey()) != number ){console.log(`yay we're now upto number ${num} of ${number}`);}
  console.log(`All done counting to ${number}. not gonna optionally ask you if you wanna start again. you have no choice!`);
  shit();
}
shit();

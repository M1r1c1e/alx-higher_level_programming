#!/usr/bin/node
const args = process.argv.slice(2).map(Number); 

if (args.len === 0) {
    console.log(0);
} else if (args.len === 1) {
    console.log(0);
} else {
    const sortedArgs = args.sort((a, b) => b - a); 
    console.log(sortedArgs[1]); 
}


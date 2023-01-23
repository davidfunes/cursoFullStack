let num = 10;
let factorial = 1;
let i = 1;

while (i <= num) {
    factorial *= i;
    i++;    
}

console.log(`El factorial del número ${num} es: ${factorial}`);
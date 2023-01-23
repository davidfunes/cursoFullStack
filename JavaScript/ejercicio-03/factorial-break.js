let num = 10;
let factorial = 1;
let i = 1;

while (true) {
    factorial *= i;
    if (i == num) {
        break;
    }
    i++;
}

console.log(`El factorial de número ${num} es: ${factorial}`);
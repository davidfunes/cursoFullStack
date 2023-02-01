// Crea un archivo JS que contenga las siguientes líneas

// - Una variable que contenga tu altura en centímetros (entero)
let height_cm = 172;
console.log(height_cm);

// - Una variable que contenga tu altura en metros (número de coma flotante)
let height_m = height_cm / 100;
console.log(height_m);

// - Una variable que contenga tu peso en kilogramos (número de coma flotante)
let weight_kg = 120.23;
console.log(weight_kg);

// - Una variable que contenga tu altura en metros redondeada hacia arriba
let height_m_ceil = Math.ceil(height_m);
console.log(height_m_ceil);

// - Una variable que contenga tu peso en kilogramos redondeado hacia abajo
let weight_kg_rounded = Math.floor(weight_kg);
console.log(weight_kg_rounded);

// - Una variable que contenga si "el máximo valor que se puede obtener en Javascript + 1" es igual al máximo valor que se puede obtener en Javascript
let max_value_is_equal = (Number.MAX_VALUE + 1 === Number.MAX_VALUE);
console.log(max_value_is_equal);

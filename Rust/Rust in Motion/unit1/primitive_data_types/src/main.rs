fn main() {
    println!("Primitive Data Types");

    println!("\nSimple built-in types\n");

    // booleans
    let a = true;
    let b = false;
    if a {
        println!("a is true");
    }
    if !b {
        println!("b is false");
    }

    // integers
    // signed and unsigned
    // i8 - signed 8 bit integer(MSB used for sign), u8 - unsigned 8 bit integer
    // sizes: 8, 16, 32, 64
    let x = 5; // by default integer values assigned to a variable make that variable an i32
    println!("x is {}", x);

    // floating-point numbers
    // sizes: f32 and f64
    let x = 54.3; // by default FP values assigned to a variable make that variable an f64
    println!("x is {}", x);

    // characters - char
    // unicode character assigned with single quotes
    let c = 'に';
    println!("c is {}", c);

    println!("\nCompound built-in types\n");

    // tuples
    let tup = (1, 'c', true); // multiple values of same/different types can be grouped together
    // println!("tup is {}", tup); // will fail compilation, not valid unlike in Python
    println!("tup is {:?}", tup); // this is valid
    println!("item at index 1 of tup is {}", tup.1);
    let (x, y, z) = tup; // tuple destructuring
    println!("3 items in tup after destructuring are {}, {} and {}", x, y, z); // similar to Python, maybe useful for returning multiple values

    // arrays
    // they have fixed size
    let a = [0.0, 3.14, -8.7928]; // all elements of an array has the same type
    println!("a is {:?}", a); // this is valid
    println!("second element present in array 'a' is {}", a[1]);
    let mut b = a; // b is mutable but its length is fixed
    println!("before modification, mut b is {:?}", b);
    b[1] *= 2.0;
    println!("after modification, b is {:?}", b);
    // b += 78.9; // will fail, use Vec provided by Standard Library

    // slices
    let a = [1, 2, 3, 4, 5];
    let b = &a[0..2]; // slice of a, index 0 inclusive but index 2 exclusive
    println!("a is {:?}, b is {:?}", a, b);

    // string literals
    // array of characters assigned with double quotes
    let s = "Hello, World!";
    let substring = &s[3..8];
    println!("s is \"{}\", substring [3, 8) is \"{}\"", s, substring);
}

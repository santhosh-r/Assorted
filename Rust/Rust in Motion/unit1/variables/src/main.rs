fn main() {
    let x = 5;
    let y = 6;
    let z = x + y;
    println!("z is {}", z); // "println!" is a macro

    let mut w = 6; // by default let declares variables as constants, "mut" is needed to explicitly declare "w" here as a variable
    w += 7;
    println!("w is {}", w);

    let mut u: i32 = 1024; // types can be annotated (here i32 is 32-bit integer) but Rust can infer type from value assigned
    u += w;
    println!("u is {}", u);

    // let y: i32 = true; // will fail compilation due to type mismatch (expected 32-bit integer but was assigned a boolean value)
    // also notice above variable names can be reused

    
}

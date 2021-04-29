
fn print_square_of(number: i32) {
    // if number == 0 | 1 { // logical error
    if number == 0 || number == 1 { // same as C++
        return;
    }
    println!("The square of {} is {}.", number, number*number);
}

fn next_birthday(name: &str, current_age: u8) -> String { // str is not an acceptable return type because because size can't be known while compiling but String is?
    let next_age = current_age + 1;
    format!("Hi {}, on your next birthday, you'll be {}!", name, next_age) // no semicolon, idiomatic way to return at the end of a function but return works as in C
}

fn main() {
    print_square_of(0); // nothing will be printed
    print_square_of(11);
    println!("{}\n{}", next_birthday("Santhosh", 34), next_birthday("Harsha", 9));
}

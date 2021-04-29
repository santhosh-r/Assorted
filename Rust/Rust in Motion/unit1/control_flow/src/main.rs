use std::time::{Instant, Duration};
use std::thread::sleep;
use std::io;
use std::io::Write; // to bring flush() into scope

fn main() {
    // Control Flow

    // if...else if...else
    let condition_a = false;
    let condition_b = false;
    let value = if condition_a {
        "a"
    } else if !condition_b {
        "!b"
    } else {
        "!a and b"
    }; // similar to Rust functions but if else needs to exhaustive, all values of same type and end with a semicolon
    println!("value is {}", value);

    // loop
    let current_time = Instant::now();
    let mut i = 0;
    print!("running loop for 4 seconds...");
    loop { // allow loop to run for 4 seconds
        print!("{:.1} secs elapsed", (i as f32)*0.5);
        i += 1;
        // io::stdout().flush().unwrap(); // unwrap to avoid using result from flush, to handle exception flush().ok().expect("Could not flush stdout"), why use ok()?
        io::stdout().flush().expect("Couldn't flush");
        print!("\x1B[16D");
        // sleep(Duration::new(1, 0));
        sleep(Duration::from_millis(500));
        if current_time.elapsed().as_secs() == 4 {
            println!("done            "); // extra spaces to clear "secs elapsed"
            break;
        }
    }

    loop {
        print!("What's the secret word? ");
        io::stdout().flush().expect("Couldn't flush"); // needs flush to display prompt, may be idiomatic to not prompt in this manner (use println! which does flush)
        let mut word = String::new();
        io::stdin().read_line(&mut word).expect("Failed to read line");

        if word.trim() == "rust" {
            println!("{} is the correct secret word", word.trim());
            break;
        } else {
            println!("{} is not the secret word", word.trim());
        }
    }

    // while
    let mut word = String::new();
    while word.trim() != "korone" {
        println!("What's the secret word now? (Hint: first name of doggo that insulted a turtle for its small house)");
        word = String::new();
        io::stdin().read_line(&mut word).expect("Failed to read line");
        if word.trim() != "korone" {
            println!("Wrong! Another Hint: https://twitter.com/CarolineDirectr/status/1316582424470450177");
        }
    }

    // for
    // similar to python
    print!("running for loop for 2 seconds...");
    for i in 0..8 { // run for loop on range [0,7]
        print!("{:.2} secs elapsed", (i as f32)*0.25);
        io::stdout().flush().expect("Couldn't flush");
        print!("\x1B[17D");
        sleep(Duration::from_millis(250));
    }
    println!("done             "); // extra spaces to clear "secs elapsed"

    // match
    // kind of similar to switch except match is exhaustive
    // strange quip: destructured tuple uses pattern matching??
    let x = 3;
    match x {
        1 => println!("you are lonely\nlonely lonely lonely"),
        2 => println!("Two's a company"),
        3 => { println!("Three's a crowd"); println!("another statement inside pattern '3'") }, // curly brackets can be used for multiple statements, semicolon optional for last statement
        _ => println!("Some other number") // ending comma for last pattern (catch all here) is optional
    }

    let die1 = 1;
    let die2 = 5;

    match (die1, die2) {
        (1 , 1) => println!("lonely lonely lonely"),
        (_, 5) | (5, _) => println!("You rolled at least one 5! Watch 35!"), // | here is for pattern alternatives, normally its bitwise or like in C/C++
        _ => println!("Move your piece!"),
    }
}

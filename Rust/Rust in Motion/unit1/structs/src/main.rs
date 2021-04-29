
// structs
enum HockeyPosition {
    Wing // enum variants should be in CamelCase
}

struct HockeyPlayer { // by convention, struct and enum names should be in CamelCase
    name: String, // field names should be in snake_case
    number: u8,
    position: HockeyPosition,
    goals_ytd: u8
}

// tuple structs
struct Triangle(u32, u32, u32); // fields are not named, they are accessed with dot and index like a tuple

fn is_triangle_pythagorean(triangle: Triangle) -> bool {
    let longest_side = if triangle.0 > triangle.1 && triangle.0 > triangle.2 {
        triangle.0
    } else if triangle.1 > triangle.2 {
        triangle.1
    } else {
        triangle.2
    };
    longest_side * longest_side * 2 == triangle.0 * triangle.0 + triangle.1 * triangle.1 + triangle.2 * triangle.2
}

// tuple struct use in "newtype pattern"
// existing type is wrapped in a single element tuple struct to give meaning
// now the exisiting type cannot be used accidently in place of the new struct eg. u8 value meant for Liters used for a Meters arg
struct Meters(u8);

fn add_distance(d1: Meters, d2: Meters) -> Meters {
    Meters(d1.0 + d2.0)
}

// unit structs are structs with no fields but can have methods defined

// enums with named fields
enum Clock {
    // Sundial(u8),
    Sundial { hours: u8 },
    // Digital(u8, u8),
    Digital { hours: u8, minutes: u8 },
    // Analog(u8, u8, u8),
    Analog  { hours: u8, minutes: u8, seconds: u8 },
    // enum variants can also have named fields
}

fn tell_time(clock: Clock) {
    match clock {
        Clock::Sundial { hours: h } => println!("It is about {} o'clock", h),
        Clock::Digital { hours: h, minutes: m } => println!("It is {} minutes past {} o'clock", m, h),
        Clock::Analog { hours, minutes, seconds } => { // no need to give names/aliases to fields
            println!("It is {} minutes and {} seconds past {} o'clock", minutes, seconds, hours)
        }
    }
}

fn main() {
    let player = HockeyPlayer { // instantiating a HockeyPlayer
        name: String::from("Bryan Rust"),
        goals_ytd: 7, // fields need not be the same order as struct declaration, do default values exist?
        number: 17,
        position: HockeyPosition::Wing, // even though not necessary adding comma for the last field makes rearranging convenient
    }; // like C/C++, assignment statement ends with a semicolon

    // to be able to modify a struct instance, use mut keyword

    print!("{} #{} has scored {} goals this season and has the ",
        player.name, player.number, player.goals_ytd); // field access similar to C++
    match player.position { // if statements with eq() or == aren't valid without the programmer defining them
        HockeyPosition::Wing => print!("Wing")
    }
    println!(" position"); // unlike print macro, println macro flushes buffer to screen without needing flush statement

    let triangle1 = Triangle(3, 5, 4);
    println!("Is triangle1 pythagorean? {}", is_triangle_pythagorean(triangle1));

    // tuple struct use in "newtype pattern"
    println!("Adding distances 2 and 7 results in {}", add_distance(Meters(2), Meters(7)).0);
    // println!("Adding distances 2 and 7 results in {}", add_distance(Meters(2), 7).0); // type mismatch error

    // enums with named fields example
    let clock = Clock::Sundial { hours: 6 };
    tell_time(clock);
    tell_time(Clock::Digital { hours: 9, minutes: 45 });
    tell_time(Clock::Analog { hours: 10, seconds: 32, minutes: 54 } ); // fields need not be in the same order as they are named
}

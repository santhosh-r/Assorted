// methods define behavior on custom types defined by enums and structs
// they are similar to functions like in C++/Java
// "associated functions" are different from both methods and functions
// types: read only methods and r/w methods

enum HockeyPosition {
    Center,
    Wing,
    Defense,
    Goalie
}

// dummy function to get rid of warnings
fn next_player(position: HockeyPosition) {
    match position {
        HockeyPosition::Center => print!("Center"),
        _ => print!("Not center")
    }
    println!("\x1B[2K\x1B[A"); // erase current line and move up cursor one line
}

struct HockeyPlayer {
    name: String,
    number: u8,
    position: HockeyPosition,
    goals_ytd: u8
}

// my own definition
// fn shoot_puck(mut hockey_player: HockeyPlayer) -> HockeyPlayer { // mut keyword needed to able to change field value
//     hockey_player.goals_ytd += 1;
//     hockey_player
// }

// definition from book
// fn shoot_puck(hockey_player: HockeyPlayer, seconds_remaining: u16) {
//     if seconds_remaining < 300 {
//         match hockey_player.position { // logic used here: only players in the Center position have the composure to make the goal under 5 minutes
//             HockeyPosition::Center => println!("Goal!"),
//             _ => println!("Miss!")
//         }
//     } else {
//         println!("Goal!")
//     }
// }
// the above function is only applicable to hockey players and is better implemented as a method for HockeyPlayer

// methods: adding behavior to user defined data types

impl HockeyPlayer { // similar for enum
    // fn shoot_puck(self, seconds_remaining: u16) { // consumes self/takes ownership of self
    // fn shoot_puck(&self, seconds_remaining: u16) { // proper way but self can't be modified
    fn shoot_puck(&mut self, seconds_remaining: u16) { // now self is a reference than be used to modify instance
            if seconds_remaining < 300 {
            match self.position { // logic used here: only players in the Center position have the composure to make the goal under 5 minutes
                HockeyPosition::Center => {
                    self.goals_ytd += 1;
                    println!("Goal!")
                },
                _ => println!("Miss!")
            }
        } else {
            self.goals_ytd += 1;
            println!("Goal!")
        }
    } // notice the method is identical to the fuction with the exception of reference to self like in Python instead of typed argument name

    // associated functions (similar to friendly functions in C++?? Nope)
    // basically a "method" without reference to self, used without instancing struct with :: operator
    // NOTICE
    // NOTICE new is not a special keyword or in-built function in Rust but
    // NOTICE by convention used to create new instance of a type like a constructor
    // NOTICE
    fn new(name: String, number: u8, position: HockeyPosition) -> HockeyPlayer {
        HockeyPlayer {
            name: name,
            number: number,
            position: position,
            goals_ytd: 0,
        }
    }
}

fn main() {
    // dummy statements to get rid of warnings
    next_player(HockeyPosition::Center);
    next_player(HockeyPosition::Defense);
    next_player(HockeyPosition::Goalie);
    
    // println!("\x1B[2J"); // VT100 escape sequnce to clear screen. 1B(hex) = 33(oct) = 27(dec) ANSI code for Escape character.
    // In VS code terminal output, the code just inserts enough lines to push already existing lines out of output but they can be accessed by scrolling up

    // let mut player = HockeyPlayer { // for old definition of shoot_puck
    // let player = HockeyPlayer {
    //     name: String::from("Bryan Rust"),
    //     number: 17,
    //     position: HockeyPosition::Wing,
    //     goals_ytd: 7,
    // };

    // using the associated function new to instantiate HockeyPlayer player
    let mut player = HockeyPlayer::new(String::from("Bryan Rust"), 17, HockeyPosition::Wing);
    player.goals_ytd = 7; // these two lines are equivalent to above commented out definition of player
    // do we have default values for arguments in Rust?

    // // shoot_puck(player); // player is moved to hockey_player in shoot_puck(), can't be used again
    // player = shoot_puck(player);
    println!("{} #{} has shot {} goals this season", player.name, player.number, player.goals_ytd);

    // the method from book
    // shoot_puck(player, 280);

    // method call
    player.shoot_puck(780); // same problem as my custom definition when instance method is called after use in a function call, player is consumed ie. ownership is taken by first function/method call
    player.shoot_puck(225); // fixed with reference to self i.e. &self in method signature, again same problem

    // player after goal attempts, method has modified goals_ytd
    println!("{} #{} has shot {} goals this season", player.name, player.number, player.goals_ytd);
}    

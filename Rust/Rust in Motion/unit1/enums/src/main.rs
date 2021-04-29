// enums

// can only be one value at a time
// all possible values can be listed/enumerated

enum HockeyPosition {
    Center,
    Wing,
    Defense,
    Goalie
}

fn next_player(position: HockeyPosition) {
    match position {
        HockeyPosition::Center => println!("Center"),
        _ => println!("Not center")
    }
}

enum Clock {
    Sundial(u8),
    Digital(u8, u8),
    Analog(u8, u8, u8)
    // enum variants can also have named fields
}

fn tell_time(clock: Clock) {
    match clock {
        Clock::Sundial(h) => println!("It is about {} o'clock", h),
        Clock::Digital(h, m) => println!("It is {} minutes past {} o'clock", m, h),
        Clock::Analog(h, m, s) => {
            println!("It is {} minutes and {} seconds past {} o'clock", m, s, h)
        }
    }
}

fn main() {
    tell_time(Clock::Sundial(6));
    tell_time(Clock::Digital(9, 45));
    tell_time(Clock::Analog(10, 32, 54));
    let position = HockeyPosition::Defense;
    next_player(position);
    next_player(HockeyPosition::Center);
    next_player(HockeyPosition::Wing);
    next_player(HockeyPosition::Goalie) // last statement apparently doesn't need a semicolon even though the function is declared to have no return value
}

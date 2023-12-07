use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("input")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let split Vec<_> = contents.split("\n").collect();
    for e in split[0] {
        println!("{}", e);
    }
    Ok(())
}

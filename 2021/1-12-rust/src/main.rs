mod helpers;

use crate::helpers::*;

fn main() {
    // Creation of the object that will host the input data

    let mut input_arr: Vec<i32> = Vec::new();

    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("./input/data.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
                //push the string as numbers in the Vector
                input_arr.push(ip.parse().unwrap());
            }
        }
    }

    //println!("{:?}", input_arr); // print the input

    let mut i:usize = 1;
    let mut count:i32 = 0;
    while i < input_arr.len() {
        
        // println!("{}", input_arr[i]);
        if input_arr[i-1] < input_arr[i] {
            count += 1
        }


        i += 1;

    }

    println!("{}{}", "First result is ", count);

    i = 3;
    count = 0;

    while i < input_arr.len() {
        
        // println!("{}", input_arr[i]);
        if input_arr[i-3] < input_arr[i] {
            count += 1
        }


        i += 1;

    }

    println!("{}{}", "Second result is ", count);



}
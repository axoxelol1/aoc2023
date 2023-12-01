fn main() {
    let input = include_str!("../input.txt");
    let part1: usize = input.lines().fold(0, |acc, line| {
        let digits: Vec<char> = line.chars().filter(|c| c.is_digit(10)).collect();
        let first = digits[0];
        let last = digits[digits.len() - 1];
        let mut num = first.to_string();
        num.push(last);
        acc + num.parse::<usize>().unwrap()
    });
    let part2: usize = input.lines().fold(0, |acc, line| {
        let mut digits: Vec<char> = vec![];
        let chars: Vec<char> = line.chars().collect();
        for i in 0..(chars.len()) {
            if chars[i].is_digit(10) {
                digits.push(chars[i])
            } else {
                for j in 3..=5 {
                    if i + j > chars.len() {
                        continue;
                    }
                    let word: String = chars[i..i + j].iter().collect();
                    if let Some(d) = numstr_to_num(&word) {
                        digits.push(d)
                    }
                }
            }
        }
        let first = digits[0];
        let last = digits[digits.len() - 1];
        let mut num = first.to_string();
        num.push(last);
        acc + num.parse::<usize>().unwrap()
    });
    println!("Part 1: {:?}", part1);
    println!("Part 2: {:?}", part2)
}

fn numstr_to_num(num: &str) -> Option<char> {
    match num {
        "one" => Some('1'),
        "two" => Some('2'),
        "three" => Some('3'),
        "four" => Some('4'),
        "five" => Some('5'),
        "six" => Some('6'),
        "seven" => Some('7'),
        "eight" => Some('8'),
        "nine" => Some('9'),
        _ => None,
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let part1: i32 = input
        .lines()
        .map(|line| {
            let mut nums: Vec<i32> = line
                .split_whitespace()
                .map(|x| x.parse().unwrap())
                .collect();
            let mut lastnums = vec![];
            while !nums.iter().all(|&x| x == 0) {
                lastnums.push(nums[nums.len() - 1]);
                nums = nums.windows(2).map(|a| a[1] - a[0]).collect();
            }
            return lastnums.iter().rev().fold(0, |acc, x| acc + x);
        })
        .sum();

    // Copy pasted with rev
    let part2: i32 = input
        .lines()
        .map(|line| {
            let mut nums: Vec<i32> = line
                .split_whitespace()
                .rev()
                .map(|x| x.parse().unwrap())
                .collect();
            let mut lastnums = vec![];
            while !nums.iter().all(|&x| x == 0) {
                lastnums.push(nums[nums.len() - 1]);
                nums = nums.windows(2).map(|a| a[1] - a[0]).collect();
            }
            return lastnums.iter().rev().fold(0, |acc, x| acc + x);
        })
        .sum();

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}

use std::collections::{HashMap, HashSet};
use std::str;

fn main() {
    let input = include_bytes!("../input.txt");
    let mut grid: Vec<&[u8]> = input.split(|&b| b == b'\n').collect();
    grid.pop();
    let mut nums: Vec<Vec<(usize, usize)>> = vec![];
    let mut symbol_poss: HashSet<(usize, usize)> = HashSet::new();
    for y in 0..grid.len() {
        for x in 0..grid[y].len() {
            if grid[y][x] != b'.' && !grid[y][x].is_ascii_digit() {
                symbol_poss.insert((x, y));
            }
        }
    }
    for y in 0..grid.len() {
        let mut x = 0;
        while x < grid[y].len() {
            if grid[y][x].is_ascii_digit() {
                let mut num = vec![];
                num.push((x, y));
                while x + 1 < grid[y].len() {
                    x += 1;
                    if grid[y][x].is_ascii_digit() {
                        num.push((x, y));
                    } else {
                        break;
                    }
                }
                nums.push(num)
            }
            x += 1;
        }
    }
    let mut part1sum = 0;
    for num in &nums {
        if symbols_around(num, &grid).len() > 0 {
            part1sum += vec_to_num(num, &grid)
        }
    }
    println!("Part 1: {}", part1sum);
    let mut asterterik_to_nums: HashMap<(usize, usize), Vec<&Vec<(usize, usize)>>> = HashMap::new();
    for num in &nums {
        for &(x, y) in symbols_around(num, &grid).iter() {
            if grid[y][x] == b'*' {
                let arr = asterterik_to_nums.entry((x, y)).or_insert(vec![]);
                arr.push(num)
            }
        }
    }
    let mut part2sum = 0;
    for (_, nums) in asterterik_to_nums.iter() {
        if nums.len() == 2 {
            part2sum += vec_to_num(nums[0], &grid) * vec_to_num(nums[1], &grid);
        }
    }
    println!("Part 2: {}", part2sum)
}

fn symbols_around(numvec: &Vec<(usize, usize)>, grid: &Vec<&[u8]>) -> HashSet<(usize, usize)> {
    let mut symbols = HashSet::new();
    for &(x, y) in numvec {
        for xd in 0..=2 {
            for yd in 0..=2 {
                if (x as i32 + xd as i32 - 1) < 0
                    || x + xd - 1 >= grid[0].len()
                    || (y as i32 + yd as i32 - 1) < 0
                    || y + yd - 1 >= grid.len()
                {
                    continue;
                }
                if !grid[y + yd - 1][x + xd - 1].is_ascii_digit()
                    && grid[y + yd - 1][x + xd - 1] != b'.'
                {
                    symbols.insert((x + xd - 1, y + yd - 1));
                }
            }
        }
    }
    symbols
}

fn vec_to_num(numvec: &Vec<(usize, usize)>, grid: &Vec<&[u8]>) -> i32 {
    let (firstx, y) = numvec[0];
    let (lastx, _) = numvec[numvec.len() - 1];
    return str::from_utf8(&grid[y][firstx..=lastx])
        .unwrap()
        .parse()
        .unwrap();
}

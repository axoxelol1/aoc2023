use std::collections::{HashMap, HashSet};

use num::Integer;

fn main() {
    let input = include_str!("../input.txt");
    let names_to_indexes: HashMap<&str, usize> = input
        .lines()
        .skip(2)
        .enumerate()
        .map(|(i, l)| (l.split_once(" ").unwrap().0, i))
        .collect();

    let adj: Vec<(usize, usize)> = input
        .lines()
        .skip(2)
        .map(|l| {
            let (l, r) = &l.split_once("=").unwrap().1.trim()[1..9]
                .split_once(", ")
                .unwrap();
            (
                *names_to_indexes.get(l).unwrap(),
                *names_to_indexes.get(r).unwrap(),
            )
        })
        .collect();

    let instrs: Vec<char> = input.lines().next().unwrap().chars().collect();

    if let Some(&zzz) = names_to_indexes.get("ZZZ") {
        println!(
            "Part 1 took {} steps",
            step_count(0, &HashSet::from([zzz]), &instrs, &adj)
        );
    }

    let startposs: Vec<usize> = names_to_indexes
        .iter()
        .filter(|(k, _)| k.chars().last().unwrap() == 'A')
        .map(|(_, v)| *v)
        .collect();
    let part2ends: HashSet<usize> = names_to_indexes
        .iter()
        .filter(|(k, _)| k.chars().last().unwrap() == 'Z')
        .map(|(_, v)| *v)
        .collect();

    let part2 = startposs
        .iter()
        .map(|&pos| step_count(pos, &part2ends, &instrs, &adj))
        .fold(1, |acc, steps| acc.lcm(&steps));
    println!("Part 2 took {:?} steps", part2);
}

fn step_count(
    start: usize,
    ends: &HashSet<usize>,
    instrs: &Vec<char>,
    adj: &Vec<(usize, usize)>,
) -> usize {
    let mut curpos = start;
    let mut steps = 0;
    while !ends.contains(&curpos) {
        let ins = instrs[steps % instrs.len()];
        curpos = if ins == 'L' {
            adj[curpos].0
        } else {
            adj[curpos].1
        };
        steps += 1;
    }
    return steps;
}

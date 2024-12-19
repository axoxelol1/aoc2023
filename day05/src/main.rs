use std::ops::Range;

fn main() {
    let input = include_str!("../input.txt");
    let seeds: Vec<i64> = input
        .lines()
        .next()
        .unwrap()
        .split_whitespace()
        .skip(1)
        .map(|w| w.parse().unwrap())
        .collect();

    let maps: Vec<Vec<(Range<i64>, i64)>> = input
        .split("\n\n")
        .skip(1)
        .map(|group| {
            let mut vec: Vec<(Range<i64>, i64)> = vec![];
            let lines = group.lines().skip(1);
            for line in lines {
                let nums: Vec<i64> = line
                    .split_whitespace()
                    .map(|w| w.parse().unwrap())
                    .collect();
                let dest = nums[0];
                let source = nums[1];
                let i = nums[2];
                let range = source..source + i;
                vec.push((range, dest - source))
            }
            vec
        })
        .collect();

    let part1: i64 = seeds
        .iter()
        .map(|seed| {
            maps.iter().fold(*seed, |id, ranges| {
                for (range, num) in ranges {
                    if range.contains(&id) {
                        return id + num;
                    }
                }
                return id;
            })
        })
        .min()
        .unwrap();

    println!("Part 1: {}", part1);

    let mut part2seeds: Vec<Range<i64>> = vec![];
    for i in (0..seeds.len() - 1).step_by(2) {
        part2seeds.push(seeds[i]..(seeds[i]+seeds[i+1]))
    }

    let part2: i64 = part2seeds.into_iter().map(|range| {
        range.map(|seed| {
            maps.iter().fold(seed, |id, ranges| {
                for (range, num) in ranges {
                    if range.contains(&id) {
                        return id + num;
                    }
                }
                return id;
            })
        })
        .min()
        .unwrap()
    }).min().unwrap();



    println!("part2seeds: {:?}", part2)
}

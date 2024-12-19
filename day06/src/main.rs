fn main() {
    let input = include_str!("../example.txt");
    let times: Vec<i32> = input
        .lines()
        .next()
        .unwrap()
        .split_whitespace()
        .skip(1)
        .map(|time| time.parse().unwrap())
        .collect();
    let dists: Vec<i32> = input
        .lines()
        .skip(1)
        .next()
        .unwrap()
        .split_whitespace()
        .skip(1)
        .map(|time| time.parse().unwrap())
        .collect();

    let part1 = times
        .iter()
        .zip(dists.iter())
        .fold(1, |acc, (&time, &dist)| {
            acc * (0..=time).filter(|t| (time - t) * t > dist).count()
        });

    let mut part2time = input
        .lines()
        .next()
        .unwrap()
        .split_whitespace()
        .skip(1)
        .collect::<String>();
    part2time.retain(|c| !c.is_whitespace());
    let part2time: i64 = part2time.parse().unwrap();
    let mut part2dist = input
        .lines()
        .skip(1)
        .next()
        .unwrap()
        .split_whitespace()
        .skip(1)
        .collect::<String>();
    part2dist.retain(|c| !c.is_whitespace());
    let part2dist: i64 = part2dist.parse().unwrap();
    let part2 = (0..=part2time)
        .filter(|t| (part2time - t) * t > part2dist)
        .count();

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}

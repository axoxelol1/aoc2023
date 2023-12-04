fn main() {
    let cards: Vec<(Vec<i32>, Vec<i32>)> = include_str!("../input.txt")
        .lines()
        .map(|line| {
            let (_, rest) = line.split_once(":").unwrap();
            let (winstr, mystr) = rest.split_once("|").unwrap();
            let winnums = winstr
                .split_whitespace()
                .map(|words| words.trim().parse().unwrap())
                .collect();
            let mynums = mystr
                .split_whitespace()
                .map(|words| words.trim().parse().unwrap())
                .collect();
            (winnums, mynums)
        })
        .collect();

    let part1sum = cards.iter().fold(0, |acc, card| acc + value(card));

    let mut curr_cards: Vec<usize> = (0..cards.len()).collect();
    let wincounts: Vec<usize> = cards
        .iter()
        .map(|(winnums, mynums)| mynums.iter().filter(|x| winnums.contains(x)).count())
        .collect();
    let mut part2count = 0;
    while let Some(id) = curr_cards.pop() {
        part2count += 1;
        let wincount = wincounts[id];
        for i in (id + 1)..=(id + wincount) {
            curr_cards.push(i)
        }
    }
    println!("Part 1: {}", part1sum);
    println!("Part 2: {}", part2count);
}

fn value(card: &(Vec<i32>, Vec<i32>)) -> i32 {
    let (winners, numbers) = card;
    numbers.iter().fold(0, |acc, x| {
        if winners.contains(x) {
            if acc == 0 {
                1
            } else {
                acc * 2
            }
        } else {
            acc
        }
    })
}

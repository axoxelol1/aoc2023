use std::collections::HashSet;

type Hand = [i32; 5];

#[derive(Debug, PartialEq, Eq, Ord, PartialOrd)]
enum Type {
    High,
    Pair,
    TwoPair,
    Three,
    FullHouse,
    Four,
    Five,
}

fn main() {
    let mut hands: Vec<(Hand, Type, i32)> = include_str!("../input.txt")
        .lines()
        .map(|l| {
            let (hand, bid) = l.split_once(" ").unwrap();
            let hand: Vec<i32> = hand.chars().map(|c| char_to_val(&c)).collect();
            let hand: [i32; 5] = [hand[0], hand[1], hand[2], hand[3], hand[4]];
            (hand, hand_to_type(&hand), bid.parse().unwrap())
        })
        .collect();

    hands.sort_by(|a, b| {
        use std::cmp::Ordering::*;
        match a.1.cmp(&b.1) {
            Equal => {
                for i in 0..5 {
                    let cmp = a.0[i].cmp(&b.0[i]);
                    if cmp != Equal {
                        return cmp;
                    }
                }
                panic!("Identical hands =(")
            }
            ord => ord,
        }
    });

    let part1 = hands
        .iter()
        .enumerate()
        .fold(0, |acc, (i, (_, _, bid))| acc + (i as i32 + 1) * bid);

    println!("Part 1: {}", part1);

    let mut hands2: Vec<(Hand, Type, i32)> = include_str!("../input.txt")
        .lines()
        .map(|l| {
            let (hand, bid) = l.split_once(" ").unwrap();
            let hand: Vec<i32> = hand.chars().map(|c| char_to_val2(&c)).collect();
            let hand: [i32; 5] = [hand[0], hand[1], hand[2], hand[3], hand[4]];
            (hand, hand_to_type2(&hand), bid.parse().unwrap())
        })
        .collect();

    hands2.sort_by(|a, b| {
        use std::cmp::Ordering::*;
        match a.1.cmp(&b.1) {
            Equal => {
                for i in 0..5 {
                    let cmp = a.0[i].cmp(&b.0[i]);
                    if cmp != Equal {
                        return cmp;
                    }
                }
                panic!("Identical hands =(")
            }
            ord => ord,
        }
    });

    let part2 = hands2
        .iter()
        .enumerate()
        .fold(0, |acc, (i, (_, _, bid))| acc + (i as i32 + 1) * bid);

    println!("Part 2: {}", part2)
}

fn char_to_val(c: &char) -> i32 {
    match c {
        'A' => 14,
        'K' => 13,
        'Q' => 12,
        'J' => 11,
        'T' => 10,
        _ => c.to_digit(10).unwrap() as i32,
    }
}

fn char_to_val2(c: &char) -> i32 {
    match c {
        'A' => 14,
        'K' => 13,
        'Q' => 12,
        'J' => 0,
        'T' => 10,
        _ => c.to_digit(10).unwrap() as i32,
    }
}

fn hand_to_type(hand: &[i32; 5]) -> Type {
    use Type::*;
    let unique_count: i32 = hand.iter().collect::<HashSet<&i32>>().len() as i32;
    let c1count = hand.iter().filter(|&&c| c == hand[0]).count();
    if unique_count == 1 {
        Five
    } else if unique_count == 2 {
        if c1count == 1 || c1count == 4 {
            Four
        } else {
            FullHouse
        }
    } else if unique_count == 3 {
        if c1count == 3 {
            Three
        } else if c1count == 2 {
            TwoPair
        } else {
            let c2count = hand.iter().filter(|&&c| c == hand[1]).count();
            if c2count == 2 {
                TwoPair
            } else {
                Three
            }
        }
    } else if unique_count == 4 {
        Pair
    } else {
        High
    }
}

fn hand_to_type2(hand: &[i32; 5]) -> Type {
    if !hand.contains(&0) {
        hand_to_type(hand)
    } else {
        let mut joker_indexes = vec![];
        for i in 0..5 {
            if hand[i] == 0 {
                joker_indexes.push(i)
            }
        }
        (1..=14)
            .filter(|&c| c != 11)
            .map(|val| {
                let mut newh = hand.clone();
                for i in joker_indexes.iter() {
                    newh[*i] = val
                }
                hand_to_type(&newh)
            })
            .max()
            .unwrap()
    }
}

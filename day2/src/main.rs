type Game = (usize, Vec<CubeSet>);

#[derive(Debug)]
struct CubeSet {
    red: usize,
    green: usize,
    blue: usize,
}

fn main() {
    let games: Vec<Game> = include_str!("../input.txt")
        .lines()
        .map(|line| {
            let (idstr, revealedstr) = line.split_once(":").unwrap();
            let revealedstr = revealedstr.trim();
            let id = idstr[5..].parse::<usize>().unwrap();
            let cube_sets = revealedstr
                .split(";")
                .map(|setstr| {
                    let (mut red, mut green, mut blue): (usize, usize, usize) = (0, 0, 0);
                    for color in setstr.split(",") {
                        let color = color.trim();
                        let (amount, color) = color.split_once(" ").unwrap();
                        if color.starts_with("r") {
                            red = amount.parse().unwrap()
                        } else if color.starts_with("g") {
                            green = amount.parse().unwrap()
                        } else {
                            blue = amount.parse().unwrap()
                        }
                    }
                    CubeSet { red, green, blue }
                })
                .collect();
            (id, cube_sets)
        })
        .collect();
    let part1sum = games.iter().fold(0, |sum, (id, cube_sets)| {
        if game_possible(cube_sets, 12, 13, 14) {
            sum + id
        } else {
            sum
        }
    });
    let part2sum = games.iter().fold(0, |sum, (_, cube_sets)| {
        let minr = cube_sets.iter().map(|set| set.red).max().unwrap();
        let ming = cube_sets.iter().map(|set| set.green).max().unwrap();
        let minb = cube_sets.iter().map(|set| set.blue).max().unwrap();
        sum + minr * ming * minb
    });
    println!("Part 1: {}", part1sum);
    println!("Part 2: {}", part2sum);
}

fn game_possible(cube_sets: &Vec<CubeSet>, maxred: usize, maxgreen: usize, maxblue: usize) -> bool {
    cube_sets
        .iter()
        .all(|&CubeSet { red, green, blue }| red <= maxred && green <= maxgreen && blue <= maxblue)
}

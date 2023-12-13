use std::collections::HashMap;
use std::env;

#[derive(Debug, PartialEq, Clone, Copy)]
struct Dirs {
    north: bool,
    east: bool,
    south: bool,
    west: bool,
}

impl Dirs {
    fn new(north: bool, east: bool, south: bool, west: bool) -> Dirs {
        Dirs {
            north,
            east,
            south,
            west,
        }
    }
}

fn main() {
    let chars_matrix: Vec<Vec<char>> = include_str!("../input.txt")
        .lines()
        .map(|l| l.chars().collect())
        .collect();
    let sketch: Vec<Vec<Dirs>> = include_str!("../input.txt")
        .lines()
        .map(|l| {
            l.chars()
                .map(|c| match c {
                    '|' => Dirs::new(true, false, true, false),
                    '-' => Dirs::new(false, true, false, true),
                    'L' => Dirs::new(true, true, false, false),
                    'J' => Dirs::new(true, false, false, true),
                    '7' => Dirs::new(false, false, true, true),
                    'F' => Dirs::new(false, true, true, false),
                    '.' => Dirs::new(false, false, false, false),
                    'S' => Dirs::new(true, false, false, true),
                    _ => panic!("Invalid pipe"),
                })
                .collect()
        })
        .collect();

    let startpos = (10, 61); //HARDCODED

    let mut visited = HashMap::new();
    let loop_conns = dfs(&sketch, startpos, &mut visited);

    let part1pos1 = visited.get(&(9, 61));
    let part1pos2 = visited.get(&(10, 60));

    let picture = env::args().collect::<Vec<String>>().get(1).is_some();

    let mut inside_count = 0;
    let mut inside_coords = vec![];
    for y in 0..sketch.len() {
        let mut inside = false;
        for x in 0..sketch[y].len() {
            if loop_conns.contains_key(&(x, y)) {
                if "|JLS".contains(chars_matrix[y][x]) {
                    inside = !inside
                }
            } else {
                if inside {
                    inside_count += 1;
                    inside_coords.push((x, y))
                }
            }
        }
    }
    if !picture {
        println!("Part 1: {:?} or {:?}", part1pos1, part1pos2);
        println!("Part 2: {}", inside_count);
    } else {
        const IMAGE_WIDTH: i32 = 140;
        const IMAGE_HEIGHT: i32 = 140;
        println!("P3\n{} {}\n255", IMAGE_WIDTH, IMAGE_HEIGHT);

        for y in 0..sketch.len() {
            for x in 0..sketch[y].len() {
                let (mut r, mut b, mut g) = (0, 0, 0);
                if loop_conns.contains_key(&(x, y)) {
                    r = 255
                }
                if inside_coords.contains(&(x, y)) {
                    b = 255
                }
                println!("{} {} {}", r, g, b);
            }
        }
    }
}

fn dfs(
    sketch: &Vec<Vec<Dirs>>,
    start: (usize, usize),
    visited: &mut HashMap<(usize, usize), usize>,
) -> HashMap<(usize, usize), (usize, usize)> {
    let mut stack = vec![];
    let mut connections = HashMap::new();
    stack.push((start, 0));
    while let Some(((x, y), d)) = stack.pop() {
        if visited.contains_key(&(x, y)) {
            continue;
        }
        visited.insert((x, y), d);
        let mut neighbours = vec![];
        let dirs = sketch[y][x];
        if dirs.north && y.checked_sub(1).is_some() && sketch[y - 1][x].south {
            neighbours.push((x, y - 1));
            connections.insert((x, y - 1), (x, y));
        }
        if dirs.east && x + 1 < sketch[y].len() && sketch[y][x + 1].west {
            neighbours.push((x + 1, y));
            connections.insert((x + 1, y), (x, y));
        }
        if dirs.south && y + 1 < sketch.len() && sketch[y + 1][x].north {
            neighbours.push((x, y + 1));
            connections.insert((x, y + 1), (x, y));
        }
        if dirs.west && x.checked_sub(1).is_some() && sketch[y][x - 1].east {
            neighbours.push((x - 1, y));
            connections.insert((x - 1, y), (x, y));
        }
        for neighbour in neighbours {
            stack.push((neighbour, d + 1))
        }
    }
    return connections;
}

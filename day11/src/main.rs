use itertools::Itertools;

fn main() {
    let mut grid: Vec<Vec<char>> = include_str!("../input.txt")
        .lines()
        .map(|l| l.chars().collect())
        .collect();
    let empty_rows: Vec<usize> = grid
        .iter()
        .enumerate()
        .filter(|(_, l)| l.iter().all(|&c| c == '.'))
        .map(|(i, _)| i)
        .collect();
    let empty_cols: Vec<usize> = (0..grid[0].len())
        .filter(|&c| (0..grid.len()).all(|r| grid[r][c] == '.'))
        .collect();

    let mut added = 0;
    for empty_row in empty_rows {
        grid.insert(
            empty_row + added,
            ".".repeat(grid[0].len()).chars().collect(),
        );
        added += 1
    }

    let mut added = 0;
    for col in empty_cols {
        for row in grid.iter_mut() {
            row.insert(col + added, '.')
        }
        added += 1;
    }

    let galaxy_coords: Vec<(usize, usize)> = (0..grid.len())
        .cartesian_product(0..grid[0].len())
        .filter(|&(y, x)| grid[y][x] == '#')
        .collect();

    let part1 = galaxy_coords
        .iter()
        .combinations(2)
        .fold(0, |sum, galaxies| {
            let (y1, x1) = galaxies[0];
            let (y2, x2) = galaxies[1];
            sum + y2.abs_diff(*y1) + x2.abs_diff(*x1)
        });
    println!("Part 1: {:?}", part1);

    // This works for part1 too just change the factor from 999999 factor to 1
    let grid: Vec<Vec<char>> = include_str!("../input.txt")
        .lines()
        .map(|l| l.chars().collect())
        .collect();

    let empty_rows: Vec<usize> = grid
        .iter()
        .enumerate()
        .filter(|(_, l)| l.iter().all(|&c| c == '.'))
        .map(|(i, _)| i)
        .collect();

    let empty_cols: Vec<usize> = (0..grid[0].len())
        .filter(|&c| (0..grid.len()).all(|r| grid[r][c] == '.'))
        .collect();

    let galaxy_coords: Vec<(usize, usize)> = (0..grid.len())
        .cartesian_product(0..grid[0].len())
        .filter(|&(y, x)| grid[y][x] == '#')
        .map(|(orgy, orgx)| {
            let yincrease = empty_rows.iter().filter(|&&r| r < orgy).count() * 999999;
            let xincrease = empty_cols.iter().filter(|&&c| c < orgx).count() * 999999;
            (orgy + yincrease, orgx + xincrease)
        })
        .collect();

    let part2 = galaxy_coords
        .iter()
        .combinations(2)
        .fold(0, |sum, galaxies| {
            let (y1, x1) = galaxies[0];
            let (y2, x2) = galaxies[1];
            sum + y2.abs_diff(*y1) + x2.abs_diff(*x1)
        });

    println!("Part 2: {}", part2)
}

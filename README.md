# 🎄 Advent of Code 2024

Welcome to my Advent of Code 2024 repository! This project contains my solutions for the daily coding challenges hosted by [Advent of Code](https://adventofcode.com/2024), solved using **Python 3.12**.

## 📂 Repository Structure

Each day’s puzzle solution is stored in its respective folder:

```graphql
📦 advent-of-code-2024
├── day_01
│   ├── part_1.py       # Code for part 1
│   └── part_2.py       # Code for part 2
├── day_02
│   ├── ...
└── README.md           # Main README
```

In accordance with the rules of this event, my input files (`input.txt`) are not included in this repository.

## 🌟 Challenges

- I challenge myself to implement the solutions using **only the Python standard library** so as to improve my knowledge and understanding of the language, while also developing problem-solving skills that can be applied to a wide range of situations.
- I try to be as concise and efficient as possible, while not disregarding readability.
- I do not use LLMs; only the Python documentation, StackOverflow and the [Advent of Code subreddit](https://www.reddit.com/r/adventofcode/) if I am stuck, or just for the memes.

## 🏆 Progress

| Day | Part 1 | Part 2 |
| --- | ------ | ------ |
| 1   | ✅     | ✅     |
| 2   | ✅     | ✅     |
| 3   | ✅     | ✅     |
| 4   | ✅     | ✅     |
| 5   | ✅     | ✅     |
| 6   | ✅     | ✅     |
| 7   | ✅     | ✅     |
| 8   | ✅     | ✅     |
| 9   | ✅     | ✅     |
| 10  | ✅     | ✅     |
| 11  | ✅     | ✅     |
| 12  | ✅     | ✅     |
| 13  | ⏳     | ⏳     |
| 14  | ⏳     | ⏳     |
| 15  | ⏳     | ⏳     |
| 16  | ⏳     | ⏳     |
| 17  | ⏳     | ⏳     |
| 18  | ⏳     | ⏳     |
| 19  | ⏳     | ⏳     |
| 20  | ⏳     | ⏳     |
| 21  | ⏳     | ⏳     |
| 22  | ⏳     | ⏳     |
| 23  | ⏳     | ⏳     |
| 24  | ⏳     | ⏳     |
| 25  | ⏳     | ⏳     |

### 📝 Implementation Notes

> [!WARNING]  
> The below section contains spoilers with possible approaches to solving the challenges, though other methods exist.

| Day | Part 1                                                                                                        | Part 2                                                                   |
| --- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 1   |                                                                                                               | Only a 4-line difference                                                 |
| 2   | _Reports_ can be sorted to check if _levels_ are gradually increasing or decreasing                           |                                                                          |
| 3   | Regular expressions and capturing groups                                                                      |                                                                          |
| 4   |                                                                                                               |                                                                          |
| 5   | Each _update_ operates on a directed acyclic graph, which gives the correct _page_ order to solve the problem | Only a 2-line difference                                                 |
| 6   |                                                                                                               | Exhaustive search (also known as brute-force)                            |
| 7   | `itertools.product` to get all possible operator combinations                                                 | Only a 3-line difference                                                 |
| 8   | `itertools.combinations` to get all possible _antenna_ pairs                                                  |                                                                          |
| 9   |                                                                                                               | Heaps with `heapq` to keep a sorted list of free space indices by length |
| 10  | Recursion                                                                                                     | Accidentally wrote the code for it while trying to do part 1             |
| 11  |                                                                                                               | Recursion + counter                                                      |
| 12  | Breadth-first search (BFS)                                                                                    | Counting convex/concave corners                                          |
| 13  |                                                                                                               |                                                                          |
| 14  |                                                                                                               |                                                                          |
| 15  |                                                                                                               |                                                                          |
| 16  |                                                                                                               |                                                                          |
| 17  |                                                                                                               |                                                                          |
| 18  |                                                                                                               |                                                                          |
| 19  |                                                                                                               |                                                                          |
| 20  |                                                                                                               |                                                                          |
| 21  |                                                                                                               |                                                                          |
| 22  |                                                                                                               |                                                                          |
| 23  |                                                                                                               |                                                                          |
| 24  |                                                                                                               |                                                                          |
| 25  |                                                                                                               |                                                                          |

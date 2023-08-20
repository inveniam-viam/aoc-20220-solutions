# Advent of Code 2022
# Problem 1

def process_elf_energies(filename: str) -> list[list[int]]:

    """Function to process the input file and calculate the energy supply carried by each elf."""

    calories =[]

    elf_calories = 0

    with open(filename, 'r', encoding="utf-8") as reader:

        for line in reader:
            if line != '\n':
                elf_calories += int(line)
            elif line == '\n':
                calories.append(elf_calories)
                elf_calories = 0
                continue
    return calories

def part_one(filename: str) -> int:

    """ Getting the elf with maximum energy supply"""

    elf_calories = process_elf_energies(filename)

    max_energy = 0
    max_index = 0

    for index, value in enumerate(elf_calories, start=1):
        if value > max_energy:
            max_energy = value
            max_index = index
    return max_index, max_energy

def part_two(filename: str) -> int:
    """Solving part 2 of the problem."""

    elf_calories = process_elf_energies(filename)

    elf_calories.sort(reverse=True)

    return sum(elf_calories[:3])


if __name__ == '__main__':

    INPUT_FILE_PATH = './inputs/problem1_input.txt'

    print("Part One Solution:")
    print(f"""Elf # {part_one(INPUT_FILE_PATH)[0]} carries the most energy supplies, at {part_one(INPUT_FILE_PATH)[1]} units.""")
    print("Part Two Solution:")
    print(f"The 3 elves carrying the most energy supplies carry a total of {part_two(INPUT_FILE_PATH)} units.")

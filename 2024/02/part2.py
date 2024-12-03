solution_answer = 4

def process_input(inputs: list[str]) -> int:
    safe_count = 0

    for line in inputs:
        print(line)

        print(report_safe(line))
        if report_safe(line):
            safe_count += 1
        else:
            for i in range(len(line.split())):
                if report_safe(" ".join([*line.split()[:i], *line.split()[i+1:]])):
                    safe_count += 1
                    break

    return safe_count


def report_safe(line: str) -> bool:
    readings = [int(reading) for reading in line.split()]
    increasing = readings[1] > readings[0]
    problem_dampener = False
    for i in range(len(readings) - 1):
        if not level_compare(readings[i], readings[i+1], increasing):
            return False

    
    return True
    
def level_compare(level1, level2, increasing):
    if abs(level1 - level2) > 3 or abs(level1 - level2) == 0:
        return False
    if (level2 > level1) != increasing:
        return False
    return True

if __name__ == "__main__":
    sample_answer = -100
    with open("sample_input.txt", "r") as input_file:
        sample_answer = process_input([line.strip() for line in input_file.readlines()])
        print(f"Solution to sample: `{sample_answer}` (expected `{solution_answer}`)")
    
    if sample_answer == solution_answer:
        with open("input.txt", "r") as input_file:
            print(f"Solution to puzzle: {process_input([line.strip() for line in input_file.readlines()])}")
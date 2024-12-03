solution_answer = 2

def process_input(inputs: list[str]) -> int:
    safe_count = 0

    for line in inputs:
        if report_safe(line):
            safe_count += 1

    return safe_count
        


def report_safe(line: str) -> bool:
    readings = [int(reading) for reading in line.split()]
    increasing = readings[1] > readings[0]
    for i in range(len(readings) - 1):
        if abs(readings[i] - readings[i+1]) > 3 or abs(readings[i] - readings[i+1]) == 0:
            return False
        if (readings[i+1] > readings[i]) != increasing:
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
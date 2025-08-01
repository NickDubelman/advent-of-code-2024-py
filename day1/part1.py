def load_input(filename='input.txt') -> tuple[list[int], list[int]]:
    with open(filename, 'r', encoding='utf-8') as f:
        lines_list = [list(map(int, line.split())) for line in f]
        col1, col2 = zip(*lines_list) # Transpose
        return list(col1), list(col2)


def main():
    (list1, list2) = load_input()

    list1_sorted, list2_sorted = sorted(list1), sorted(list2)

    distances = []
    for i in range(len(list1)):
        distances.append(abs(list1_sorted[i] - list2_sorted[i]))

    print(sum(distances))

if __name__ == "__main__":
    main()
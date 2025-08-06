from part1 import load_input

"""
similarity score = add up each number in the left list after multiplying it by the number of times
that number appears in the right list
"""

def main():
    (list1, list2) = load_input()

    similarities = []
    for i in range(len(list1)):
        left_num = list1[i]
        similarities.append(list2.count(left_num) * left_num)

    print(sum(similarities))

if __name__ == "__main__":
    main()
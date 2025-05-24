def find_sum_pairs_for_range(target_sum):
    """
    Finds pairs of numbers from the range(target_sum) that add up to target_sum.
    """
    integers = list(range(target_sum))
    pairs = []
    for i in range(len(integers)):
        for j in range(i + 1, len(integers)):
            if integers[i] + integers[j] == target_sum:
                pairs.append((integers[i], integers[j]))
    return pairs

if __name__ == "__main__":
    while True:
        try:
            user_sum = int(input("Bitte geben Sie die Summe ein, die Sie erreichen möchten: "))
            break
        except ValueError:
            print("Bitte gib eine ganze Zahl ein.")

    found_pairs = find_sum_pairs_for_range(user_sum)

    for pair in found_pairs:
        print(f"{user_sum} = {pair[0]} + {pair[1]}")

    if user_sum % 2 == 0:
        # This handles the case where the sum can be formed by two equal numbers.
        # The find_sum_pairs_for_range function will not find this pair if target_sum / 2 is an integer,
        # because j starts from i + 1.
        # For example, for target_sum = 6, integers = [0,1,2,3,4,5]
        # find_sum_pairs_for_range(6) returns [(1,5), (2,4)]
        # The original code explicitly prints "6 = 3 + 3"
        # We need to ensure this logic is preserved.
        # The problem description states the function should just return the list of pairs,
        # and the main script handles the specific even sum print.
        # So, if target_sum is 6, the function returns [(1,5), (2,4)].
        # The loop prints:
        # 6 = 1 + 5
        # 6 = 2 + 4
        # Then this specific print statement adds:
        # 6 = 3 + 3
        # This seems correct according to the instructions.
        print(f"{user_sum} = {user_sum // 2} + {user_sum // 2}")
x = [1, 2, 3, 4, 5]

def swap(input, idx_A, idx_B):
    temp_idx = input[idx_A]
    input[idx_A] = input[idx_B]
    input[idx_B] = temp_idx
    return input

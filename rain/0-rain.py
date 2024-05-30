#!/usr/bin/python3


"""
Module: rain

def rain(walls):
    """
    Calculate the total amount of rainwater retained.

    Args:
    walls (list): A list of non-negative integers representing the heights of walls.

    Returns:
    int: Total amount of rainwater retained.
    """
    if not walls:
        return 0
    
    n = len(walls)
    if n < 3:
        return 0  # Not enough walls to trap any water

    left_max = [0] * n
    right_max = [0] * n
    
    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])
    
    # Fill right_max array
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])
    
    # Calculate total trapped water
    total_water = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        total_water += max(0, water_level - walls[i])
    
    return total_water

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([], 0),
        ([2, 0, 2], 2),
        ([0, 1, 0, 2, 0, 3, 0, 4], 6),
        ([1, 1, 2, 0, 1, 1, 1], 1),
        ([0, 2, 1, 0, 1, 3, 1, 2, 1, 1, 2, 1], 8),
        ([2, 0, 0, 0, 0, 3, 0], 10),
        ([1], 0),
        ([3, 3], 0)
    ]

    for walls, expected in test_cases:
        result = rain(walls)
        print(f"rain({walls}) = {result}, expected = {expected}, {'PASS' if result == expected else 'FAIL'}")

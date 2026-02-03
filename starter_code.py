"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])


def count_even(numbers):
    if len(numbers) == 0:
        return 0
    
    first_is_even = 1 if numbers[0] % 2 == 0 else 0
    return first_is_even + count_even(numbers[1:])


def find_strings_with(strings, target):
    if len(strings) == 0:
        return []
    
    if target in strings[0]:
        return [strings[0]] + find_strings_with(strings[1:], target)
    else:
        return find_strings_with(strings[1:], target)


# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    if not os.path.isdir(directory_path):
        return 0
    
    total_files = 0
    
    try:
        items = os.listdir(directory_path)
        
        for item in items:
            item_path = os.path.join(directory_path, item)
            
            if os.path.isfile(item_path):
                total_files += 1
            elif os.path.isdir(item_path):
                total_files += count_files(item_path)
    except (PermissionError, OSError):
        return 0
    
    return total_files


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    infected_files = []
    
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            infected_files.append(directory_path)
        return infected_files
    
    if not os.path.isdir(directory_path):
        return infected_files
    
    try:
        items = os.listdir(directory_path)
        
        for item in items:
            item_path = os.path.join(directory_path, item)
            
            if os.path.isfile(item_path):
                if item_path.endswith(extension):
                    infected_files.append(item_path)
            elif os.path.isdir(item_path):
                infected_files.extend(find_infected_files(item_path, extension))
    except (PermissionError, OSError):
        pass
    
    return infected_files


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================


if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE")
    print("Complete the functions above, then run this file to test your work.\n")
    
    
    print("\nTest sum_list:")
    print(f"  sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])} (expected: 10)")
    print(f"  sum_list([]) = {sum_list([])} (expected: 0)")
    print(f"  sum_list([5, 5, 5]) = {sum_list([5, 5, 5])} (expected: 15)")


    print("\nTest count_even:")
    print(f"  count_even([1, 2, 3, 4, 5, 6]) = {count_even([1, 2, 3, 4, 5, 6])} (expected: 3)")
    print(f"  count_even([1, 3, 5]) = {count_even([1, 3, 5])} (expected: 0)")
    print(f"  count_even([2, 4, 6]) = {count_even([2, 4, 6])} (expected: 3)")

    print("\nTest find_strings_with:")
    result = find_strings_with(["hello", "world", "help", "test"], "hel")
    print(f"  find_strings_with(['hello', 'world', 'help', 'test'], 'hel') = {result}")
    print(f"  (expected: ['hello', 'help'])")
        
    result = find_strings_with(["cat", "dog", "bird"], "z")
    print(f"  find_strings_with(['cat', 'dog', 'bird'], 'z') = {result}")
    print(f"  (expected: [])")
    
    
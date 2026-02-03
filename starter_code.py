"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    
    This is your first recursion problem. Think about:
    - Base case: What's the sum of an empty list?
    - Recursive case: If you know the sum of the rest of the list,
      how do you include the first number?
    
    Args:
        numbers (list): List of numbers to sum
    
    Returns:
        int: Sum of all numbers in the list
    
    Example:
        sum_list([1, 2, 3, 4]) should return 10
        sum_list([]) should return 0
    """
    # TODO: Implement this function
    # Hint: if len(numbers) == 0, return 0
    # Otherwise, return numbers[0] + sum_list(numbers[1:])
    
    pass

# Uncomment to test sum_list
# print("\nTest sum_list:")
# print(f"  sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])} (expected: 10)")
# print(f"  sum_list([]) = {sum_list([])} (expected: 0)")
# print(f"  sum_list([5, 5, 5]) = {sum_list([5, 5, 5])} (expected: 15)")


def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    
    This teaches you how to count items that match a condition.
    You'll use this same pattern for counting files!
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int: Count of even numbers in the list
    
    Example:
        count_even([1, 2, 3, 4, 5, 6]) should return 3
        count_even([1, 3, 5]) should return 0
    """
    # TODO: Implement this function
    # Hint: Base case is empty list (return 0)
    # If first number is even, add 1 to count from rest of list
    # If first number is odd, just return count from rest of list
    
    pass

# Uncomment to test count_even
# print("\nTest count_even:")
# print(f"  count_even([1, 2, 3, 4, 5, 6]) = {count_even([1, 2, 3, 4, 5, 6])} (expected: 3)")
# print(f"  count_even([1, 3, 5]) = {count_even([1, 3, 5])} (expected: 0)")
# print(f"  count_even([2, 4, 6]) = {count_even([2, 4, 6])} (expected: 3)")

def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    
    This teaches you how to build a list of items that match a condition.
    You'll use this same pattern for finding infected files!
    
    Args:
        strings (list): List of strings to search
        target (str): Substring to search for
    
    Returns:
        list: All strings that contain the target substring
    
    Example:
        find_strings_with(["hello", "world", "help"], "hel") 
        should return ["hello", "help"]
    """
    # TODO: Implement this function
    # Hint: Base case is empty list (return [])
    # If first string contains target, add it to results from rest of list
    # Otherwise, just return results from rest of list
    # Use: if target in strings[0]
    
    pass

# Uncomment to test find_strings_with
# print("\nTest find_strings_with:")
# result = find_strings_with(["hello", "world", "help", "test"], "hel")
# print(f"  find_strings_with(['hello', 'world', 'help', 'test'], 'hel') = {result}")
# print(f"  (expected: ['hello', 'help'])")
    
# result = find_strings_with(["cat", "dog", "bird"], "z")
# print(f"  find_strings_with(['cat', 'dog', 'bird'], 'z') = {result}")
# print(f"  (expected: [])")

# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    
    Args:
        directory_path (str): Path to the directory to analyze
    
    Returns:
        int: Total number of files in the directory tree
    
    Example:
        If directory structure is:
        root/
            file1.txt
            file2.txt
            subdir/
                file3.txt
        
        count_files('root') should return 3
    """
    # TODO: Implement this function
    # Hints:
    # 1. What is the base case? (What if directory_path is a file, not a directory?)
    # 2. How do you list items in a directory? (Check Resource 3)
    # 3. For each item, is it a file or directory? Recursively handle directories.
    # 4. How do you combine the results?
    
    pass


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    
    Args:
        directory_path (str): Path to the directory to analyze
        extension (str): File extension to search for (default: ".encrypted")
    
    Returns:
        list: List of full paths to all files with the specified extension
    
    Example:
        If directory structure is:
        root/
            normal.txt
            virus.encrypted
            subdir/
                data.encrypted
        
        find_infected_files('root', '.encrypted') should return:
        ['root/virus.encrypted', 'root/subdir/data.encrypted']
    """
    # TODO: Implement this function
    # Hints:
    # 1. Base case: If it's a file, check if it has the extension
    # 2. Recursive case: If it's a directory, check all items inside
    # 3. You'll need to build and return a list of matching file paths
    # 4. Use os.path.join() to create full paths
    
    pass


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================


if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE")
    print("Complete the functions above, then run this file to test your work.\n")
    
    ## 1. Uncomment to run tests for count_files functions
    # print("Total files (Test Case 1):", count_files("test_cases/case1_flat")) # 5
    # print("Total files (Test Case 2):", count_files("test_cases/case2_nested")) # 4
    # print("Total files (Test Case 3):", count_files("test_cases/case3_infected")) # 5

    ## 2. Uncomment to run count_files for breached files
    # print("Total files (breeched files):", count_files("breach_data")) # ???

    ## 3. Uncomment to run tests for find_infected_files function
    # print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case1_flat"))) # 0
    # print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case2_nested"))) # 0
    # print("Total Infected Files (Test Case 3):", len(find_infected_files("test_cases/case3_infected"))) # 3

    ## 4. Uncomment to run find_infected breached files
    # print("Total Infected Files (breached files):", len(find_infected_files("breach_data"))) # ???

    ## 5. Determine how many files were corrupted by department (Finance, HR, and Sales)
    


    
    print("\n⚠ Uncomment the test functions in the main block to run tests!")
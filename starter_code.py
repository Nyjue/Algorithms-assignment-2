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
    print("RECURSION ASSIGNMENT - FINDING INFECTED FILES")
    print("Testing find_infected_files function\n")
    
    # First, let's create the test directory structure manually
    # so we have predictable test results
    
    # Clean up old test directories if they exist
    import shutil
    if os.path.exists("test_cases"):
        shutil.rmtree("test_cases")
    
    # Create test directory structure
    print("Creating test directories...")
    
    # Test Case 1: Simple flat structure (no encrypted files)
    case1 = "test_cases/case1_flat"
    os.makedirs(case1)
    for i in range(5):
        with open(os.path.join(case1, f"file{i}.txt"), 'w') as f:
            f.write("test")
    
    # Test Case 2: One level of nesting (no encrypted files)
    case2 = "test_cases/case2_nested"
    os.makedirs(case2)
    with open(os.path.join(case2, "root_file.txt"), 'w') as f:
        f.write("test")
    
    subdir = os.path.join(case2, "subdir")
    os.makedirs(subdir)
    for i in range(3):
        with open(os.path.join(subdir, f"nested_file{i}.txt"), 'w') as f:
            f.write("test")
    
    # Test Case 3: Multiple levels with .encrypted files
    case3 = "test_cases/case3_infected"
    os.makedirs(case3)
    with open(os.path.join(case3, "normal.txt"), 'w') as f:
        f.write("test")
    with open(os.path.join(case3, "infected1.encrypted"), 'w') as f:
        f.write("test")
    
    level1 = os.path.join(case3, "level1")
    os.makedirs(level1)
    with open(os.path.join(level1, "data.encrypted"), 'w') as f:
        f.write("test")
    
    level2 = os.path.join(level1, "level2")
    os.makedirs(level2)
    with open(os.path.join(level2, "deep.txt"), 'w') as f:
        f.write("test")
    with open(os.path.join(level2, "virus.encrypted"), 'w') as f:
        f.write("test")
    
    print("✓ Test directories created successfully!")
    
    print("\n" + "="*60)
    print("TESTING find_infected_files FUNCTION")
    print("="*60)
    
    ## 1. Test find_infected_files on test cases
    print("\n1. Testing on test cases:")
    print("-" * 40)
    
    # Test Case 1: Should return 0 infected files
    infected_case1 = find_infected_files("test_cases/case1_flat")
    print(f"Test Case 1 (case1_flat): {len(infected_case1)} infected files")
    print(f"  Expected: 0")
    print(f"  Result: {'✓ PASS' if len(infected_case1) == 0 else '✗ FAIL'}")
    
    # Test Case 2: Should return 0 infected files
    infected_case2 = find_infected_files("test_cases/case2_nested")
    print(f"\nTest Case 2 (case2_nested): {len(infected_case2)} infected files")
    print(f"  Expected: 0")
    print(f"  Result: {'✓ PASS' if len(infected_case2) == 0 else '✗ FAIL'}")
    
    # Test Case 3: Should return 3 infected files
    infected_case3 = find_infected_files("test_cases/case3_infected")
    print(f"\nTest Case 3 (case3_infected): {len(infected_case3)} infected files")
    print(f"  Expected: 3")
    print(f"  Result: {'✓ PASS' if len(infected_case3) == 3 else '✗ FAIL'}")
    
    # Show the actual infected files found in test case 3
    if infected_case3:
        print(f"\n  Found these infected files:")
        for i, file in enumerate(infected_case3, 1):
            print(f"  {i}. {file}")
    
    ## 2. Test find_infected_files on breach_data
    print("\n" + "="*60)
    print("ANALYZING breach_data DIRECTORY")
    print("="*60)
    
    # Check if breach_data directory exists
    if os.path.exists("breach_data"):
        print("\nbreach_data directory found. Analyzing infected files...")
        
        # Count total files first
        total_files = count_files("breach_data")
        print(f"\nTotal files in breach_data: {total_files}")
        
        # Find all infected files
        infected_breach_files = find_infected_files("breach_data")
        infected_count = len(infected_breach_files)
        
        print(f"\nTotal infected files in breach_data: {infected_count}")
        
        if infected_breach_files:
            print(f"\nInfected files found ({infected_count} total):")
            for i, file in enumerate(infected_breach_files[:10], 1):  # Show first 10
                print(f"  {i}. {file}")
            
            if infected_count > 10:
                print(f"  ... and {infected_count - 10} more")
            
            # Calculate infection rate
            if total_files > 0:
                infection_rate = (infected_count / total_files) * 100
                print(f"\nInfection rate: {infection_rate:.1f}%")
        
        # Count infected files by department
        print("\n" + "-" * 40)
        print("Infected files by department:")
        print("-" * 40)
        
        departments = ['Finance', 'HR', 'Sales', 'Marketing', 'Operations', 'Creative']
        department_counts = {}
        
        for dept in departments:
            # Count infected files that have department name in path
            dept_infected = [f for f in infected_breach_files if dept in f]
            if dept_infected:
                department_counts[dept] = len(dept_infected)
                print(f"  {dept}: {len(dept_infected)} infected files")
        
        # Find most affected department
        if department_counts:
            most_affected = max(department_counts.items(), key=lambda x: x[1])
            print(f"\nMost affected department: {most_affected[0]} with {most_affected[1]} infected files")
    
    else:
        print("\n⚠ WARNING: breach_data directory not found!")
        print("To test with breach_data:")
        print("1. Make sure the breach_data directory exists in the same folder")
        print("2. Or run the test data generation code first")
        print("\nFor now, testing with the existing test cases only.")
    
    print("\n" + "="*60)
    print("TESTING COMPLETE")
    print("="*60)
    
    print("\n📊 SUMMARY FOR REFLECTION:")
    print("-" * 30)
    
    # Show test case results
    print(f"Test Case 1 infected files: {len(infected_case1)} (expected: 0)")
    print(f"Test Case 2 infected files: {len(infected_case2)} (expected: 0)")
    print(f"Test Case 3 infected files: {len(infected_case3)} (expected: 3)")
    
    # Show breach_data results if available
    if os.path.exists("breach_data"):
        total_files = count_files("breach_data")
        infected_count = len(find_infected_files("breach_data"))
        print(f"\nbreach_data results:")
        print(f"  Total files: {total_files}")
        print(f"  Infected files: {infected_count}")
        if total_files > 0:
            infection_rate = (infected_count / total_files) * 100
            print(f"  Infection rate: {infection_rate:.1f}%")
    
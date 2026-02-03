"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os
import shutil
import random

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
# TEST DIRECTORY GENERATION FUNCTIONS
# ============================================================================

def generate_breach_data():
    """Generate a simulated compromised file system for analysis."""
    root_path = "breach_data"
    max_depth = 4
    max_files = 8
    max_dirs = 3
    
    # Clean up existing directory if it exists
    if os.path.exists(root_path):
        shutil.rmtree(root_path)
    
    # Create root directory
    os.makedirs(root_path)
    
    # File extensions (simulating a marketing firm's files)
    normal_extensions = ['.pdf', '.docx', '.xlsx', '.pptx', '.jpg', '.png', '.mp4', '.txt']
    encrypted_extension = '.encrypted'
    
    # Department/folder names for realistic structure
    departments = ['Marketing', 'Sales', 'Creative', 'Finance', 'HR', 'Operations']
    project_names = ['Q1_Campaign', 'Q2_Campaign', 'Q3_Campaign', 'Q4_Campaign', 
                     'Client_Projects', 'Internal_Docs', 'Archive', 'Drafts']
    
    file_types = ['report', 'presentation', 'budget', 'photo', 'video', 'contract', 
                  'invoice', 'memo', 'brief', 'strategy']
    
    def create_structure(current_path, current_depth):
        """Recursively create directory structure with files."""
        if current_depth >= max_depth:
            return
        
        # Create files in current directory
        num_files = random.randint(2, max_files)
        for i in range(num_files):
            # 30% chance of being encrypted
            if random.random() < 0.3:
                extension = encrypted_extension
            else:
                extension = random.choice(normal_extensions)
            
            file_name = f"{random.choice(file_types)}_{random.randint(1000, 9999)}{extension}"
            file_path = os.path.join(current_path, file_name)
            
            # Create empty file
            with open(file_path, 'w') as f:
                f.write(f"Mock content for {file_name}\n")
        
        # Create subdirectories
        if current_depth < max_depth - 1:
            num_dirs = random.randint(1, max_dirs)
            for i in range(num_dirs):
                if current_depth == 0:
                    dir_name = random.choice(departments)
                elif current_depth == 1:
                    dir_name = random.choice(project_names)
                else:
                    dir_name = f"Subfolder_{random.randint(100, 999)}"
                
                dir_path = os.path.join(current_path, dir_name)
                
                # Avoid duplicate directory names
                counter = 1
                while os.path.exists(dir_path):
                    dir_path = os.path.join(current_path, f"{dir_name}_{counter}")
                    counter += 1
                
                os.makedirs(dir_path)
                create_structure(dir_path, current_depth + 1)
    
    print("Generating compromised file system...")
    create_structure(root_path, 0)
    
    # Count total files and infected files
    total_files = 0
    infected_files = 0
    
    for root, dirs, files in os.walk(root_path):
        total_files += len(files)
        infected_files += len([f for f in files if f.endswith('.encrypted')])
    
    print(f"✓ File system generated at: {root_path}/")
    print(f"✓ Total files: {total_files}")
    print(f"✓ Infected files (.encrypted): {infected_files}")
    print(f"✓ Infection rate: {infected_files/total_files*100:.1f}%")
    print("\nYou can now implement your recursive functions to analyze this breach!")

def generate_test_cases():
    """Generate small test cases with known answers."""
    test_dir = "test_cases"
    
    # Clean up existing test directory
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    # Test Case 1: Simple flat structure
    case1 = os.path.join(test_dir, "case1_flat")
    os.makedirs(case1)
    for i in range(5):
        with open(os.path.join(case1, f"file{i}.txt"), 'w') as f:
            f.write("test")
    
    # Test Case 2: One level of nesting
    case2 = os.path.join(test_dir, "case2_nested")
    os.makedirs(case2)
    with open(os.path.join(case2, "root_file.txt"), 'w') as f:
        f.write("test")
    
    subdir = os.path.join(case2, "subdir")
    os.makedirs(subdir)
    for i in range(3):
        with open(os.path.join(subdir, f"nested_file{i}.txt"), 'w') as f:
            f.write("test")
    
    # Test Case 3: Multiple levels with .encrypted files
    case3 = os.path.join(test_dir, "case3_infected")
    os.makedirs(case3)
    with open(os.path.join(case3, "normal.txt"), 'w') as f:
        f.write("test")
    with open(os.path.join(case3, "infected.encrypted"), 'w') as f:
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
    
    print(f"\n✓ Test cases generated at: {test_dir}/")
    print("\nTest Case 1 (case1_flat): 5 files, max depth 0")
    print("Test Case 2 (case2_nested): 4 files total (1 root + 3 in subdir), max depth 1")
    print("Test Case 3 (case3_infected): 5 files total, 3 .encrypted files, max depth 2")


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================

if __name__ == "__main__":
    # Generate test directories first
    generate_test_cases()
    print("\n" + "="*60 + "\n")
    generate_breach_data()
    
    print("\n" + "="*60)
    print("RUNNING TESTS")
    print("="*60)
    
    # Test the recursive warm-up functions
    print("\n=== PART 1: RECURSION WARM-UPS ===")
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
    
    print("\n" + "="*60)
    print("=== PART 2 & 3: FILE SYSTEM TESTS ===")
    print("="*60)
    
    ## 1. Test count_files function on test cases
    print("\n1. Testing count_files on test cases:")
    print(f"   Total files (Test Case 1): {count_files('test_cases/case1_flat')} (expected: 5)")
    print(f"   Total files (Test Case 2): {count_files('test_cases/case2_nested')} (expected: 4)")
    print(f"   Total files (Test Case 3): {count_files('test_cases/case3_infected')} (expected: 5)")
    
    ## 2. Test count_files on breach_data
    print("\n2. Testing count_files on breach_data:")
    print(f"   Total files (breach_data): {count_files('breach_data')}")
    
    ## 3. Test find_infected_files function on test cases
    print("\n3. Testing find_infected_files on test cases:")
    infected_case1 = find_infected_files("test_cases/case1_flat")
    print(f"   Infected files (Test Case 1): {len(infected_case1)} (expected: 0)")
    
    infected_case2 = find_infected_files("test_cases/case2_nested")
    print(f"   Infected files (Test Case 2): {len(infected_case2)} (expected: 0)")
    
    infected_case3 = find_infected_files("test_cases/case3_infected")
    print(f"   Infected files (Test Case 3): {len(infected_case3)} (expected: 3)")
    
    ## 4. Test find_infected_files on breach_data
    print("\n4. Testing find_infected_files on breach_data:")
    infected_breach_files = find_infected_files("breach_data")
    print(f"   Total Infected Files (breach_data): {len(infected_breach_files)}")
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    # Display final counts
    total_breach_files = count_files("breach_data")
    total_infected = len(infected_breach_files)
    
    print(f"\nTotal files in breach_data: {total_breach_files}")
    print(f"Total infected files in breach_data: {total_infected}")
    
    if total_breach_files > 0:
        infection_rate = (total_infected / total_breach_files) * 100
        print(f"Infection rate: {infection_rate:.1f}%")
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED!")
    print("="*60)
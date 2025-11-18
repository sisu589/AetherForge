from functions.get_files_info import get_files_info

# Test 1: Current directory
print('get_files_info("calculator", "."):\nResult for current directory:')
result = get_files_info("calculator", ".")
print(result)
print()

# Test 2: pkg subdirectory
print('get_files_info("calculator", "pkg"):\nResult for \'pkg\' directory:')
result = get_files_info("calculator", "pkg")
print(result)
print()

# Test 3: Absolute path outside working directory
print('get_files_info("calculator", "/bin"):\nResult for \'/bin\' directory:')
result = get_files_info("calculator", "/bin")
print(f"    {result}")
print()

# Test 4: Relative path outside working directory
print('get_files_info("calculator", "../"):\nResult for \'../\' directory:')
result = get_files_info("calculator", "../")
print(f"    {result}")
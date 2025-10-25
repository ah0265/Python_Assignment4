file_name = "sample.txt"
try:
    fh = open(file_name, "rt")
    print("Reading file content:")
    i = 1
    lines = fh.readlines()
    for i  in range(0,len(lines)):
        print(f"Line {i+1}: {lines[i]}", end="")
    fh.close()
        
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

    
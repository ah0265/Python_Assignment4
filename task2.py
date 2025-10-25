file_name = "output.txt"
fh = open(file_name, "at")
data1 = input("Enter text to write to the file: ")
fh.write(data1)
print(f"Data succesfully written to {file_name}.\n")
data2 = input("Enter additional text to append: ")
fh.write(f"\n{data2}")
print(f"Data successfully appended.\n")
fh.close()

fh = open(file_name, "rt")
print(f"Final content of {file_name}:")
output = fh.readlines()
for i in range(0,len(output)):
    print(f"{output[i]}", end="")
fh.close()
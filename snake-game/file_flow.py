## READ FILE

with open("file_name") as file:
    content = file.read()
    print(content)


## WRITE FILE

## Mode types:
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)

with open("file_name", mode="a") as file:
    file.write("test\n")

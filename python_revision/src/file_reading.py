import mmap

# Open a file in read-only mode
with open('example.txt', 'r') as f:
    # Create a memory map of the file
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

    # Access the mapped file using a pointer or other indexing methods
    print(m.read(10))

    # Close the memory map
    m.close()

# Open a file in read-write mode
with open('example.txt', 'r+b') as f:
    # Create a memory map of the file
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ | mmap.ACCESS_WRITE)

    # Access the mapped file using a pointer or other indexing methods
    print(m.read(10))

    # Modify some data in the mapped file
    m[10] = b'new data'

    # Close the memory map
    m.close()
numbers = [10, 20, 30, 40, 50]

# Take an iterator from the list.

iterator = iter(numbers)
print("Iterator object created.")

while True:
    try:
        print("Calling next...")
        item = next(iterator)
        print("Got item:", item)
        
    except StopIteration:
        print("No more items. StopIteration called")
        break
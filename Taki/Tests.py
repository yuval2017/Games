import random

def choose_random_and_remove(arr):
    if not arr:
        return None  # Return None if the array is empty

    # Step 1: Generate a random index
    random_index = random.randint(0, len(arr) - 1)

    # Step 2: Get the element at the random index
    random_element = arr[random_index]

    # Step 3: Remove the element from the array
    del arr[random_index]

    return random_element

# Example usage
my_array = [1, 2, 3, 4, 5]
random_element = choose_random_and_remove(my_array)

print(f"Randomly chosen element: {random_element}")
print(f"Array after removal: {my_array}")
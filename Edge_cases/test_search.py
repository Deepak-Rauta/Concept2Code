import pytest
from search import binary_search

# We define the variables; array, target to find, and expected index
@pytest.mark.parametrize("arr, target, expected", [
    # Normal cases (Happy Path)
    ([1, 2, 3, 4, 5], 3, 2),  # Target in the middle
    ([1, 2, 3, 4, 5], 1, 0),  # Target at the beginning
    ([1, 2, 3, 4, 5], 5, 4),  # Target at the end

    # Target not found
    ([1, 2, 3, 4, 5], 10, -1),  # Target larger than all
    ([1, 2, 3, 4, 5], -5, -1),  # Target smaller than all

    # Edge Cases
    ([], 5, -1),  # Empty array
    ([7], 7, 0),  # Single element array (Target exists)
    ([7], 3, -1), # Single element array (Target missing)

    # Extreme/Large numbers
    ([1000000, 2000000, 3000000], 2000000, 1)


])

def test_binary_search_scenarios(arr, target, expected):
    result = binary_search(arr, target)
    assert result == expected



# [
#     # NORMAL CASES (The "Happy Path")
#     # Structure: ([array], target, expected_index)
    
#     # The array has 5 items. The number 3 is at index 2.
#     ([1, 2, 3, 4, 5], 3, 2),  
    
#     # The number 1 is the very first item, so we expect index 0.
#     ([1, 2, 3, 4, 5], 1, 0),  
    
#     # The number 5 is the very last item, so we expect index 4.
#     ([1, 2, 3, 4, 5], 5, 4),  

#     # ---------------------------------------------------------
#     # TARGET NOT FOUND
#     # If a number is missing, our binary search returns -1.
    
#     # 10 is not in the list. We expect the function to return -1.
#     ([1, 2, 3, 4, 5], 10, -1), 
    
#     # -5 is not in the list. We expect the function to return -1.
#     ([1, 2, 3, 4, 5], -5, -1), 

#     # ---------------------------------------------------------
#     # EDGE CASES (The tricky boundaries)
    
#     # The list is completely empty. 5 cannot be in it. Expect -1.
#     ([], 5, -1),  
    
#     # The list only has one item. We are looking for 7. It is at index 0.
#     ([7], 7, 0),  
    
#     # The list only has one item (7). We are looking for 3. Expect -1.
#     ([7], 3, -1), 

#     # ---------------------------------------------------------
#     # EXTREME NUMBERS (Testing scalability)
    
#     # The numbers are huge, but the logic remains the same. 
#     # 2,000,000 is in the middle of the list, which is index 1.
#     ([1000000, 2000000, 3000000], 2000000, 1)
# ]

"""It automates the testing
The real magic is the @pytest.mark.parametrize part. It tells pytest: "Hey, look at this list of 9 scenarios. I want you to run the test_binary_search_scenarios function 9 times in a row. Every time you run it, plug in the next scenario from the list and check if the function gets the right answer."

Basically, this code allows you to write the test logic only once, but run it 9 different times with completely different data to make sure your search function is bulletproof."""
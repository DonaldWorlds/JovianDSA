#from mybinarysearch import locate_card
import mybinarysearch

# Test for Query in the middle 

# Test for Query in the middle
def occurs_in_the_middle():
    cards = [13, 11, 10, 7, 4, 3, 1, 0]
    query = 7
    expected_index = 3
    results = mybinarysearch.locate_cards_four(cards,query)
    
    # Check if the assertion passes
    assert results == expected_index, f"Expected {expected_index}, but got {results}"
    print(f"Test 1 passed: Expected {expected_index}, got {results}")

occurs_in_the_middle()
print()

# test is the query is th first element 
def occurs_in_the_first():
    cards = [4,2,1,-1]
    query = 4
    expected_indexed_output = 0
    #check if the assertion passes
    
    results = mybinarysearch.locate_cards_four(cards,query)
    
    assert results == expected_indexed_output, f"Expected {expected_indexed_output}, but got {results} fix your inputs and outputs" # This wil be the function call 
    print(f"Test 2 passed with values expexted as {expected_indexed_output} and {results} as results")
    
# dont forget to call the method
occurs_in_the_first()
print()

# test if the query is the last element 
def occurs_in_the_last():
    cards = [3,-1,-9,-127]
    query = -127
    expected_indexed_output = 3
    results = mybinarysearch.locate_cards_four(cards,query)
    assert results == expected_indexed_output, f"Expected {expected_indexed_output}, but got {results}"
    print(f"Test 3 passed with expected index as {expected_indexed_output} and results as {results} ") 

occurs_in_the_last()
print()


# test is cards contain just one element 
def contains_one():
    cards = [6]
    query = 0
    expected_indexed_output = 0
    
    results = mybinarysearch.locate_cards_four(cards,query)
    assert results == expected_indexed_output,f"Expected {expected_indexed_output}, but got {results}" # This will be the function call
    print(f"Test 4 passed with expected {expected_indexed_output} and reults as {results}")
print()


# cards does not contain query 
def does_not_contain_query():
    cards = [9,7,5,2,-9]
    query = -4
    expected_indexed_output = -1
    results = mybinarysearch.locate_cards_four(cards,query)
    assert results == expected_indexed_output, f"Expected {expected_indexed_output}, but got {results}" 
    print(f"Test 5 passed with expected {expected_indexed_output} and results as {results}")


does_not_contain_query()
print()


# This originally caused an error that we fixed 
def empty_cards():
    cards = []
    query = 7
    expected_indexed_output = -1
    print("Calling locate_card function...")
    results = mybinarysearch.locate_cards_four(cards, query)
    assert results == expected_indexed_output, f"Expected {expected_indexed_output}, got {results}"
    print(f"Test 6 passed with expected {expected_indexed_output} and results as {results}")

empty_cards()
print()





# numbers are repeated in cards 
def repeated_number_in_cards_two():
    cards = [8,8,6,6,6,6,6,3,2,2,2,0,0,0]
    query = 3
    expected_indexed_output = 7
    results = mybinarysearch.locate_cards_four(cards,query)
    assert results == expected_indexed_output,f"Expected {expected_indexed_output}, got {results}" # This will be the function call 
    print(f"Test 7 passed with expected {expected_indexed_output} and results as {results}")
    
repeated_number_in_cards_two()
print()




#query occurs multiple times 

#This will fail because it is not picking up the first occurence of our query 6 thats why out expected is 2 but got 9 for our index counting from zero
# we will fix this later down the line. 
def query_occurs_multiple_times():
    cards = [8,8,6,6,6,6,6,6,3,2,2,2,0,0,0]
    query = 2
    expected_indexed_output = 2 # the index counting from zero
    results = mybinarysearch.locate_cards_four(cards,query)
    assert results == expected_indexed_output, f"Expected {expected_indexed_output}, got {results}" # this will be the function call
    print(f"Test 8 passed with expected {expected_indexed_output} ans results as {results}")
    
query_occurs_multiple_times() 
print()




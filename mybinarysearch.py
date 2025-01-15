


"""This is the signaure and the bruteforce solution"""

def locate_card(cards,query):
    # This will be for the position of the array 
    position = 0 
    
    
    #set the while loop to loop through the cards 
    while True:
        # cards is an array and we will check to see if it is equal to out query and or target number 
        if cards[position] == query:
            #Answer found! Return and exit 
            return position
        
        #Increment the position 
        position += 1
        
        
        # Check if we have reached the end of the array 
        if position == len(cards):
            #Number not found, return -1
            return -1

#This is the function to debug the empty cards
def locate_cards_two(cards,query):
    position = 0
    
    #Print statement for the for the input and the value of the position
    print("cards",cards)
    print("query",query)
    
    while True:
        #Print the position 
        print("position",position)
        
        if cards[position] == query:
            return position
        
        position += 1
        
        #return -1 if the query position is not in the cards
        if position == len(cards):
            return -1



        
# Test for empty cards
cards = []
query = 7

# Call the function with empty cards
#result = locate_cards_two(cards, query)

# Print the final result
#print(f"Final result: {result}")
    
    
def locate_cards_three(cards,query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


# Binary Search Algorithm

# When the list is sorted in ascending order:
# - If the middle value is equal to the query, return the middle value.
# - If the middle value is less than the query, search the right half, so set low = middle_index + 1.
# - If the middle value is greater than the query, search the left half, so set high = middle_index - 1.

# When the list is sorted in descending order:
# - If the middle value is equal to the query, return the middle value.
# - If the middle value is less than the query, search the left half, so set high = middle_index - 1.
# - If the middle value is greater than the query, search the right half, so set low = middle_index + 1.

# Adjust the logic for ascending or descending order accordingly.

def locate_cards_four(cards,query):
    low = 0
    high = len(cards) - 1
    
    while low <= high:
        middle_index = (low + high) // 2
        middle_value = cards[middle_index]
        
        print("low: ",low," ,high: ",high," ,middle_index: ",middle_index," ,middle_value: ",middle_value)
        
        if middle_value == query:
            return middle_index
        elif middle_value < query:
            high = middle_index - 1
        elif middle_value > query:
            low = middle_index + 1
    return -1
        
    
        


    
    

# **Binary Search**

This project demonstrates a binary search algorithm. In this example, we will solve a problem step by step, showcasing how binary search works and how it can be used efficiently.

---

## **The Problem**

Alice has a set of cards with numbers on them. She arranges these cards in decreasing order and lays them face down in a sequence on a table. Bob is tasked with finding a specific card by turning over as few cards as possible. We need to write a function to help Bob locate the card.

---

## **The Method**

Here is the systematic approach we will apply to solve this problem:

1. **State the problem clearly**: Identify the input and output formats.
2. **Create examples**: Generate example inputs and outputs, covering various edge cases.
3. **Design a solution**: Develop a correct solution to the problem, and explain it in simple terms.
4. **Implement the solution**: Code the solution and test it with example inputs. Fix any bugs that arise.
5. **Analyze complexity**: Evaluate the algorithm’s complexity and identify any inefficiencies.
6. **Optimize**: If there are inefficiencies, apply the right techniques to optimize the solution. Repeat steps 3 to 6.

---

## **The Solution**

The problem is to locate the card containing a given number. We will use binary search, an efficient algorithm that reduces the number of elements Bob needs to check.

Binary search works by repeatedly dividing the list in half, allowing us to minimize the number of cards Bob needs to turn over. We will implement this solution in Python.

---

## **Practice with Word Problems**

Practicing word problems without immediately jumping into code helps improve problem-solving skills. In this case, we treat the sequence of cards as a list of numbers. Turning over a card is analogous to accessing an element from the list.

---

## **How to Solve the Problem**

The task is to find the position of a given number in a list of numbers sorted in decreasing order. The goal is to minimize the number of times we access elements from the list.

---

## **Input**

1. **Cards**: A list of numbers sorted in decreasing order.  
   Example: `[13, 11, 10, 7, 4, 3, 1, 0]`

2. **Query**: A number whose position in the array is to be determined.  
   Example: `7`

---

## **Output**

3. **Position**: The position (index) of the query in the list of cards.  
   Example: `3` (counting from zero)

---

## **The Signature**

The function signature for this problem will be placed in `binarysearch.py`.

---

## **Test Cases**

Before implementing the function, it's helpful to develop test cases that cover various scenarios. We'll use these cases to test our function later. Here's an example test case:

```python
cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3
```

The function should handle a variety of situations, including:

- The query is located somewhere in the middle of the list.
- The query is the first element in the list.
- The query is the last element in the list.
- The list contains only one element, which is the query.
- The list does not contain the query.
- The list is empty.
- The list contains repeating numbers.
- The query appears multiple times in the list.

---

## **Edge Cases**

Edge cases are rare or extreme examples that can sometimes be tricky to handle. These include situations like an empty array or the query not being present in the list. Proper handling of edge cases is crucial for making the function robust.

---

## **Test File**

In the test file, we will use Python assertions to validate the test cases and edge cases. The assertions will compare the expected output with the actual result from the function. The test cases will be represented using dictionaries to simplify the process of testing.

Example test case representation:

```python
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
```

The assertions will check if the function's actual output matches the expected output.

---

## **The Brute Force Method**

### **Solution in Plain English**

The brute force method is the simplest approach to solving the problem. Here's how it works:

1. Initialize a variable `position` to 0.
2. Check whether the number at index `position` in `cards` is equal to the `query`.
3. If it matches, return `position` as the answer.
4. If not, increment `position` by 1 and repeat the process.
5. If no match is found by the end of the list, return `-1`.

The brute force method works, but it's not the most efficient approach, especially for larger lists. However, it’s a good starting point for understanding the problem.

---

## **Debugging the Brute Force Method**

For edge cases where the list is empty, the brute force method would throw an error because it tries to access an element from an empty list. To avoid this, we will modify the `locate_cards_two()` function to include print statements that help us debug the inputs and the `position` variable during each iteration.

### **Fixing the Error**

To prevent the "index out of range" error when the list is empty, we need to check whether the position has reached the end of the list before trying to access an element. This will be the terminating condition for the while loop.

The function `locate_cards_two()` with print statements for debugging can be found in the `mybinarysearch.py` file.

---

## **Updated `locate_cards_two` Function**

The function `locate_cards_two` is an updated version of the original `locate_card` function. It addresses the issue of trying to access an invalid index when the list is empty. The function performs a brute-force search to find the position of a given query in a list of cards:

- The function loops through the list (`cards`) and checks if the current card matches the query.
- The loop condition ensures that `position` is always within the bounds of the list (`position < len(cards)`).
- If a match is found, it returns the index of the card.
- If no match is found by the end of the list, it returns `-1`.

Re-run the test with the new function and see the outputs of the test.

---

## **Analyze the Algorithm's Complexity and Identify Inefficiencies**

Recall this statement from the original question: "Alice challenges Bob to pick out the card containing a given number by turning over as few cards as possible." We restated this requirement as: "Minimize the number of times we access elements from the list cards."

Before we can minimize the number, we need a way to measure it. Since we access a list element once in every iteration, for a list of size N we access the elements from the list up to N times. Thus, Bob may need to overturn up to N cards in the worst case, to find the required card.

Suppose he is only allowed to overturn 1 card per minute. It may take him 30 minutes to find the required card if 30 cards are laid out on the table. Is this the best he can do? Is there a way for Bob to arrive at the answer by turning over just 5 cards, instead of 30?

The field of study concerned with finding the amount of time, space, or other resources required to complete the execution of computer programs is called the analysis of algorithms. The process of figuring out the best algorithm to solve a given problem is called algorithm design and optimization.

---

## **Complexity and Big O Notation**

Complexity of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of a given size (e.g., N). Unless otherwise stated, the term complexity always refers to the worst-case complexity (i.e., the highest possible time/space taken by the program/algorithm to process an input).

In the case of linear search:

    - Time complexity: O(N) — for N elements in the list, we may need to check all of them.
    - Space complexity: O(1) — constant space, as we only need a single variable to store the position.

---

## **Apply the Right Technique to Overcome the Inefficiency**

At the moment, we're simply going over cards one by one, and not even utilizing the fact that they're sorted. This is called a brute force approach.

It would be great if Bob could somehow guess the card at the first attempt, but with all the cards turned over, it's simply impossible to guess the right card.

The next best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the target card lies to the left or right of it. In fact, if we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list. Then, we can simply repeat the process with each half. This technique is called **binary search**. Here's a visual explanation of the technique:

---

## **Correct Solution in Plain English**

Here’s how binary search can be applied to our problem:

1. Find the middle element of the list.
2. If it matches the queried number, return the middle position as the answer.
3. If it is less than the queried number, search the first half of the list.
4. If it is greater than the queried number, search the second half of the list.
5. If no more elements remain, return `-1`.

---

## **Implement the Solution and Test It Using Example Inputs**

There will be an implementation of the binary search algorithm for our problem in `binarysearch.py`.

Moving to the `testbinary.py` file, we will fix our test for handling duplicate values. It seems like we did locate a `6` in the array, but it wasn't the first occurrence of `6`. As you can guess, this is because in binary search, we don't go over indices in a linear order.

So, how do we fix it?

When we find that `cards[mid]` is equal to the query, we need to check whether it is the **first occurrence** of the query in the list (i.e., check the number that comes before it).

Example array:
```python
[8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
```

To make it easier, we’ll define a helper function called `test_location`, which will take the list `cards`, the `query`, and `mid` as inputs to check the first occurrence of the query.

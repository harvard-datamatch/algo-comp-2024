# Assignment 1: Scoring

In this assignment, you will implement a lightweight scoring function of your choice. You are free to design your scoring function however you like, but may find the design discussions we've had during our comp meetings helpful. 

This project will be implemented in **Python** and most of your code will be in the `main.py` file, where you will implement the `compute_score` function.

## Code Layout
To make this more straightforward, we have provided a `User` class with a few attributes that you would find in Datamatch's main scoring algorithm:
```python
class User:
    def __init__(self, first_name, last_name, grad_year=None, responses=None):
        self.first_name = first_name # string
        self.last_name = last_name # string
        self.grad_year = grad_year # int (e.g. 2022, 2023, 2024, 2025)
        self.responses = responses # List[int] (e.g. [0, 1, 2, 3, 1])
```
Note that for  `responses`, each index represents a question and the value stored at that index refers to the answer choice for that question (so in our above case, that person picked `2` for question `2`).

Your task for this assignment will be to implement `compute_score`. `compute_score` takes in two `User` objects and outputs a float denoting their compatibility. One thing to consider is that we want all compatibility scores to be **normalized** across some defined scale (usually this is from `0` to `1`). This helps us better understand the relative differences between two scores (e.g. `6` vs. `7` normalized on `0-10` means something different than `6` vs. `7` normalized on `0-20`.

## Running Your Code
```python3 main.py```

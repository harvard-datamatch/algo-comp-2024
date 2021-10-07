#!usr/bin/env python3
class User:
    def __init__(self, name, grad_year=None, responses=None):
        self.name = name
        self.grad_year = grad_year
        self.responses = responses


# Takes in two user objects and outputs a float denoting compatibility
def compute_score(user1, user2):
    # Your code here
    return 0


if __name__ == '__main__':
    print('Hello World!')

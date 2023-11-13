#!usr/bin/env python3
import json
import sys
import os
from math import comb

INPUT_FILE = 'testdata.json' # Constant variables are usually in ALL CAPS

class User:
    def __init__(self, name, gender, preferences, grad_year, responses):
        self.name = name
        self.gender = gender # str
        self.preferences = preferences # list str
        self.grad_year = grad_year
        self.responses = responses


# Takes in two user objects and outputs a float denoting compatibility
def compute_score(user1, user2):
    # if preferences are opposite, then multiply by 0
    pref1 = 0
    for i in range(len(user1.preferences)):
        if user2.gender == user1.preferences[i]:
            pref1 = 1 - i/len(user1.preferences)
    pref2 = 1
    for i in range(len(user2.preferences)):
        if user1.gender == user2.preferences[i]:
            pref2 = 1 - i/len(user2.preferences)
    pref = (pref1 + pref2)/2
    # if grad years are more than 2 years apart, then multiply by 0
    age = 0
    if abs(user2.grad_year - user1.grad_year) <= 2:
        age = 1
    # measure response similarity
    sim1 = 0
    sim2 = 0
    for i in range(len(user1.responses)):
        if user1.responses[i]==user2.responses[i]:
            sim1+=1
            for j in range(i+1, len(user1.responses)):
                if user1.responses[j]==user2.responses[j]:
                    sim2 += 1
    sim1 = sim1/20
    sim2 = sim2/((len(user1.responses)-1)*(len(user1.responses) -2)/2)
    sim = (sim1 + sim2)/2
    return sim

if __name__ == '__main__':
    # Make sure input file is valid
    if not os.path.exists(INPUT_FILE):
        print('Input file not found')
        sys.exit(0)

    users = []
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
        for user_obj in data['users']:
            new_user = User(user_obj['name'], user_obj['gender'],
                            user_obj['preferences'], user_obj['gradYear'],
                            user_obj['responses'])
            users.append(new_user)

    for i in range(len(users)-1):
        for j in range(i+1, len(users)):
            user1 = users[i]
            user2 = users[j]
            score = compute_score(user1, user2)
            print('Compatibility between {} and {}: {}'.format(user1.name, user2.name, score))

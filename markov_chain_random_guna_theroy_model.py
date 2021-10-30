import numpy as np
import random as rm
# The statespace
states = ["Sattvic","Rajasic","Tamasic"]

# Possible sequences of events
transitionName = [["SS","SR","ST"],["RS","RR","RT"],["TS","TR","TT"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]
#transitionMatrix = [[0.09,0.29,0.62],[0.29,0.6,0.11],[0.62,0.11,0.17]]

# A function that implements the Markov model to forecast the state/mood.
def activity_forecast(days):
    # Choose the starting state
    activityToday = "Sattvic"
    print("Start state: " + activityToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activityList = [activityToday]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != days:
        if activityToday == "Sattvic":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sattvic")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Tamasic"
                activityList.append("Tamasic")
            else:
                prob = prob * 0.2
                activityToday = "Rajasic"
                activityList.append("Rajasic")
        elif activityToday == "Tamasic":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 0.6
                activityList.append("Tamasic")
                pass
            elif change == "RS":
                prob = prob * 0.1
                activityToday = "Sattvic"
                activityList.append("Sattvic")
            else:
                prob = prob * 0.3
                activityToday = "Rajasic"
                activityList.append("Rajasic")
        elif activityToday == "Rajasic":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "TT":
                prob = prob * 0.1
                activityList.append("Rajasic")
                pass
            elif change == "TS":
                prob = prob * 0.2
                activityToday = "Sattvic"
                activityList.append("Sattvic")
            else:
                prob = prob * 0.7
                activityToday = "Tamasic"
                activityList.append("Tamasic")
        i += 1  
    print("Possible states: " + str(activityList))
    print("End state after "+ str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))
    print("Transition Matrix",transitionMatrix)

# Function that forecasts the possible state for the next 2 days
activity_forecast(10)

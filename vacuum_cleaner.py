# What the goal state of agent should be 
goalState = {'A' : '0' , 'B' : '0' }
action = 0       # 0 = Clean , 1 = Dirty
cost = 0
roomStates = {'A' : '0' , 'B' : '0' }

#initial input
print ("Enter the starting location of vacuum (A/B) = ")
location = input()
print()

for room in roomStates:
    action = input("Enter the state of " + room + " (0 for clean /1 for dirty): ")
    roomStates[room] = action

#General Outputs

print()
print("\nCurrent State: " + str(roomStates))
print("\nGoal state: " + str(goalState))

print("\n Vacuum is placed in location " + location)

if (roomStates != goalState) :
    
    #If the starting location is room A
    if (location == 'A'):
        if (roomStates['A'] == '1'): #if dirty
            roomStates['A'] = '0'
            cost+=1
            print("Location A was dirty\nLocation A has been cleaned\nCost for cleaning is 1.")
            
        if (roomStates == goalState):
            print("Goal state has been met.")
            print("\nPerformance Measurement: " + str(cost))
            
        #If A is clean. Going from A -> B
        else:
            print("\nA is clean")
            print("\nA -> B")
            print("\nCost for moving within rooms = 1")
            cost+=1
            
            if (roomStates['B'] == '1'):#If B is dirty
                roomStates['B'] = '0'
                cost+=1
                print("Location B was dirty\nLocation B has been cleaned\nCost for cleaning is 1.")
                
            if (roomStates == goalState):
                print("Goal state has been met.")
                print("\nPerformance Measurement: " + str(cost))
                    
    #If the starting location is room B   
    elif (location == "B"):
        if(roomStates['B'] == '1'): #B is dirty
            roomStates['B'] = '0'
            cost+=1
            print("Location B was dirty\nLocation B has been cleaned\nCost for cleaning is 1.")
            
        if (roomStates == goalState):
            print("Goal state has been met.")
            print("\nPerformance Measurement: " + str(cost))
            
        #If B is clean, then we will move to A first
        else:
            print("\nB is clean")
            print("\nB -> A")
            print("\nCost for moving within rooms = 1")
            cost+=1
            
            if(roomStates['A'] == '1'): #A is dirty
                roomStates['A'] = '0'
                cost+=1
                print("Location A was dirty\nLocation A has been cleaned\nCost for cleaning is 1.")
                
                if (roomStates == goalState):
                    print("Goal state has been met.")
                    print("\nPerformance Measurement: " + str(cost))
                
                else:
                    print("\nA is clean")
                    print("\nA -> B")
                    print("\nCost for moving within rooms = 1")
                    cost+=1

                    if (roomStates == goalState):
                        print("Goal state has been met.")
                        print("\nPerformance Measurement: " + str(cost))
                
                if (roomStates == goalState):
                    print("Goal state has been met.")
                    print("\nPerformance Measurement: " + str(cost))
                
    else:
        print("\nInvalid Start Location")
        
else:
    print("\nAll rooms are already clean")
    print("\nPerformance Measurement: " + str(cost))
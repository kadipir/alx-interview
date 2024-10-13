#!/usr/bin/python3
"""
Method to determine if all boxes can be opened using prototype: def canUnlockAll(boxes);
"""

def canUnlockAll(boxes):
    """check if boxes can be unlocked"""
    n = len(boxes) #number of boxes

    #set to keep track of unlocked boxes
    unlocked  = set()

    #list to manage boxes to be explored
    explore = [0]

    while explore:
        current_box = explore.pop()
        
        #if in  box explores skip
        if current_box in explored:
            continue

        #mark the current_box as unlocked
        unlocked.add(current_box)

        #get the keys in current box
        for key in boxes[current_box]:

            #if the key is a valid box index and not yet in unlocked
            if key < n and key not in unlocked:
                explore.append(key)


    #check if all unlocked
    return len(unlocked) = n

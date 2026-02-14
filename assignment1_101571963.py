"""
Author: Alfred Ranz Navarro
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"     # String
preferred_weight_kg = 20.5      # Float
highest_rep = 25                # Integer
membership_active = True        # Boolean

# Step c: Create a dictionary named workout_stats
workout_stats = { # Yoga Running Weightlifting
    "John": (22.3, 35, 55),
    "Doe": (33, 21, 70),
    "Jeremy": (40, 33, 20)
}
# TODO EXPLAIN
# Step d: Calculate total workout minutes using a loop and add to dictionary
for key in list(workout_stats.keys()):
    total = sum(workout_stats[key])
    name= key + "_total"
    workout_stats[name] = total
# Step e: Create a 2D nested list called workout_list
# Workout list: each row is friend, each column is activity,
start = 0
workout_list = [[], [], []]
for x in workout_stats.values():
    if type(x) == tuple:
        for val in x:
            sublist = workout_list[start]
            sublist.append(val)
            start += 1
    start = 0
# Print the tuple correspondingly
start = 0
for key,value in workout_stats.items():
    if type(value) != tuple:
        break
    print(key, "'s workout statistics are: ", workout_list[start] )
    start+=1


# Step f: Slice the workout_list
print("Yoga and running statistics are: ")
for row in range(len(workout_list)):
    print(workout_list[row][:2])
for val in workout_list[-2:]:
    print("Weightlifting statistics for the last two friends: ", val[2])


# Step g: Check if any friends total >= 120
for key, value in workout_stats.items():
    if type(value) != tuple:
        continue
    if sum(value)>=120:
        print("Doe had a total of ", sum(value), " minutes of workout this week. Great job staying active, ", key)
# Step h: User input to look up a friend
inquiry = input("Enter your friend's name: ")
found = False
for key in workout_stats.keys():
    if key == inquiry:
        found = True
if found:
    print("Stats: ", workout_stats[inquiry])
else:
    print("Friend ", inquiry, " not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
lowest = 100000
highest = 0
for key, value in workout_stats.items():
    if type(value) == tuple:
        continue
    if value > highest:
        highest = value
    if value < lowest:
        lowest = value

print("Highest workout time is: ", highest)
print("Lowest workout time is: ", lowest)

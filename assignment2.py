import math

people = int(input("How many people will attend? "))
hotdogs = int(input("How many hot dogs will each person get? "))

total_hotdogs = people * hotdogs
total_buns = total_hotdogs 

hotdog_packages = math.ceil(total_hotdogs / 10)
bun_packages = math.ceil(total_buns / 8)

hotdogs_leftover = (hotdog_packages * 10) - total_hotdogs
buns_leftover = (bun_packages * 8) - total_buns

print(f"\nMinimum number of hot dog packages required: {hotdog_packages}")
print(f"Minimum number of hot dog bun packages required: {bun_packages}")
print(f"Number of hot dogs that will be left over: {hotdogs_leftover}")
print(f"Number of hot dog buns that will be left over: {buns_leftover}")
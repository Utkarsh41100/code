import os
if not os.path.exists("Data"):
    os.mkdir("Data")

for i in range(1,100):
    os.mkdir(f"Data/Day {i}")


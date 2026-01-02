from itertools import cycle
import time

def run_light(color,message,seconds):
    print(f"\n{color} light - {message}")
    for i in range(seconds, 0 ,-1):
        print(f"changing in {i} sec",end="\r")
        time.sleep(1)
    print()


print("===Traffic Light Simulator ===")

cycles = int(input("Enter number of cycles: "))

for _ in range(cycles):
    run_light("RED","STOP",3)
    run_light("YELLOW","READY",2)
    run_light("GREEN","GO",3)
    print("--------------------------")

print("simulation completed")    
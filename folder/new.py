import random

# processing times (seconds)
A_time = 5
B_time = 6
C_time = 6

products = 50

time = 0
A_free = 0
B_free = 0
C_free = 0

for i in range(products):
    # Machine A
    start_A = max(time, A_free)
    finish_A = start_A + A_time

    # Machine B
    start_B = max(finish_A, B_free)
    finish_B = start_B + B_time

    # Machine C
    start_C = max(finish_B, C_free)
    finish_C = start_C + C_time

    # update machine availability
    A_free = finish_A
    B_free = finish_B
    C_free = finish_C

    time = start_A

print("Total production time:", finish_C)

print(f"Product {i+1} finished at time {finish_C}")
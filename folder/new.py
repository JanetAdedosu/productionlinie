import random
#for graph 
import matplotlib.pyplot as plt

A_time = 5
B_time = 8
C_time = 6

products = 40



A_free = 0
B_free = 0
C_free = 0

waiting_B = []
waiting_C = []


for i in range(products):
    # Machine A
    start_A =  A_free
    finish_A = start_A + A_time

    # Machine B
    wait_B = max(0, finish_A - B_free)
    start_B = max(finish_A, B_free)
    finish_B = start_B + B_time

    # Machine C
    wait_C = max(0, finish_B - C_free)
    start_C = max(finish_B, C_free)
    finish_C = start_C + C_time

# update machine availability
    A_free = finish_A
    B_free = finish_B
    C_free = finish_C

    waiting_B.append(wait_B)
    waiting_C.append(wait_C)

print("Total production time:", finish_C)
print(f"Product {i+1} finished at time {finish_C}")

print("Average waiting at B:", sum(waiting_B)/len(waiting_B))
print("Average waiting at C:", sum(waiting_C)/len(waiting_C))

# now it takes 251 seconds to produce all products thru A-B-C , 
#machine b was the slowest and create a bottle necks 
#because other machines wait for it
#Before optimization time  : 331 seconds 
#After optimization time : 251 seconds 

plt.plot(waiting_B, label="Waiting at B")
plt.plot(waiting_C, label="Waiting at C")
plt.show()
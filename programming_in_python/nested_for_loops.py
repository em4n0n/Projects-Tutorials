#Nested for loop

#outer loop
# for x in range(10):
#     print(x)
#     #inner loop
#     for y in range(10):
#         print(y)

#the outer loop starts, and then the inner loop
#the inner loop with start until its range limit is met
#once the inner loops completes, it will come back to the outer loop for its next iteration, then step into the inner loops again
#repeats until the outer loop has reached its limit

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# count = 0
# #outer loop
# for x in list1:
#     count+=1
#     #inner loop
#     for y in list2:
#         count+=1

# print(count)

import time
start_time = time.time()
#outer loop
for i in range(10):
    #inner loop
    for j in range(10):
        print(0, end = " ")
    print()

print(round((time.time() - start_time), 2))

import time
start_time = time.time()

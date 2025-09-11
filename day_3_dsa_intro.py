#Big O notation Analysis
import time

#Defining function for O(1)
def find_at_index(data_list,index):
    return data_list[index]

#Function for O(n):
def find_at_value(data_list,value):
    for item in data_list:
        if item == value:
            return item
    return None

def find_all_value(data_list):
    for item1 in data_list:
        for item2 in data_list:
            pass


large_list = list(range(10_000_000))
small_list = list(range(1_000))

start_time_o1 = time.time()
result_o = find_at_index(large_list,9_000_000)
end_time_o1 = time.time()
print(f"O(1) operation found {result_o}")
print(f"Time Taken is {end_time_o1-start_time_o1}")

print("\n"+"-"*20+"\n")

start_time_on = time.time()
result_n = find_at_value(large_list,9_999_000)
end_time_on = time.time()
print(f"O(n) operation found {result_n}")
print(f"Time Taken is {end_time_on-start_time_on}")

print("\n"+"-"*20+"\n")

start_time_on2 = time.time()
result_n2 = find_all_value(small_list)
end_time_on2 = time.time()
print(f"O(n^2) operation found {result_n2}")
print(f"Time Taken is {end_time_on2-start_time_on2}")
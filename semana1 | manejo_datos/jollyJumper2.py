from sys import stdin, stdout

# Ingreso de datos

nums_arr = [int(x) for x in stdin.readline().split(" ")]
nums_arr = [elemento for elemento in nums_arr if elemento != ""]
# Obtener elementos
set_nums = set()
arr_size = len(nums_arr)
for i in range(1, arr_size):
    set_nums.add(i)

# TEST
for index in range(0, len(set_nums)):
    num = int(nums_arr[index])
    next_num = int(nums_arr[index + 1])
    diff = abs(num - next_num)
    if(diff in set_nums):
        set_nums.remove(diff)
if (len(set_nums) == 0):
    stdout.write("Jolly")
else:
    stdout.write("Not jolly")

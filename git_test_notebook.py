# Databricks notebook source
# MAGIC %md
# MAGIC ## just a random test for dbx/git interplay

# COMMAND ----------

print('hello world')

# COMMAND ----------

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example array and target
example_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

# Perform binary search
index = binary_search(example_array, target_value)
index

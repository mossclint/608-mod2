values = [47, 95, 88, 73, 88, 84]
print(len(values))
print(sum(values))
print(sum(values)/len(values))

xmedian = len(values)
values.sort()
  
if xmedian % 2 == 0:
    median1 = values[xmedian//2]
    median2 = values[xmedian//2 - 1]
    median = (median1 + median2)/2
else:
    median = values[xmedian//2]
print("Median is: " + str(median))


data = collections.len(values)
data_list = dict(data)
max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value]
if len(mode_val) == len(num_list):
   print("No mode in the list")
else:
   print("The Mode of the list is : " + ', '.join(map(str, mode_val)))


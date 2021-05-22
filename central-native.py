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


from collections import Counter
  
# list of elements to calculate mode
n_num = [values]
n = len(n_num)
  
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)

values = [47, 95, 88, 73, 88, 84]
print('Count is', + len(values))
print('Sum is', + sum(values))
print('Mean is', + sum(values)/len(values))

xmedian = len(values)
values.sort()
  
if xmedian % 2 == 0:
    median1 = values[xmedian//2]
    median2 = values[xmedian//2 - 1]
    median = (median1 + median2)/2
else:
    median = values[xmedian//2]
print("Median is: " + str(median))

mode = mex(values, key = values.count)
Print(Mode is', + mode)


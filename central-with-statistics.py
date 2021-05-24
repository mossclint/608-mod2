import statistics


values = [47, 95, 88, 73, 88, 84]

print('Count is', + len(values))
print('Sum is', + sum(values))
print('Count using statistics is', + statistics.count(values))
print('Mean using statistics is', + statistics.mean(values))
print('Median using statistics is', + statistics.median(values))
print('Mode using statistics is', + statistics.mode(values))

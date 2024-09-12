# Enter your code here. Read input from STDIN. Print output to STDOUT
len_arr = int(input())
arr = list(map(int, input().split(" ")))

mean = round(sum(arr)/len_arr, 1)
arr.sort()
if len_arr % 2==0:
    median = arr[(len_arr//2)-1:(len_arr//2)+1]
    median = round(sum(median)/2, 1)
else:
    median = round((arr[len_arr//2])/len_arr, 1)
a = list(set(arr))
a.sort()
appeareances = dict(zip(a, [0]*len(arr)))
for e in arr:
    appeareances[e] += 1
mode = max(appeareances.items(), key=lambda x: x[1])[0]

print(mean)
print(median)
print(mode)

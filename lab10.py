#1
from math import log
print("Задание 1")

def my_log(n):
	arr = []
	for i in n:
		if i > 0: arr.append(log(i))
		else: arr.append(None)
	return arr
print(my_log([1, 3, 2.5, -1, 9, 0, 2.71]))


#2
print("\nЗадание 2")

def zp(a, b):
	if len(a) == len(b): return dict(zip(a, b))
	else:
		print("Списки имеют разную длину")
		return {}
print(zp(["Ann", "Tim", "Sam"], [12, 23, 17]))
print(zp(["Ann", "Tim", "Sam"], [12, 23, 17, 45]))


#3
print("\nЗадание 3")
from math import factorial
def C(k, n):
	if 0 <= k and k <= n:
		return factorial(n) / (factorial(k) *  factorial(n - k))
	if 0 <= n and n <= k:
		return 0
def binom_prob(p, n, k):
	return C(k, n) * (p ** k) * ((1 - p)**(n-k))

print(binom_prob(0.5, 4, 2))


#4
print("\nЗадание 4")
def all_sort(s):
	return sorted(list(map(int, s.split(", "))))

print(all_sort('7, 6, 1, 3, 8, 0, -2'))
my_list = [10, 20, 30, 40, 50]

a, b, c, d, e = my_list
print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}, e={e}", end=" | ")

a, _, c, _, e = my_list
print(f"Skipping values: a={a}, c={c}, e={e}")

x, *y = my_list
print(f"First element: x={x}, Remaining elements: y={y}")

*start, z = my_list
print(f"Last element: z={z}, Starting elements: start={start}")

first, *middle, last = my_list
print(f"First element: first={first}, Middle elements: middle={middle}, Last element: last={last}")

# Caution below, last element is returned as list.
new_list = [10, 20, 30]
a, b, *rest = new_list
print(f"a={a}, b={b}, rest={rest}")
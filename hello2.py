# lambda function
si = lambda p, t, r: (p * t * r) / 100

# given values for principal (p), time (t) in years, and rate of interest (r) per annum
p, t, r = 8, 6, 8

res = si(p, t, r)
print(res)


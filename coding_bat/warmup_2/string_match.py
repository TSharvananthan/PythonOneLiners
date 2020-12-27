def string_match(a, b): return [a[n:n+2] == b[n:n+2] for n in range(len(a) - 1)].count(True)

def last2(str): return [str[n:n+2] == str[-2::] for n in range(len(str))].count(True) - 1 if not len(str) == 0 else 0

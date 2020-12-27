def count_code(str): return len([1 for x in range(0, len(str)-3) if str[x:x+2] == "co" and str[x+3] == "e"])

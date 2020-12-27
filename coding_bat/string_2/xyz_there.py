def xyz_there(str): return 1 in [(str[i] != '.' and str[i+1:i+4] == 'xyz') or (str[0:3] == 'xyz') for i in range(len(str))]

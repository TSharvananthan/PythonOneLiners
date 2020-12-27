def date_fashion(you, date): return [you <= 2 or date <= 2, not you <= 2 and not date <= 2 and not you >= 8 and not date >= 8, you >= 8 or date >= 8].index(True)

def ensure_positive_int(val):
    if type(val) is int:
        if int(val) > 0:
            return int(val)
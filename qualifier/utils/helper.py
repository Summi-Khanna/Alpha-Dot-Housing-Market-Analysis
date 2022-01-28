import pandas as pd

def add_values(val1, val2, val3, val4):
    return val1 + val2 + val3 + val4

def create_code(code):
    code = '53' + str(code).zfill(3)
    return code
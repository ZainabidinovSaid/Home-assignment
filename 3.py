import pandas as pd

batch_group = {
    'MatMIE':27,
    'MatDAIS': 30,
    'COMIE':28,
    'COMEC': 34
}

stud_series = pd.Series(batch_group)

print(stud_series)
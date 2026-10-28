import pandas as pd
data = {
        'A':[10,20,30,40],
        'B':[15,10,40,60],
        'C':[13,26,66,70]
        }
df = pd.DataFrame(data)
print("carrelationnn matrix")
print(df.corr())
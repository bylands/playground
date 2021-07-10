import pandas as pd

df = pd.DataFrame(
    {
        'Name': [
            'Samuel Byland',
            'Katrin Leenen',
            'Marlon Byland'
        ],
        'Age': [
            50,
            48,
            18
        ],
        'Sex': [
            'm',
            'f',
            'm'
        ]
    }
)
print(df)
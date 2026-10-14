import pandas as pd
import os

df = pd.read_csv('./data/raw/courses.csv')

df = df[df['price'] > 1500]

df.to_csv(os.path.join('data','processed','courses_having_price_greater_than_1500.csv'), index=False)
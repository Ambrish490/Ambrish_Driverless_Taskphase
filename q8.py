import numpy as np
import pandas as pd

input_filename = input()

df = pd.read_csv(input_filename)

df['distance_to_origin'] = np.sqrt(df['x']**2 + df['y']**2)
df_sorted = df.sort_values(by='distance_to_origin')

df_blue = df_sorted[df_sorted['colour'] == 'blue'].copy()
df_yellow = df_sorted[df_sorted['colour'] == 'yellow'].copy()

df_blue.drop(columns=['distance_to_origin']).to_csv('blue_cones.csv', index=False)
df_yellow.drop(columns=['distance_to_origin']).to_csv('yellow_cones.csv', index=False)

midpoints = []

for _, blue_row in df_blue.iterrows():
    bx, by = blue_row['x'], blue_row['y']
    distances_to_yellow = np.sqrt((df_yellow['x'] - bx)**2 + (df_yellow['y'] - by)**2)
    nearest_yellow = df_yellow.loc[distances_to_yellow.idxmin()]
    
    midpoints.append({
        'blue_id': blue_row['cone_id'],
        'yellow_id': nearest_yellow['cone_id'],
        'mid_x': (bx + nearest_yellow['x']) / 2,
        'mid_y': (by + nearest_yellow['y']) / 2
    })

df_centreline = pd.DataFrame(midpoints)
df_centreline.to_csv('centreline.csv', index=False)

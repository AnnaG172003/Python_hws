import pandas as pd
import numpy as np

# Training data
data = {
    "x1":  [0.8, 2.0, 2.5, 3.2, 4.1, 5.9, 6.4, 6.9, 7.8, 9.1],
    "x2":  [5.0, 5.5, 3.5, 6.3, 5.2, 5.6, 6.4, 3.7, 5.3, 6.1],
    "class": [-1, -1, -1, -1, -1, +1, +1, +1, +1, +1]
}
df = pd.DataFrame(data)

# Test point
test_x1, test_x2 = 5.1, 4.9

# Compute distances
df["distance"] = np.sqrt((df["x1"] - test_x1)**2 + (df["x2"] - test_x2)**2)

# Sort by distance
df_sorted = df.sort_values("distance").reset_index(drop=True)

# Add columns for neighbor votes
df_sorted["1NN"] = ""
df_sorted["3NN"] = ""
df_sorted["5NN"] = ""

# Fill with class values instead of X
df_sorted.loc[0, "1NN"] = df_sorted.loc[0, "class"]
df_sorted.loc[:2, "3NN"] = df_sorted.loc[:2, "class"]
df_sorted.loc[:4, "5NN"] = df_sorted.loc[:4, "class"]

# Predictions
def knn_predict(df_sorted, k):
    neighbors = df_sorted.head(k)
    vote = neighbors["class"].value_counts()
    return vote.idxmax()

pred_1nn = knn_predict(df_sorted, 1)
pred_3nn = knn_predict(df_sorted, 3)
pred_5nn = knn_predict(df_sorted, 5)

# Add test point row with final predictions
df_sorted.loc[len(df_sorted)] = {
    "x1": test_x1,
    "x2": test_x2,
    "class": "?",
    "distance": None,
    "1NN": pred_1nn,
    "3NN": pred_3nn,
    "5NN": pred_5nn
}

print(df_sorted)

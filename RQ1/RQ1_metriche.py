import pandas as pd
from pathlib import Path
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

groundtruth_file = Path(__file__).parent /"rq1_groundtruth.csv"
results_file = Path(__file__).parent /"rq1_results.csv"

df_gt = pd.read_csv(groundtruth_file)    
df_results = pd.read_csv(results_file) 

df = pd.merge(df_gt, df_results, on="filename")

df["Label"] = df["label"].str.strip().str.lower()
df["RQ1_Response"] = df["RQ1_Response"].str.strip().str.lower()

# Mappa: yes -> 1 (dirty), no -> 0 (clean)
label_map = {"yes": 1, "no": 0}
y_true = df["Label"].map(label_map)
y_pred = df["RQ1_Response"].map(label_map)

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
cm = confusion_matrix(y_true, y_pred)

print("=== RISULTATI RQ1 ===")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("\nConfusion Matrix:")
print(cm)


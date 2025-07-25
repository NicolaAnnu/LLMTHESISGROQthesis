import pandas as pd
from pathlib import Path
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_rq2_metrics(csv_path):
    df = pd.read_csv(csv_path)

    if 'RQ2_Response' not in df.columns or 'is_correct' not in df.columns:
        raise ValueError("Il CSV deve contenere le colonne 'RQ2_Response' e 'is_correct'.")

    y_pred = df['RQ2_Response'].astype(str).str.strip().str.lower()
    
    y_true = [
        pred if correct else ("no" if pred == "yes" else "yes")
        for pred, correct in zip(y_pred, df["is_correct"])
    ]

    pos_label = "yes"

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, pos_label=pos_label, zero_division=0)
    recall = recall_score(y_true, y_pred, pos_label=pos_label, zero_division=0)
    f1 = f1_score(y_true, y_pred, pos_label=pos_label, zero_division=0)

    return accuracy, precision, recall, f1

one_shot_file = Path(__file__).parent / "rq2_resultsOneShot.csv"
few_shot_file = Path(__file__).parent / "rq2_resultsFewShot.csv"

acc1, prec1, rec1, f1_1 = evaluate_rq2_metrics(one_shot_file)
acc2, prec2, rec2, f1_2 = evaluate_rq2_metrics(few_shot_file)

print("=== RISULTATI RQ2 ===")
print("--- One-Shot ---")
print(f"Accuracy:  {acc1:.2%}")
print(f"Precision: {prec1:.2%}")
print(f"Recall:    {rec1:.2%}")
print(f"F1 Score:  {f1_1:.2%}\n")

print("--- Few-Shot ---")
print(f"Accuracy:  {acc2:.2%}")
print(f"Precision: {prec2:.2%}")
print(f"Recall:    {rec2:.2%}")
print(f"F1 Score:  {f1_2:.2%}")

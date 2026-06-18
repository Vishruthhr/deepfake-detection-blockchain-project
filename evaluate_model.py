import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tensorflow.keras.models import load_model

from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from face_dataset_generator import FaceGenerator


# ==========================
# LOAD TEST DATA
# ==========================

test_gen = FaceGenerator(
    "face_test.csv",
    batch_size=2,
    shuffle=False
)

# ==========================
# LOAD MODEL
# ==========================

model = load_model(
    "face_models/best_finetuned_model.h5"
)

# ==========================
# PREDICTIONS
# ==========================

y_true = []
y_pred = []
y_prob = []

print("\nRunning Predictions...\n")

for i in range(len(test_gen)):

    X_batch, y_batch = test_gen[i]

    preds = model.predict(
        X_batch,
        verbose=0
    )

    preds = preds.flatten()

    y_true.extend(y_batch)

    y_prob.extend(preds)

    y_pred.extend(
        (preds > 0.5).astype(int)
    )

y_true = np.array(y_true)
y_pred = np.array(y_pred)
y_prob = np.array(y_prob)

# ==========================
# METRICS
# ==========================

accuracy = accuracy_score(
    y_true,
    y_pred
)

precision = precision_score(
    y_true,
    y_pred
)

recall = recall_score(
    y_true,
    y_pred
)

f1 = f1_score(
    y_true,
    y_pred
)

roc_auc = roc_auc_score(
    y_true,
    y_prob
)

print("=" * 50)
print("MODEL EVALUATION RESULTS")
print("=" * 50)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"ROC AUC   : {roc_auc:.4f}")

print("\nClassification Report:\n")

print(
    classification_report(
        y_true,
        y_pred,
        target_names=[
            "Real",
            "Fake"
        ]
    )
)

# ==========================
# CONFUSION MATRIX
# ==========================

cm = confusion_matrix(
    y_true,
    y_pred
)

plt.figure(figsize=(8, 6))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Real", "Fake"],
    yticklabels=["Real", "Fake"]
)

plt.title(
    "Confusion Matrix"
)

plt.xlabel(
    "Predicted"
)

plt.ylabel(
    "Actual"
)

plt.tight_layout()

plt.savefig(
    "confusion_matrix.png",
    dpi=300
)

plt.show()

print(
    "\nConfusion Matrix saved as confusion_matrix.png"
)
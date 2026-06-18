import os

from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint
)

from face_dataset_generator import FaceGenerator
from model import build_model

os.makedirs("face_models", exist_ok=True)

train_gen = FaceGenerator(
    "face_train.csv",
    batch_size=4,
    shuffle=True
)

test_gen = FaceGenerator(
    "face_test.csv",
    batch_size=4,
    shuffle=False
)

model = build_model()

checkpoint = ModelCheckpoint(
    "face_models/best_face_model.h5",
    monitor="val_accuracy",
    save_best_only=True,
    mode="max",
    verbose=1
)

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True,
    verbose=1
)

history = model.fit(
    train_gen,
    validation_data=test_gen,
    epochs=10,
    callbacks=[
        checkpoint,
        early_stop
    ]
)

model.save(
    "face_models/final_face_model.h5"
)

print("\nTraining Complete!")
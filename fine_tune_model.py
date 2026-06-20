import tensorflow as tf

from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import (
    ModelCheckpoint,
    EarlyStopping
)

from face_dataset_generator import FaceGenerator


# =====================
# LOAD DATA
# =====================

train_gen = FaceGenerator(
    "face_train.csv",
    batch_size=2,
    shuffle=True
)

test_gen = FaceGenerator(
    "face_test.csv",
    batch_size=2,
    shuffle=False
)

# =====================
# LOAD BEST MODEL
# =====================

model = load_model(
    "face_models/best_face_model.h5"
)

# =====================
# GET XCEPTION BACKBONE
# =====================

xception_model = model.layers[0].layer

# =====================
# FINE-TUNE ONLY LAST 30 LAYERS
# =====================

xception_model.trainable = True

for layer in xception_model.layers[:-30]:
    layer.trainable = False

# =====================
# RECOMPILE
# =====================

model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=1e-5
    ),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# =====================
# CALLBACKS
# =====================

checkpoint = ModelCheckpoint(
    "face_models/best_finetuned_model.h5",
    monitor="val_accuracy",
    save_best_only=True,
    mode="max",
    verbose=1
)

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True,
    verbose=1
)

# =====================
# TRAIN
# =====================

history = model.fit(
    train_gen,
    validation_data=test_gen,
    epochs=10,
    callbacks=[
        checkpoint,
        early_stop
    ]
)

# =====================
# SAVE FINAL MODEL
# =====================

model.save(
    "face_models/final_finetuned_model.h5"
)

print("\nFine-tuning Complete!")
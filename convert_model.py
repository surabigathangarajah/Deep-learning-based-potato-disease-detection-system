import tensorflow as tf

# load your model
model = tf.keras.models.load_model("saved_model/saved_model.keras")

# EXPORT for TensorFlow Serving (IMPORTANT)
model.export("saved_model_tf")
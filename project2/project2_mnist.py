import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

# Step 1: Load Dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Step 2: Reshape and Normalize
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# Step 3: One-hot Encode Labels
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Step 4: Build CNN Model
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Step 5: Compile Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 6: Train Model
model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.1)

# Step 7: Evaluate
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Test Accuracy: {:.2f}%".format(test_accuracy * 100))

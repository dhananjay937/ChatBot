import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import legacy as optimizers
import random

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load intents data
data_file = open('data.json').read()
intents = json.loads(data_file)

words = []
classes = []
documents = []
ignore_words = ['?', '!']

# Process intents
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique lemmatized words", words)

# Save words and classes
pickle.dump(words, open('texts.pkl', 'wb'))
pickle.dump(classes, open('labels.pkl', 'wb'))

# Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag, output_row])

# Debugging print to check lengths of input and output vectors
for t in training:
    print(f'Input vector length: {len(t[0])}, Output vector length: {len(t[1])}')

# Shuffle the training data
random.shuffle(training)

# Ensure all lists in training data have consistent lengths before converting to numpy arrays
train_x = []
train_y = []
for t in training:
    train_x.append(t[0])
    train_y.append(t[1])

# Convert lists to numpy arrays
train_x = np.array(train_x, dtype=np.float32)
train_y = np.array(train_y, dtype=np.float32)

print("Training data created")

# Debugging print to check shapes of train_x and train_y
print(f'train_x shape: {train_x.shape}')
print(f'train_y shape: {train_y.shape}')

# Create the model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile the model using the legacy optimizer
sgd = optimizers.SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fit and save the model
hist = model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)
model.save('model.h5')

print("model created")

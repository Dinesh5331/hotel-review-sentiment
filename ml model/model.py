import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
import re
import pickle
import os

data=pd.read_csv("tripadvisor_hotel_reviews.csv")

stopwords=stopwords.words("english")

def process_text(text):
    text=re.sub(r'\d+',' ',text)
    text=text.split()
    text=' '.join([word for word in text if word.lower().strip() not in stopwords])
    return text

reviews=data["Review"].apply(process_text)

num_words=10000
tokenizer=Tokenizer(num_words=num_words)
tokenizer.fit_on_texts(reviews)
sequences=tokenizer.texts_to_sequences(reviews)

max_seq_length=np.max(list(map(lambda x: len(x),sequences)))
inputs=pad_sequences(sequences,maxlen=max_seq_length,padding='post')

labels=np.array(data['Rating'].apply(lambda x: 1 if x > 3.5 else 0))

train_inputs,test_inputs,train_labels,test_labels=train_test_split(inputs,labels,train_size=0.7,random_state=100)

embedding_dim=128
inputs=tf.keras.Input(shape=(max_seq_length,))
embedding=tf.keras.layers.Embedding(
    input_dim=num_words,
    output_dim=embedding_dim,    

)(inputs)
gru=tf.keras.layers.Bidirectional(tf.keras.layers.GRU(128,return_sequences=True))(embedding)
flatten=tf.keras.layers.Flatten()(gru)
outputs=tf.keras.layers.Dense(1,activation='sigmoid')(flatten)
model=tf.keras.Model(inputs,outputs)

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=[
        'accuracy',
        tf.keras.metrics.AUC(name='auc')
    ]
)
history=model.fit(
    train_inputs,
    train_labels,
    validation_split=0.2,
    batch_size=32,
    epochs=2,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(
            monitor='val_accuracy',
            patience=2,
            restore_best_weights=True
        )
    ]
)

test_loss, test_accuracy, test_auc = model.evaluate(test_inputs, test_labels)

def predict_review_sentiment(text):
    processed_text = process_text(text)
    sequence = tokenizer.texts_to_sequences([processed_text])
    padded_sequence = pad_sequences(sequence, maxlen=max_seq_length, padding='post')
    prediction = model.predict(padded_sequence, verbose=0)[0][0]
    if prediction > 0.5:
        return "POSITIVE", prediction
    else:
        return "NEGATIVE", prediction


os.makedirs('saved_model', exist_ok=True)
model.save('saved_model/hotel_review_model.h5')
with open('saved_model/tokenizer.pkl', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('saved_model/max_seq_length.pkl', 'wb') as handle:
    pickle.dump(max_seq_length, handle, protocol=pickle.HIGHEST_PROTOCOL)
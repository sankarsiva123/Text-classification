from typing import Optional

from fastapi import FastAPI
import tensorflow
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop = stopwords.words('english')
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

## Importing tokenizer
with open('tokenizer_final.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

## to clean the text --> preprocess steps
def clean_text(list_text):
    out = []
    for i in list_text:
        result = re.sub('<.*?>','',i)
        result = re.sub('[^a-z\sA-Z]+','',result)
        result = ' '.join([word for word in result.split() if word not in (stop)])
        result = result.lower()
        out.append(result)
    return out

## Load the model
model = tensorflow.keras.models.load_model('model_text_final.hdf5',compile= False)

app = FastAPI()



@app.get("/text_classification/{text}")
def read_item(text: str):
    text_list = []
    text_list.append(text)
    out = clean_text(text_list) ## Clean the text
    seq = tokenizer.texts_to_sequences(out) ## Pass text to tokenizer to get vector
    padded = pad_sequences(seq, maxlen=50) ## padding to ensure same length of text is maintained
    pred = model.predict(padded) ## prediction
    print(pred)
    test_pred = ['Positive' if num>0.5  else 'Negative' for num in pred]
    return {"Sentiment": test_pred}
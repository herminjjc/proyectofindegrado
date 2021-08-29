
import joblib
from numpy.lib.function_base import vectorize
import pandas as pd
import spacy
import re
from spacy.lang.en.stop_words import STOP_WORDS
import en_core_web_sm 

def deleteRegularExpresion(text):
    if type(text) == str:
        text = re.sub('<[^>]*>', '', text)
        text = re.sub('[\W]+', '', text.lower())
        
    return text

def spacy_tokenizer(imput_data):

    parser = en_core_web_sm.load()
    mytokens = parser(imput_data)
     
    lema_list = []
    for token in mytokens:
        if token.is_stop is False:
            token_preprocessed = deleteRegularExpresion(token.lemma_)
            if token_preprocessed != '':
                lema_list.append(token_preprocessed)
    return lema_list


def clean_text(tex):
    #convertimos el textoa minusculas
    return tex.strip().lower()


class LogisticRegresion:
    """
    class that receives a review and uses the created model
    to predict sentiment
    """

    def __init__(self):
        self.model = joblib.load("modelos/classifier.joblib")
        self.vect = joblib.load("modelos/vectorize.joblib")

    def preprocesing(self, input_data): 
        return " ".join(spacy_tokenizer(clean_text(input_data)))
    
    def vectorize(self, input_data):
        return self.vect.transform([input_data])

    def predict(self, input_data):
        return self.model.predict_proba(input_data)

    def postprocesing(self, input_Data):
        
        if input_Data[1] > 0.5:
            return {"probability_negative": input_Data[0],"probability_positive": input_Data[1], "label": "positivo"  }
        else: 
            return {"probability_negative": input_Data[0],"probability_positive": input_Data[1], "label": "negativo" }



        








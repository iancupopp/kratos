import spacy
from spacy import displacy

text = "George Washington are mere."

nlp = spacy.load("ro_core_news_sm")
doc = nlp(text)
displacy.serve(doc, style="ent")
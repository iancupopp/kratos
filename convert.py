import srsly
import typer
import warnings
from pathlib import Path

import spacy
from spacy.tokens import DocBin
from spacy import displacy

nlp = spacy.blank("ro")
db = DocBin()
batch = srsly.read_json("train.json")
for sample in batch:
    str = ""
    for i in range(0, len(sample["tokens"])):
        word = sample["tokens"][i]
        str += word

        if sample["space_after"][i] == True:
            str += " "

    cnt = 0
    ents = []
    doc = nlp.make_doc(str)
    for i in range(0, len(sample["tokens"])):
        word = sample["tokens"][i]
        start = cnt
        end = cnt + len(word)
        span = doc.char_span(start, end, sample["ner_tags"][i])
        if span is not None:
            ents.append(span)

        cnt = end
        if sample["space_after"][i] == True:
            cnt += 1

    doc.ents = ents
    db.add(doc)
db.to_disk("train.spacy")
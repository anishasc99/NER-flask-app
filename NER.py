class ner(object):
    def __init__(self, e, n):
        self.email = e
        self.nlp = n
    def testing(self):
        #output_dir = './nlp'
        #nlp = spacy.load(output_dir)
        doc = self.nlp(self.email)
        print("Entities in '%s'" % self.email)
        labels = []
        text = []
        for ent in doc.ents:
            print(ent.label_, ent.text)
            labels.append(ent.label_)
            text.append(ent.text)
        return (labels,text)
        
    
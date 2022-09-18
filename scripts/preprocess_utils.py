import pandas as pd

class Preporcess:
    def __init__(self) -> None:
        print('Preprocess function called')
    
    def preprocess_tokens(self,tokens):
        enti = {}
        for t in tokens:

            if t['entityLabel'] in enti.keys():
                enti[t['entityLabel']] = enti[t['entityLabel']] + ','+t['text']
            else:
                enti[t['entityLabel']] = t['text']
        label = ""
        for k, v in enti.items():
            label += k+':'+v+"\n"
        return label
    
    def preprocess_document(self,train_df:pd.DataFrame):

        train_doc = []
        for i in range(train_df.shape[0]):
            ent = train_df.label.iloc[i]
            docu = train_df.document.iloc[i].replace("\n", " ")
            if len(ent) != 0:
                train_doc.append(docu+"\n\nExtracted Text:" +
                                '\n'+ent+"----\n")

        with open('../data/output/training_prompt.txt', 'w') as f:
            for item in train_doc:
                # write each item on a new line
                f.write("%s\n" % item.strip())
        return train_doc
    
    def clean_test_token(self,x):
        x = "".join(x)
        x = x.lower()
        x = x.lstrip()
        x = x.replace("\n",';')
        return x

    def clean_extracted_token(self,x):
        x = "".join(x)
        x = x.lower()
        x = x.replace("---","")
        x = x.lstrip()
        x = x.replace("\n",";")
        return x
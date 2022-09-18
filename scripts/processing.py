from cProfile import label
import pandas as pd

def process_tokens(tokens):
    enty={}
    for t in tokens:
        
        if t['entityLabel'] in enty.keys():
            enty[t['entityLabel']] = enty[t['entityLabel']] +','+t['text']
        else:
            enty[t['entityLabel']] = t['text']
    label = ""
    for k, v in enty.items():
        label += k+':'+v+"\n"
    return label

def entity_extraction(self,test_df:pd.DataFrame):
    test_doc = test_df.document.apply(
        lambda x: x.replace("\n", " ")+'\n\nExtracted Text:').to_list()
    return test_doc
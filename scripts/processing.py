from cProfile import label


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
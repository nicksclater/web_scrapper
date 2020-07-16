

import nltk
import json

def extract_entities(string):

    tagger = nltk.pos_tag(string.split())
    chucker = nltk.ne_chunk(tagger)

    tmp = {'people':[], 'places':[], 'organisation':[]}

    for i in chucker:
        if isinstance(i, nltk.tree.Tree):
            if i.label() == 'PERSON':
                tmp['people'] = i[0][0]
            elif i.label() == ('GPE' or 'LOCATION'):
                tmp['places'] = i[0][0]
            elif i.label() == 'ORGANIZATION':
                tmp['organisation'] = i[0][0]

    entities_json = json.dumps(tmp, indent=4)

    return entities_json



test1 = 'My name is Charlotte'
test2 = "I live in Heighington"
test3 = 'I work for the Council'

test_cases = [test1, test2, test3]

for test in test_cases:
    res = extract_entities(test)
    print(res)


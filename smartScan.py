import spacy
import json

def testFunc(ocrResult):
    print(ocrResult)
    return ocrResult



def impFunc(ocrResult):
    nlp = spacy.load('en_core_web_sm')
    sent = '''Olivia Wilson

    Real Estate Agent

    +123-456-7890 
    +123-456-7890

    www.reallygreatsite.com 
    hello@reallygreatsite.com

    7th North St., New York, ST 07086'''
    respDict = {}
    name = ''
    ts = nlp(sent)
    for ent in ts.ents:
        print(f'{ent.label_.upper():{10}} - {ent.text}')
        if ent.label_.upper() == 'PERSON':
            name = ent.text


    print(name)
    respDict["FullName"] = name
    ls = sent.split('\n')

    for ent in ls:
        temp = ent
        temp = temp.replace('-','')
        temp = temp.replace('+','')
        temp = temp.strip()
        if 'www.' in temp and '.com' in temp:
            print(ent +  '- Web')
            respDict["Website"] = ent
        elif '@' in temp and '.com' in temp:
            print(ent +  '- Email')
            respDict["Email"] = ent
        elif temp.isnumeric() and len(temp) == 10:
            print(ent +  '- Phone')
            respDict["Phone"] = ent
    print(name +  '- Name')
    respJson = json.loads(json.dumps(respDict))
    return respJson

#impFunc("abc")
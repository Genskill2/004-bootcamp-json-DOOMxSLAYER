import json

# Add the functions in this file
def load_function(filename):
    f= open(filename)
    data= json.load(f) 
    f.close()
    return data
    
def compute_phi(file,eventname):
    y=load_function('journal.json')
    n1p=0
    n0p=0
    np1=0
    np0=0
    n11=0
    n00=0
    n10=0
    n01=0
    for i in y:
        if eventname in i.events:

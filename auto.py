

'''
    trida: auto
        - cleny:
          -vyrobce
          -model
          -objem motoru
          -vykon

aby se dalo hezky porovnat
'''

class Auto:
    def __init__(self,vyrobce,model,objem,vykon):
        self.vyrobce=vyrobce
        self.model=model
        self.objem=objem
        self.vykon=vykon
    def __eq__(self,other):
        if isinstance(other,Auto):
            return self.vyrobce == other.vyrobce and self.model == other.model and self.objem == other.objem and self.vykon == other.vykon
        return False
        



a1 = Auto('skoda','oktavie',2.5,130)
a2 = Auto('BMW','530',3.0,200)
if a1 == a2:
    print('stejne')
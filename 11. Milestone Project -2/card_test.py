from random import randint
class CardDeck():
    
    from random import randint
    top = "----------"
    bottom = "\n----------"
    side = "\n|        |"
    symdict = {1:'♣',2:'♦',3:'♥',4:'♠'}
    middlel = "\n  "  
    middler = "  "
    
    def __init__(self):
        pass
        
    def card (self):
        x = 1
        while x < 3:
            suitn = randint(1,4)
            number = randint(1,13)
            card = print(self.top,self.side*2,self.middlel,f'{number}{self.symdict[suitn]}',self.middler,self.side*2,self.bottom)
            x += 1
            
pullcard = CardDeck()
pullcard.card()
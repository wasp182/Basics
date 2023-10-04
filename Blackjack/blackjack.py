import random
import tkinter


#load card images -> uising function
def load_cards(card_images):
    face_cards= ["king","queen","jack"]
    suites = ["spade","club","heart","diamond"]
    if tkinter.TkVersion ==8.6:
        extension = "png"
    else:
        extension="ppm"
    for suit in suites:
        for card in range(1,11):
            name="cards/{}_{}.{}".format(str(card),suit,extension)
            image=tkinter.PhotoImage(file=name)
            card_images.append((card,image))
    # face cards
        for card in face_cards:
            name="cards/{}_{}.{}".format(card,suit,extension)
            image=tkinter.PhotoImage(file=name)
            card_images.append((10,image))


#deal cards
def deal_cards(frame):
    next_card = deck.pop(0)
    # put the card at back of  deck
    deck.append(next_card)
    tkinter.Label(frame,image=next_card[1],relief='raised').pack(side='left')
    return next_card

def score_hand(hand):
    score=0
    ace=False
    for next_card in hand:
        card_value = next_card[0]
        if card_value==1 and not ace:
            ace=True
            card_value=11
        score+=card_value
        if score>21 and ace:
            score-=10
            ace=False
    return score

# below to ensure button and deal functions are configured as command option
# doesn't allow for arguments
def deal_dealer():
    dealer_score=score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)
    while 0<dealer_score<17:
        dealer_hand.append(deal_cards(dealer_card_frame))
        dealer_score_label.set(dealer_score)
        dealer_score=score_hand(dealer_hand)
    player_score = score_hand(player_hand)
    if player_score>21:
        result_text.set("Dealer Wins")
    elif dealer_score > 21 or player_score>dealer_score:
        result_text.set("Player wins")
    elif dealer_score<player_score:
        result_text.set("Dealer Wins")
    else:
        result_text.set("Draw")


def deal_player():
    player_hand.append(deal_cards(player_card_frame))
    player_score=score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score>21:
        result_text.set("Dealer Wins")

    # global player_score
    # global player_ace
    # # here player_score has been assigned new variable in local func
    # # hence python will refer to this local variable and not the global var
    # card_value= deal_cards(player_card_frame)[0]
    # if card_value==1 and not player_ace:
    #     card_value=11
    # player_score+=card_value
    # if player_score> 21 and player_ace:
    #     player_score-=10
    # player_score_label.set((player_score))
    # if player_score>21:
    #     result_text.set("Dealer Wins")
def init():
    deal_player()
    dealer_hand.append(deal_cards(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # destroy frames
    dealer_card_frame.destroy()
    player_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame,background='green')
    dealer_card_frame.grid(row=0,column=1,sticky="ew",rowspan=2)
    player_card_frame = tkinter.Frame(card_frame,background="green")
    player_card_frame.grid(row=2,column=1,sticky='ew',rowspan=2)
    dealer_hand = []
    player_hand = []
    result_text.set("")
    #start new instance
    init()

def play():
    #start new instance
    init()
    mainWindow.mainloop()

mainWindow=tkinter.Tk()
#setup screen and frames
mainWindow.title("Blackjack")
mainWindow.geometry("640x480")
mainWindow.config(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow,textvariable=result_text)
result.grid(row=0,column=0,columnspan=3)

#card frame
card_frame = tkinter.Frame(mainWindow,relief="sunken",borderwidth=2,background="green")
card_frame.grid(row=1,column=0,sticky='ew',rowspan=2,columnspan=3)

dealer_score_label= tkinter.IntVar()
tkinter.Label(card_frame,text="Dealer",background='blue',fg="white").grid(row=0,column=0)
tkinter.Label(card_frame,textvariable=dealer_score_label,background='blue',fg="white").grid(row=1,column=0)

#embed frame to hold dealer card images
dealer_card_frame= tkinter.Frame(card_frame,background="green")
dealer_card_frame.grid(row=0,column=1,sticky="ew",rowspan=2)


player_score_label = tkinter.IntVar()
# player_score=0
# player_ace=False

tkinter.Label(card_frame,text="Player",background='blue',fg="white").grid(row=2,column=0)
tkinter.Label(card_frame,textvariable=player_score_label,background='blue',fg="white").grid(row=3,column=0)

#embedded plater cards to hold images
player_card_frame = tkinter.Frame(card_frame,background="green")
player_card_frame.grid(row=2,column=1,sticky='ew',rowspan=2)

#button frames
button_frame=tkinter.Frame(mainWindow)
button_frame.grid(row=4,column=0,columnspan=3,sticky='w')
dealer_button=tkinter.Button(button_frame,text="Dealer",command=deal_dealer)
player_button=tkinter.Button(button_frame,text="Player",command=deal_player)
clear_button=tkinter.Button(button_frame,text="Clear",command=new_game)

dealer_button.grid(row=0,column=0)
player_button.grid(row=0,column=1)
clear_button.grid(row=0,column=2)

cards=[]
load_cards(cards)
print(cards)

#create new card and shuffle
deck=list(cards)
random.shuffle(deck)

#initalising the game
dealer_hand = []
player_hand=[]



if __name__ == '__main__':
    play()

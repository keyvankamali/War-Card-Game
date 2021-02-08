import random
suits = ('Club', 'Heart', 'Spades', 'Diamond')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six':6, 'Seven': 7, 'Eight': 8,
         'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

number_of_card_agreement = 5

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

three_of_diamond = Card('Diamond', 'Three') 
two_of_club = Card('club', 'Two')

class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'{self.name} now has {len(self.all_cards)} card.'

   


# Game setup
player_one = Player('One')
player_two = Player('Two')
new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.all_cards.append(new_deck.deal_one())
    player_two.all_cards.append(new_deck.deal_one())




# while loops game_on and 
game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f'Game is on playe round : {round_num}')

    if len(player_one.all_cards) == 0:
        print('Player one is out of card and player two wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player two is out of card and player one wins!')
        game_on = False
        break

    # start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())
    # print(player_one_cards)

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())
    # print(player_two_cards)

    # print(player_one_cards[-1])

    # while at war
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war =False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        
        else:
            print("WAR")

            if len(player_two.all_cards) < 5:
                print('Player Two has no enough cards, Player One wins.')
                game_on =False
                break

            elif len(player_one.all_cards) < 5:
                print('Player One has no enough cards, Player Two wins.')
                game_on =False
                break
                

            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
        
                    





# new_player = Player('Jose')
# print(new_player)
# new_card = Card('Diamond', 'Three')
# # new_player.add_cards(new_card)
# # print(new_player)
# new_player.add_cards([new_card, new_card, new_card])
# # print(new_player)
# print(new_player.player_card_list[0])

# myDeck = Deck()
# first_card = myDeck.all_cards[-1]
# print(first_card)

# for card_object in myDeck.all_cards:
#     print(card_object)

# myDeck.shuffle()
# for card_object in myDeck.all_cards:
#     print(card_object)

# myDeck = Deck()
# myDeck.shuffle()
# print(len(myDeck.all_cards))
# mynewcard = myDeck.deal_one()
# print(mynewcard)
# print(len(myDeck.all_cards))
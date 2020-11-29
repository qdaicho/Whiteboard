#========================Pre program===========================================================
import random #this module is used for the shuffle function to randomize the flash cards

#Below are all important variables which have been initialized
#Notice how variables with single elements are kept in lists, it may seem odd,
# but this allows us to change the value of these variable within the functions
card_toggle = [0]
prompt_list = []
answer_list = []
cards_file = open("Flash_Cards.txt", 'r')
cards_data = cards_file.read()
cards = cards_data.split("\n\n")
cards.pop(-1)
for i in cards:
    prompt_list.append(i.split("\n")[0].replace('[', '').replace(']', '').replace("P:", ""))
    answer_list.append(i.split("\n")[1].replace('[', '').replace(']', '').replace("A:", ""))
current_prompt = [prompt_list[0]]
current_answer = [answer_list[0]]
screen_card = [prompt_list[0]]
card_count = [0]
deck_length = len(prompt_list)

#========================Functions===========================================================
def refresh(prompt_list, answer_list, current_prompt, current_answer, card_toggle, screen_card, card_count): #refreshes the deck
    cards_file = open("Flash_Cards.txt", 'r')  #reading in the flashcards from texfile
    cards_data = cards_file.read()
    cards = cards_data.split("\n\n") #formatting the flash cards for use
    cards.pop(-1)
    prompt_list *= 0
    answer_list *= 0
    current_prompt *= 0
    current_answer *= 0   #variable lists are cleared during refresh before new values can be inserted
    card_toggle *= 0
    screen_card *= 0
    card_count *= 0

    for i in cards: #inserting new values to flash cards
        prompt_list.append(i.split("\n")[0].replace('[', '').replace(']', '').replace("P:", ""))
        answer_list.append(i.split("\n")[1].replace('[', '').replace(']', '').replace("A:", ""))

    current_prompt.append(prompt_list[0]) #inserting new values to variables useful for understanding what it the current card
    current_answer.append(answer_list[0])
    card_toggle.append(0)
    screen_card.append(prompt_list[0])
    card_count.append(0)


def shuffle(prompt_list, answer_list, current_prompt, current_answer): #shuffles the cards in the deck
    Index = list(zip(prompt_list, answer_list))
    random.shuffle(Index)
    prompt_list, answer_list = zip(*Index)

    cards_file = open("Flash_Cards.txt", 'w')
    for i in range(len(prompt_list)):
        cards_file.write("P:[" + prompt_list[i] + "]\n")
        cards_file.write("A:[" + answer_list[i] + "]\n\n")


def card_flip(card_toggle, screen_card, card_count, prompt_list, answer_list): 
    #flips the card, basically tells if we are looking at the prompt or answer of a card
    screen_card *= 0
    if card_toggle[0] == 0:
        card_toggle *= 0
        card_toggle.append(1)
        screen_card.append(answer_list[card_count[0]])
    elif card_toggle[0] == 1:
        card_toggle *= 0
        card_toggle.append(0)
        screen_card.append(prompt_list[card_count[0]])


def next_card(card_count, card_toggle, screen_card, prompt_list):
    #sets the current card to next card in the current deck

    if card_count[0] != deck_length - 1:
        temp_var = card_count[0]
        card_count *= 0
        card_count.append(temp_var + 1)
        if card_toggle[0] == 1:
            card_toggle *= 0
            card_toggle.append(0)

        screen_card *= 0
        screen_card.append(prompt_list[card_count[0]])


def prev_card(card_count, card_toggle, screen_card, prompt_list):
    #sets the current card to previous card in the current deck
    if card_count[0] != 0:
        temp_var = card_count[0]
        card_count *= 0
        card_count.append(temp_var - 1)
        if card_toggle[0] == 1:
            card_toggle *= 0
            card_toggle.append(0)

        screen_card *= 0
        screen_card.append(prompt_list[card_count[0]])

#============================instructions========================================================

# functions must be called with the below parameters:
#------------------------------------------------------
# card_flip(card_toggle,screen_card)
#shuffle(prompt_list, answer_list,current_prompt,current_answer)
# refresh(prompt_list,answer_list,current_prompt,current_answer,card_toggle,screen_card,card_count)
#next_card(card_count, card_toggle,screen_card,prompt_list)


# refresh must and can only be called after shuffle is called
# all other functions work on their own

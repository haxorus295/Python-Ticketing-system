from easygui import *   


def cards_view():
    text = 'Your cards\n'
    TITLE='Inventory'
    for character in sorted(cards):  # adding the Character name
        text = text + '\n'
        text = text + character
        text = text + ':    '
        for stat in cards[character]:  # adding the Characters and stats
            text = text + stat + ': ' + str(cards[character][stat]) \
                + ' | '
        text = text + '\n'
        print (text)
    msgbox(text, TITLE)
    main()


def search():
    cards_amount = len(cards)
    if cards_amount == 0:  # checks if there isn't any cards in the dictionary
        global card, text, TITLE, options, details
        Title = 'Card search'
        TEXT = "There aren't any cards in your inventory, try adding some more."
        msgbox(TEXT, Title)
        main()
    text2 = 'Enter card name.'
    title = 'Card search'
    card = enterbox(text2, title)
    if card is None:
        main()
    card = card.capitalize()
    if card in cards:  # checks if the character the user searched for exists
        text = card + '\n'
        text = text + '----------\n'
        for stat in cards[card]:  # adding the Characters and there stats
            text = text + stat + ': ' + str(cards[card][stat])
            text = text + '\n'
        options = ['Change card details', 'continue']
        change = buttonbox(text, title, options)
        if change is None:
            main()
        elif change == 'Change card details':
            text2 = 'Would you like to change the name or the stats of' \
                + card
            options = ['Card name', 'Card statistics']
            title = 'Card search'
            change2 = choicebox(text2, title, options)  # asks wether the user wants to change the name or the statistics
            if change2 is None:
                main()
            elif change2 == 'Card name':
                texts = 'Enter new name below'
                name = enterbox(texts).capitalize()
                if name is None:
                    main()
                while 1:
                    if name == None:  # checks if the user fills in all the information
                        break
                    texts = ''
                    if name.strip() == '':
                        texts = texts + 'You must enter a name\n\n'
                    
                    if name in cards:  # checks if the character is already in the dictionary
                        texts = texts + name + ' Is already in your inventory.\n\n'
                    
                    if texts == '':  # no problems found
                        break
                    name = enterbox(texts).capitalize()

                cards[name] = cards.pop(card)  # changes the card name
                main()
            text = 'What stats would you like to make to ' + card
            TITLE = 'Card change'
            options = ['Strength', 'Speed', 'Stealth', 'Cunning']
            info = []
            for stats in cards[card]:  # saves the current values of the card to a list
                info.append(str(cards[card][stats]))
            details = info
            card_change_error_check()
        main()
    msgbox('That card is not in your inventory', title='Card search')  # tells the user the character they searched for is not in their inventory

    search()


def card_add_pre():
    global text, details
    text = 'Enter the details of the monster below.'
    details = []
    card_add()


def card_add():
    global text, details
    TITLE = 'Card add'
    OPTIONS = ['Name', 'Strength', 'Speed', 'Stealth', 'Cunning']
    details = multenterbox(text, TITLE, OPTIONS, details)
    if details is None:
        main()
    while 1:
        if details == None:  # checks if the user fills in all the information
            break
        text = ''
        for i in range(len(OPTIONS)):
            if details[i].strip() == '':
                text = text + '''"%s" is  required.

''' % OPTIONS[i]
        if text == '':  # no problems found
            break
        card_add()
    while 1:
        text = ''
        name = details[0].capitalize()  # checks if the user enters letters in the statistics boxes
        strength = details[1]
        speed = details[2]
        stealth = details[3]
        cunning = details[4]
        for i in range(len(OPTIONS)):
            if i != 0:
                if details[i].isdigit():
                    text = text
                else: text = text + '"%s" must be not contain any letters or special characters.\n\n' % OPTIONS[i]
        if text == '':  # no problems found
            break
        card_add()
    while 1:
        text = ''
        for i in range(len(OPTIONS)):  # checks if the user enters a stat with a value higher than 25 of lower than 1
            if i != 0:
                value = int(details[i])
                if value < 26 and value > 0:
                    text = text
                else: text = text + '"%s" cannot be higher than 25 or lower than 1.\n\n' % OPTIONS[i]
        if text == '':  # no problems found
            break
        card_add()
    while 1:
        text = ''
        if name in cards:  # checks if the character is already in the dictionary
            text = text + name + ' Is already in your inventory.'
        if text == '':  # no problems found
            break
        card_add()
    name = details[0].capitalize()  # checks if the user enters letters in the statistics boxes
    strength = str(details[1])
    speed = str(details[2])
    stealth = str(details[3])
    cunning = str(details[4])
    cards_change = {}
    cards_change[name] = {}
    cards_change[name]['Strength'] = strength
    cards_change[name]['Speed'] = speed
    cards_change[name]['Stealth'] = stealth
    cards_change[name]['Cunning'] = cunning
    text = name + '\n'
    text = text + '----------\n'
    for stat in cards_change[name]:  # adding the Characters and there stats
        text = text + stat + ': ' + str(cards_change[name][stat])
        text = text + '\n'
    change = \
        ynbox('''Would you like to make any changes to the card

'''
              + text, title='Card add')  # asks the user if they want to make any changes
    if change is None:
        main()
    elif change == 0:
        cards[name] = {}  # adds the character to the dictionary
        cards[name]['Strength'] = strength
        cards[name]['Speed'] = speed
        cards[name]['Stealth'] = stealth
        cards[name]['Cunning'] = cunning
        main()
    text = 'Enter the details of the monster below.'
    card_add()


def card_change():
    cards_amount = len(cards)
    if cards_amount == 0:  # checks if there isn't any cards in the dictionary
        msgbox("There aren't any cards in your inventory, try adding some more."
               , title='Card change')
        main()
    global text, TITLE, options, card, details
    text1 = 'What card would you like to make changes to?'
    TITLE = 'Card change'
    options = cards
    card = choicebox(text1, TITLE, options)  # asks the what card they want to change
    if card is None:
        main()
    text2 = 'Would you like to change the name of the stats of' + card
    if card is None:
        main()
    options = ('Card name', 'Card statistics')
    change = choicebox(text2, TITLE, options)  # asks wether the user wants to change the name or the statistics
    if change is None:
        main()
    elif change == 'Card name':
        texts = 'Enter new name below'
        name = enterbox(texts).capitalize()
        if name is None:
            main()
        while 1:
            if name == None:  # checks if the user fills in all the information
                break
            texts = ''
            if name.strip() == '':
                texts = texts + 'You must enter a name\n\n'
            
            if name in cards:  # checks if the character is already in the dictionary
                texts = texts + name + ' Is already in your inventory.\n\n'
            
            if texts == '':  # no problems found
                break
            name = enterbox(texts).capitalize()
        cards[name] = cards.pop(card)  # changes the card name
        main()
    info = []
    for stats in cards[card]:  # saves the current values of the card to a list
        info.append(str(cards[card][stats]))
    details = info
    text = 'What stats would you like to make to ' + card
    options = ['Strength', 'Speed', 'Stealth', 'Cunning']
    card_change_error_check()


def card_change_error_check_pre():
    text2 = 'Would you like to change the name or the stats of' + card
    options = ['Card name', 'Card statistics']
    TITLE = 'Card change'
    change2 = choicebox(text2, TITLE, options)  # asks wether the user wants to change the name or the statistics
    if change2 == 'Card name':
        texts = 'Enter new name below'
        name = enterbox(texts, TITLE).capitalize()
        if name is None:
            main()
        while 1:
            if name == None:  # checks if the user fills in all the information
                break
            texts = ''
            if name.strip() == '':
                texts = texts + 'You must enter a name'
            if texts == '':  # no problems found
                break
            name = enterbox(texts, TITLE).capitalize()
        cards[name] = cards.pop(card)  # changes the card name
        main()
    text1 = 'What stats would you like to make to ' + card
    TITLE = 'Card change'
    options = ['Strength', 'Speed', 'Stealth', 'Cunning']
    info = []
    for stats in cards[card]:  # saves the current values of the card to a list
        info.append(str(cards[card][stats]))
    details = info
    global text
    text = 'Enter the details of the monster below.'
    card_change_error_check()


def card_change_error_check():
    global text, TITLE, options, card, details
    details = multenterbox(text, TITLE, options, details)  # gets the new stats for the card
    if details is None:
        main()
    strength = details[0]  # makes the changes to the card
    speed = details[1]
    stealth = details[2]
    cunning = details[3]
    if details is None:
        main()
    while 1:
        if details == None:  # checks if the user fills in all the information
            break
        text = ''
        for i in range(len(options)):
            if details[i].strip() == '':
                text = text + '''"%s" is  required.

''' % options[i]
        if text == '':  # no problems found
            break
        card_change_error_check()
    while 1:
        text = ''
        for i in range(len(options)):
            if details[i].isdigit():  # checks if the user enters letters in the statistics boxes
                text = text
            else: text = text \
                + '''"%s" must be not contain any letters or special characters.

''' \
                % options[i]
        if text == '':  # no problems found
            break
        card_change_error_check()
    while 1:
        text = ''
        for i in range(len(options)):  # checks if the user enters a stat with a value higher than 25 of lower than 1
            value = int(details[i])
            if value < 26 and value > 0:
                text = text
            else: text = text \
                + '''"%s" cannot be higher than 25 or lower than 1.

''' \
                % options[i]
        if text == '':  # no problems found
            break
        card_change_error_check()
    strength = str(details[0])
    speed = str(details[1])
    stealth = str(details[2])
    cunning = str(details[3])
    cards_change = {}
    cards_change[card] = {}
    cards_change[card]['Strength'] = strength
    cards_change[card]['Speed'] = speed
    cards_change[card]['Stealth'] = stealth
    cards_change[card]['Cunning'] = cunning
    text = card + '\n'
    text = text + '----------\n'
    for stat in cards_change[card]:  # adding the Characters and there stats
        text = text + stat + ': ' + str(cards_change[card][stat])
        text = text + '\n'
    change = \
        ynbox('''Would you like to make any changes to the card

'''
              + text, title='Card change')  # asks the user if they want to make any changes
    if change is None:
        main()
    elif change == 0:
        cards[card]['Strength'] = strength
        cards[card]['Speed'] = speed
        cards[card]['Stealth'] = stealth
        cards[card]['Cunning'] = cunning
        main()
    else: card_change_error_check_pre()


def card_remove():
    cards_amount = len(cards)
    if cards_amount == 0:  # checks if there isn't any cards in the dictionary
        msgbox("There aren't any cards in your inventory, try adding some more."
               , title='Card remove')
        main()
    elif cards_amount == 1:  # checks if there is one card left in the dictionary
        text = '''There is only one card in your inventory, are you sure you want to delete it?
        
'''
        for key in cards :
            text = text + key
        sure = \
            ynbox(text
                  , title='Card remove')
        if sure is None:
            main()
        elif sure == 1:
            last_card = str(*cards)
            cards.pop(last_card)
            main()
    else:
        TEXT = 'What card would you like to remove?'
        TITLE = 'Card remove'
        OPTIONS = cards
        card_name = multchoicebox(TEXT, TITLE, OPTIONS)  # asks the user what card-cards they want to remove
        if card_name is None:
            main()
        text = ''
        for card in card_name:  # adding the Characters
            text = text + card
            text = text + '\n'
        sure = \
            ynbox('''Are you sure you want to permanently remove the card-cards

'''
                  + text, title='Card remove')  # asks the user if they want to remove the cards-card they selected
        if sure is None:
            main()
        elif sure == 1:
            for i in range(len(card_name)):  # removes the card-cards
                cards.pop(card_name[i])
            main()  # goes back to the menu


# all the cards

cards = {
    'Stoneling': {
        'Strength': 7,
        'Speed': 1,
        'Stealth': 25,
        'Cunning': 15,
        },
    'Vexscream': {
        'Strength': 1,
        'Speed': 6,
        'Stealth': 21,
        'Cunning': 19,
        },
    'Dawnmirage': {
        'Strength': 5,
        'Speed': 15,
        'Stealth': 18,
        'Cunning': 22,
        },
    'Blazegolem': {
        'Strength': 15,
        'Speed': 20,
        'Stealth': 23,
        'Cunning': 6,
        },
    'Websnake': {
        'Strength': 7,
        'Speed': 15,
        'Stealth': 10,
        'Cunning': 5,
        },
    'Moldvine': {
        'Strength': 21,
        'Speed': 18,
        'Stealth': 14,
        'Cunning': 5,
        },
    'Vortexwing': {
        'Strength': 19,
        'Speed': 13,
        'Stealth': 19,
        'Cunning': 2,
        },
    'Rotthing': {
        'Strength': 16,
        'Speed': 7,
        'Stealth': 4,
        'Cunning': 12,
        },
    'Froststep': {
        'Strength': 14,
        'Speed': 14,
        'Stealth': 17,
        'Cunning': 4,
        },
    'Wispghoul': {
        'Strength': 17,
        'Speed': 19,
        'Stealth': 3,
        'Cunning': 2,
        },
    }

print(cards)
def main():
    text = ''
    title = 'Menu'
    choices = (
        'View cards',
        'Search for a card',
        'Add a card',
        'Remove a card',
        'Change a cards details',
        'Exit',
        )
    for spaces in range(32):
        text = text + ' '
    text = text + 'Cards of monsters\n'

    for spaces in range(38):
        text = text + ' '
    text = text + 'Menu'

    menu = buttonbox(text, title, choices)
    if menu == 'View cards':
        cards_view()
    
    elif menu == 'Search for a card':
        search()
    
    elif menu == 'Add a card':

        card_add_pre()
    elif menu == 'Remove a card':

        card_remove()
    elif menu == 'Change a cards details':

        card_change()
    elif menu == 'Exit':

        exit
    elif menu is None:

        exit


main()
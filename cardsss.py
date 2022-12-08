"""
card_playing_compatibility_idears
CS 021, Clayton Cafiero, Fall 2022, Isabella Shoemaker Ross

"""

# imports

import csv
import random


# Functions



def amount_of_players( dct, players ):
# gives you
# within_range = player_range

# does it match?
# this function deals with seeing if the ideal and current players match

    lst = []

    for key in dct:
        if int() == players:
#            print(key)
            lst.append(key)


    return lst



def player_range( dct, x, players ):
# gives you
# within_range = player_range

# this creates a list of viable games, welbiet not the most simplified way to do it; working 
# also returns information from the first list for tinkering

    larst = []
    larst2 = []

    for key in dct:
        for q in x:
            if key == q:
                larst.append(key)

    for key in dct:

# creating a range
        low = int(dct[key][1]) - 1
        high = int(dct[key][2]) + 1

        if key not in larst:
            if players > low and players < high:
                larst2.append(key)


    return larst2



def more_compatible( dct, players, exact_players_match, within_range ):
# gives you 
# possible_game = more_compatible

# weighting the compatibilty of games by player capacities

    games = {}

    for key in dct:

        for x in exact_players_match:
            if key == x:
                games[key] = 1

        middle = (int(dct[key][2]) - int(dct[key][1]))/2 + int(dct[key][1])

        for x in within_range:
            if key == x:
                mar = players - middle
                games[key] = 1 - (0.1 * (mar))

        if key not in games:
            games[key] = 0

    return games



def weighted_list( dct, possible_game, otherlist ):
# gives you
# weighted = weighted_list

# give the games percentages and then rank them?

    for x in dct:
        for key in dct[x][4]:
            for mar in otherlist:
                if key == mar:
                    possible_game[x] = int(possible_game[x]) + 2
                else:
                    possible_game[x] = int(possible_game[x])

    return possible_game



def sort_weighted( weighted ):
# gives you
# rankings = sort_weighted

# sorted is a function
# weighted.items gives the list of tuples of ( items, weight ) in dic
# lambda is a function
# we tell it what information to sort and how
# item[0] would return the first part of the tuple by alphabetical order
# reverse = True is the parameter for how it is sorted
    return dict(sorted(weighted.items(), key = lambda item: item[1], reverse = True ))



def random_of_option( rankings ):
# gives you
# rando_of_top = random_of_option

# of the options, returns random sample of top half after removing impossible options
    lst = []
    bar = []

    for game in rankings:
         if rankings[game] > 0:
            lst.append(game)

    bar = lst[:(len(lst) + 1) //2]

    return random.sample(bar, 1)



if __name__ == '__main__':

    # opening the game dictionary as it currently stands

    dct = {}
    
    with open('tester.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            dct[row[0]] = row[1:]



    # intro

    print(f'\nWelcome to card game compatibility')
    print(f"from our library, let's try to find you and/or your group")
    print(f'the most compatible game')
    print(f'or at least help with your current road block :/ \n')



    # input validation
    # eventually have this branch for customization in a personal library

    print(f"\nPlease move the cursor over to the right by pressing  ' the space bar '  once : \n")
    checker = input(f"enter when finished :  ")

    if checker == ' ':
         print(f"\nsweet, that's gonna be called the* next *buton")

    elif checker != ' ':
        print(f"perhaps there was a mistunderstanding \n")
        checker = input(f"Please move the cursor over to the right by pressing  ' the space bar '  once :  ")



    # player inputs: amount, house, speed, bluffing, betting

    players = int(input("\n\nHow many players are in this game? "))

    if players > 0 and players > 10:
        players = int(input("\nPlease pick a value between 1 and 10; even if you have more people... "))

    print(f'\nWhat kind of game were are you thinking... ')
    print(f'For the following questions, please chose  y for (yes)  or  n for (no)  :')

    larson_lst = [] 

    r = 1
    while r == 1:
    
        if players > 1:

            house = input("\nWould you like the game to include a house/dealer?  ")

            if house != 'y' and house != 'Y' and house != 'n' and house != 'N':
                print(f"\nyou did not input a value, hope the you're okay with that")
                print(f"esp. because that might continue to happen :? \n")

                print(f":? press any value over 1 to restart inputs, or next for default ")
                r = input(f"confirming: n is default and will be chosen : ")
                house = 'n'


            speed = input("Would you like the game to be quick paced? ")

            if speed != 'y' and speed != 'Y' and speed != 'n' and speed != 'N':
                print(f"\nyou did not input a value, hope the you're okay with that")
                print(f"esp. because that might continue to happen :? \n")

                print(f":? press any value over 1 to restart inputs, or next for default ")
                r = input(f"confirming: n is default and will be chosen : ")
                speed = 'n'


            bluffing = input("Would you like bluffing? ")

            if bluffing != 'y' and bluffing != 'Y' and bluffing != 'n' and bluffing != 'N':
                print(f"\nyou did not input a value, hope the you're okay with that")
                print(f"esp. because that might continue to happen :? \n")

                print(f":? press any value over 1 to restart inputs, or next for default ")
                r = input(f"confirming: n is default and will be chosen : ")
                bluffing = 'n'

        if players >= 1:

            bet = input("Would you like the game to include betting? ")

            if bet != 'y' and bet != 'Y' and bet != 'n' and bet != 'N':
                print(f"\nyou did not input a value, hope the you're okay with that")
                print(f"esp. because that might continue to happen :? \n")

                print(f":? press any value over 1 to restart inputs, or next for default ")
                r = input(f"confirming: n is default and will be chosen : ")
                bet = 'n'


        r = 2
        print("\n")


# add to a  results file?

# commonly used paramaters
    otherlist = [house, speed, bluffing, bet]


    exact_players_match = amount_of_players( dct, players )
    print (f'the match for exact_players_match = amount_of_players  is {exact_players_match}')

    within_range = player_range( dct, exact_players_match, players)
    print (f'the games that are within_range = player_range  is {within_range}')

    possible_game = more_compatible( dct, players, exact_players_match, within_range )
    print (f'confusions possible_game = more_compatible  is {possible_game}')
# format of a dict weighing the compatibilty of games by player capacities

    weighted = weighted_list( dct, possible_game, otherlist )
    print (f'what happened here weighted = weighted_list  is {weighted}')

    rankings = sort_weighted( weighted )
    print (f'the rankings = sort_weighted  are {rankings}')

    rando_of_top = random_of_option( rankings )
    print (f'the rando_of_top = random_of_option  is {rando_of_top}')


# results declarations!!
    print("\nyey, resultss....\n")

    print(f"An idea... if you'd like to to narrow it down, would be... {rando_of_top[0]} ? \n")

    results = input(f"\nWould you like to see the {rando_of_top[0]} follow up menu? submit ' y for yes ' or ' q for quit ': ")

    if results == 'y':
        print(f"\nWelcome to your waiting room options!\n")

        print(f"A: show me all of the options! and reshuffle for new game choice")
        print(f"B: get a link to something that'll give game instructions\n")

    if results == 'q':
        quit()

    #    print(f"Including all of theseeee {possible_game}...\n")
    menu_choice = input(f"your options are... A , B , (q for quit) ... ")
    if menu_choice.lower() == 'a':
        for name in rankings:
            print (name)
        print(f"\nBut you could play any of the above as well (the farthest away is the most compatible)\n")
        print(f"you had {rando_of_top[0]} ...and your new option is  {random_of_option(rankings)[0]} ? \n")
        menu_choice = input(f"your options are... a , b or q for quit ... ")

    if menu_choice.lower() == 'b':
    # flask
        print(f"\nnot sure why, but guess you wanted a url so here it is: ")
        print(f"https://bicyclecards.com/how-to-play/")
        print(f"\n** in the upper right corner of the website is the search bar if you don't want to do this all again **\n\n")
        menu_choice = input(f"your options are... 'A': reshuffle , 'B' or 'q' for quit ... ")
        print(f"\n")
    
    menu_choice = input(f" 'a' to reshuffle , 'b' to look up instructions, , 'q' for quit \n..your answer is;.. ")
    
    if menu_choice.lower() == 'q':
        quit()

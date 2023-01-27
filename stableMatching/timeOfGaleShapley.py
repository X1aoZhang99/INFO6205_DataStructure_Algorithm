import time
import argparse
import random

def main(args):
    num = args.size

    for i in range(13):

        # initialize the preferences of men and women, depending on if the user choose the worstcase option
        menPref = []
        womenPref = []
        
        for _ in range(num):
            arr = [n for n in range(num)]
            random.shuffle(arr)
            menPref.append(arr)
            womenPref.append(arr.copy())
        random.shuffle(menPref)
        random.shuffle(womenPref)
        
        timeStart = time.time()
        result = basicGaleShapley(menPref, womenPref)
        timeEnd = time.time()
        print('n = ' , num,'Time used: ', timeEnd - timeStart)
        num *= 2


def basicGaleShapley(menPref, womenPref):
    # The set stores unmatched men and the dictionary stores temporary spouse of women
    unmatchedMan = set()
    spouseOfWoman = dict()
    for i in range(len(menPref)):
        unmatchedMan.add(i)
        spouseOfWoman[i] = None

    while unmatchedMan:
        proposeMan = unmatchedMan.pop()
        # If error happen
        if not menPref[proposeMan]:
            return dict()

        proposedWoman = menPref[proposeMan].pop(0)
        if spouseOfWoman[proposedWoman] is None:
            spouseOfWoman[proposedWoman] = proposeMan
        elif womenPref[proposedWoman].index(spouseOfWoman[proposedWoman]) > womenPref[proposedWoman].index(proposeMan):
            unmatchedMan.add(spouseOfWoman[proposedWoman])
            spouseOfWoman[proposedWoman] = proposeMan
        else:
            unmatchedMan.add(proposeMan)

    return spouseOfWoman




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test for argparse')
    parser.add_argument('--size', '-s', default=8, help='the size of the matching')
    args = parser.parse_args()
    main(args)
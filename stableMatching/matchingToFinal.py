
import argparse
import random

def main(args):
    num = args.size

    # initialize the preferences of men and women

    menPrefList = []
    womenPrefList = []
    menPref = dict()
    womenPref = dict()
    
    for _ in range(num):
        arr1 = [n for n in range(num)]
        arr2 = [n for n in range(num, 2 * num)]
        random.shuffle(arr1)
        random.shuffle(arr2)
        menPrefList.append(arr2)
        womenPrefList.append(arr1)
    random.shuffle(menPrefList)
    random.shuffle(womenPrefList)
    
    for i in range(num):
        manPref = menPrefList.pop()
        womanPref = womenPrefList.pop()
        menPref[i] = manPref
        womenPref[i + num] = womanPref
    
    result = basicGaleShapley(menPref, womenPref)
    print(result)

    while True:
        winners = []
        for key, value in result.items():
            randomNum = random.randint(0, 1)
            if randomNum:
                winners.append(key)
            else:
                winners.append(value)
        if len(winners) == 1:
            break
        newMenList = winners[len(winners)//2:]
        newWomenList = winners[:len(winners)//2]
        newMenPref = dict()
        newWomenPref = dict()
        for man in newMenList:
            newMenPref[man] = newWomenList.copy()
            random.shuffle(newWomenList)
        for woman in newWomenList:
            newWomenPref[woman] = newMenList.copy()
            random.shuffle(newMenList)
        result = basicGaleShapley(newMenPref, newWomenPref)
        print(result)
    print('winner is', winners[0])

    


def basicGaleShapley(menPref, womenPref):
    # The set stores unmatched men and the dictionary stores temporary spouse of women
    unmatchedMan = set()
    spouseOfWoman = dict()
    for i in range(len(menPref)):
        unmatchedMan.add(i)
        spouseOfWoman[i] = None

    while unmatchedMan:
        # Pop a unmatchedman to propose
        proposeMan = unmatchedMan.pop()

        # If error happen
        if not menPref[proposeMan]:
            return dict()

        # Prepared to proposed to his top rated woman
        proposedWoman = menPref[proposeMan].pop(0)

        # She is unmatched
        if spouseOfWoman[proposedWoman] is None:
            spouseOfWoman[proposedWoman] = proposeMan
        # This man is her better choice
        elif womenPref[proposedWoman].index(spouseOfWoman[proposedWoman]) > womenPref[proposedWoman].index(proposeMan):
            unmatchedMan.add(spouseOfWoman[proposedWoman])
            spouseOfWoman[proposedWoman] = proposeMan
        # Rejected
        else:
            unmatchedMan.add(proposeMan)

    return spouseOfWoman




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test for argparse')
    parser.add_argument('--size', '-s', default=8, help='the size of the matching')
    args = parser.parse_args()
    main(args)
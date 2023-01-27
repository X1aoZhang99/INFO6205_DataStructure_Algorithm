
import argparse
import random

def main(args):
    num = args.size

    # initialize the preferences of men and women, depending on if the user choose the worstcase option
    if args.worstcase:
        menPref = [
            [0,1,2,3,4],
            [1,2,3,0,4],
            [2,3,0,1,4],
            [3,0,1,2,4],
            [0,1,2,3,4]
        ]
        womenPref = [
            [1,2,3,4,0],
            [2,3,4,0,1],
            [3,4,0,1,2],
            [4,0,1,2,3],
            [0,1,2,3,4]
        ]
        num = 5
    else:
        menPref = []
        womenPref = []
        
        for _ in range(num):
            arr = [n for n in range(num)]
            random.shuffle(arr)
            menPref.append(arr)
            womenPref.append(arr.copy())
        random.shuffle(menPref)
        random.shuffle(womenPref)
    

    result = basicGaleShapley(menPref, womenPref)
    print(result)


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
    parser.add_argument('--worstcase', '-w', default=False, help='if use the worst case as input, size = 4')
    args = parser.parse_args()
    main(args)
import random
import string
import winsound
from typing import List, Any

##Voice for Recruit Rush

isNotOver = True
filename = 'Recruits1.wav'
roundsRotateUnranked = 3
roundsRotateQuick = 2
isQuick = input("Write 1 if it`s Quick game")     # Is it a quick game (y/n)?
amountPlayers = int(input("How many players?"))
percentageRecruit = int(3)

nameSide = ["attacker", "next attacker", "defender", "next defender"]
DEFENDER_OPERATORS = ["Recruit", "Smoke", "Mute", "Castle", "Pulse", "Doc", "Rook", "Kapkan", "Tachankin",
                "Jäger", "Bandit", "Frost", "Valkyrie", "Caveira", "Echo", "Mira", "Lesion", "Ela",
                "Vigil", "Maestro", "Alibi", "Clash", "Kaid", "Mozzie", "Warden", "Goyo", "Wamai",
                "Oryx", "Melusi", "Aruni", "Thunderbird", "Thorn", "Azami", "Solis"]


ATTACKER_OPERATORS = ["Recruit", "Sledge", "Thatcher", "Ash", "Thermite", "Twitch", "Montagne", "Glaz",
                "Fuze", "Blitz", "Iq", "Buck", "Blackbeard", "Capitao", "Hibana", "Jackal", "Ying",
                "Zofia", "Dokkaebi", "Leon", "Finka", "Maverick", "Nomad", "Gridlock", "Nøkk", "Amaru",
                "Kali", "Iana", "Ace", "Zero", "Flores", "Osa", "Sens", "Grim", "Brava"]
ALL_OPERATORS = [DEFENDER_OPERATORS, ATTACKER_OPERATORS]

def choose_n_random_elements_from_list(n, list):
    tmp_list = [x for x in list]
    random.shuffle(tmp_list)
    print('\n'.join(tmp_list[0:n]))


def noOvertimePlay(amountGames, side, k):
    global amountPlayers
    for j in range(0, 2):
        for k in range(0, amountGames):
            randomOperatorsNoSame(amountPlayers, side, 1)
            input("Write for the next round")
        side += 1


def randomOperatorsNoSame(amount, side, i):
    if recruitRush(percentageRecruit):
        while i <= amount:
            print(ATTACKER_OPERATORS[0])
            i += 1
        winsound.PlaySound(filename, winsound.SND_FILENAME)
    else:
        while i <= amount:
            op = random.randint(0, len(ALL_OPERATORS[side % 2]) - 1)
            print(ALL_OPERATORS[side % 2][op])
            ALL_OPERATORS[side % 2].pop(op)
            i += 1


def randomOperatorsSame(amount, side, i):
    if recruitRush(percentageRecruit):
        while i <= amount:
            print(ATTACKER_OPERATORS[0])
            i += 1
        winsound.PlaySound(filename, winsound.SND_FILENAME)
    else:
        operator_list = ALL_OPERATORS[side % 2].copy()
        while i <= amount:
            op = random.randint(0, len(operator_list) - 1)
            print(operator_list[op])
            operator_list.pop(op)
            i += 1


def recruitRush(percentage):
    if ATTACKER_OPERATORS[0] == "Recruit":
        if random.randint(1, 100) <= percentage:
            if 1 == 1: #bool(random.getrandbits(1)):
                print("Recruit rush!")
                return True
        else:
            return False
    else:
        return False


def banPhase():
    is_baning = True
    numb_ban = 0
    while is_baning:
        op_to_ban = string.capwords(input("Write the name of banned {}".format(nameSide[numb_ban])))
        if op_to_ban in ATTACKER_OPERATORS and (numb_ban//2) == 0:
            banAttackers(op_to_ban)
            numb_ban += 1
        elif op_to_ban in DEFENDER_OPERATORS and (numb_ban//2) == 1:
            banDefenders(op_to_ban)
            numb_ban += 1
        elif op_to_ban == "":
            numb_ban += 1
        if numb_ban == 4:
            is_baning = False


def banAttackers(operator):
    ATTACKER_OPERATORS.remove(string.capwords(operator))


def banDefenders(operator):
    DEFENDER_OPERATORS.remove(string.capwords(operator))


def removeRecruit():
    DEFENDER_OPERATORS.remove("Recruit")
    ATTACKER_OPERATORS.remove("Recruit")


def rotationIfNotWin(times):
    global whichTeam
    whichTeam = whichTeam+1
    didWin = input("Did you win y/n")
    for i in range(0, times):
        if didWin != "y":
            whichTeam += 1
            randomOperatorsSame(amountPlayers, whichTeam, 1)
            input("Write for the next round")
        else:
            break


while isNotOver:
    if isQuick == "1":
        whichTeam = int(input("1 for attack, 2 for defence"))
        noOvertimePlay(roundsRotateQuick, whichTeam, 1)
        if int(input("If you won, write 1")) == 1:
            isNotOver = False
        else:
            whichTeam = int(input("1 for attack, 2 for defence"))
            randomOperatorsSame(amountPlayers, whichTeam, 1)
            isNotOver = False
    elif isQuick != 1:
        removeRecruit()
        banPhase()
        whichTeam = int(input("1 for attack, 2 for defence"))
        noOvertimePlay(roundsRotateUnranked, whichTeam, 1)
        rotationIfNotWin(4)
        isNotOver = False
print("GG, wp")
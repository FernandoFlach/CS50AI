from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(

    Implication(And(AKnight, AKnave), AKnight),
    Implication(Not(And(AKnight,AKnave)), AKnave),
    Biconditional(AKnight, Not(AKnave)),

    
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # They can't be both a knight and a knave
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnave, Not(BKnight)),

    Implication(And(AKnave, BKnave), AKnight),
    Implication(Or(AKnight, BKnight), AKnight)

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # They can't be both a knight and a knave
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnave, Not(BKnight)),

    Implication(Or( And( AKnight, BKnight), And(BKnave, AKnave)), AKnight),
    Implication(Or( And( AKnave, BKnight), And(AKnight, BKnave)), BKnight)
    
)


# Puzzle 3
# 1. A says either "I am a knight." or "I am a knave.", but you don't know which.
# 2. B says "A said 'I am a knave'."
# 3. B says "C is a knave."
# 4. C says "A is a knight."

# A said I am a knight: He could be either a knight or a knave

# A said I am a knave: Impossible




knowledge3 = And(
    # They can't be both a knight and a knave
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(CKnave, Not(CKnight)),

    #1.
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    #2.
    Biconditional(BKnight, AKnave),
    Biconditional(BKnave, Not(AKnave)),


    #3.
    Biconditional(BKnight, CKnave),
    Biconditional(BKnave, Not(CKnave)),

    #4.
    Biconditional(CKnight, AKnight),
    Biconditional(CKnave, Not(AKnight)),


)






def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

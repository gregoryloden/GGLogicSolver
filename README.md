GGLogicSolver
=============

Attempting to make a grid-style logic problem solver using MIT's Alloy and python.

Two ways to use!

    from solve import solve
    from LogicLanguage import *

    # populate this
    puzzleObject = Puzzle()

    answer = solve(puzzleObject)

OR

Save the implementation inside `LLImpl.py` and name the `Puzzle` object puzzle, and then `python solve.py` from the command line will solve it.

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/.

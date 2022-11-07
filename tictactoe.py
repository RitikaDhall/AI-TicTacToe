"""
Tic Tac Toe Player
"""

import math
import copy
from random import randint

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    countX = 0
    countO = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1
    if countO < countX:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actionSet = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actionSet.add((i, j))
    if actionSet == set():
        return None
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    newBoard = copy.deepcopy(board)
    i, j = action

    if newBoard[i][j] is not EMPTY:
        raise Exception("Invalid action.")

    newBoard[i][j] = player(board)

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    def check(seq):
        a, b, c = seq
        if a is EMPTY or b is EMPTY or c is EMPTY:
            return None
        if a == b and b == c:
            return a
        return None

    r1 = [board[0][0], board[0][1], board[0][2]]
    r2 = [board[1][0], board[1][1], board[1][2]]
    r3 = [board[2][0], board[2][1], board[2][2]]
    c1 = [board[0][0], board[1][0], board[2][0]]
    c2 = [board[0][1], board[1][1], board[2][1]]
    c3 = [board[0][2], board[1][2], board[2][2]]
    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]

    possibleWin = [r1, r2, r3, c1, c2, c3, d1, d2]

    for option in possibleWin:
        result = check(option)
        if result:
            return result


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board):
        return True
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    if player(board) == X:

        if board == initial_state():
            return (randint(0, 2), randint(0,2))

        optimal_action = maxOfMinValue(board)[0]
        return optimal_action

    if player(board) == O:
        optimal_action = minOfMaxValue(board)[0]
        return optimal_action


def maxOfMinValue(board):
    """
    Returns the maximum of minimum value.
    """
    if terminal(board):
        return (None, utility(board))
    v = -math.inf
    optimal_action = (None, None)
    for action in actions(board):
        action_value = minOfMaxValue(result(board, action))[1]
        if action_value == 1:
            return (action, action_value)
        if action_value > v:
            v = action_value
            optimal_action = action
    return (optimal_action, v)
    

def minOfMaxValue(board):
    """
    Returns the minimum of maximum value.
    """
    if terminal(board):
        return (None, utility(board))
    v = math.inf
    optimal_action = (None, None)
    for action in actions(board):
        action_value = maxOfMinValue(result(board, action))[1]
        if action_value == -1:
            return (action, action_value)
        if action_value < v:
            v = action_value
            optimal_action = action
    return (optimal_action, v)
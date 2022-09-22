import util
import planner
from state import State


def validate(problem, solution):
    '''
    Return true if `solution` is a valid plan for `problem`.
    Otherwise, return false.

    OBSERVATION: you should check action applicability,
    next-state generation and if final state is indeed a goal state.
    It should give you some indication of the correctness of your planner,
    mainly for debugging purposes.
    '''
    ' YOUR CODE HERE '
    #util.raiseNotDefined()

    if solution is None:
        return True

    else:
        current_state = State().union(problem.init)

        for action in solution:
            if (not applicable(current_state, action)):
                return False

            else:
                old_state = current_state
                current_state = successor(current_state, action)
                next_state_check(old_state, current_state, action)

        if (not is_goal(current_state, problem.goal)):
            return False

        else:
            return True


def applicable(state, action):
    applicable = True
    intersect = state.intersect(action.precond)

    for cond in action.precond:
        if cond not in intersect:
            applicable = False
            break

    return applicable


def next_state_check(oldstate, newstate, action):
    common = oldstate.intersect(newstate)
    inter = newstate.intersect(action.pos_effect)

    for effect in action.pos_effect:
        if effect not in inter:
            return False
        if effect in common:
            return False

    inter = newstate.intersect(action.neg_effect)

    for effect in action.neg_effect:
        if effect in inter:
            return False
        if effect in common:
            return False


def successor(state, action):
    return State(action.pos_effect).union(State(state).difference(action.neg_effect))


def is_goal(state, goal):
    return State(state).intersect(goal) == State(goal)

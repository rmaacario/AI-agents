import argparse
import time

from parser     import Parser
from planner    import ProgressionPlanning
from heuristics import h_naive, h_add, h_max, h_ff
from validator  import validate


def parse():
    usage = 'python3 pystrips.py {show, ground, solve} <DOMAIN> <INSTANCE> [OPTIONS]'
    description = 'PyStrips is a classical planner based on HSP for PDDL/STRIPS language.'
    help_commands = '''
    show PDDL files, ground all actions or solve domain/problem instance.
    '''.strip()
    parser = argparse.ArgumentParser(usage=usage, description=description)
    parser.add_argument('command', choices=['show', 'ground', 'solve'], help=help_commands)
    parser.add_argument('domain',  type=str, help='path to PDDL domain file')
    parser.add_argument('problem', type=str, help='path to PDDL problem file')
    parser.add_argument('-ph', '--heuristics', choices=['naive', 'add', 'max', 'ff'],
                        default='naive', type=str, help='heuristics (default=h_add)')
    parser.add_argument('-w', '--weight', type=float, default=1.0, help='heuristics weight (default=1.0)')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse()

    uptime = {}

    start_time = time.time()
    domain  = Parser.parse(args.domain)
    problem = Parser.parse(args.problem)
    end_time = time.time()
    uptime['parsing'] = end_time - start_time

    if args.command == 'show':
        print(domain)
        print(problem)
    elif args.command == 'ground':
        print(domain)
        print(problem)
        all_actions = problem.ground_all_actions(domain)
        for action in all_actions:
            print(action)
    elif args.command == 'solve':
        start_time = time.time()
        planner = ProgressionPlanning(domain, problem)
        end_time = time.time()
        uptime['grounding'] = end_time - start_time

        h = h_naive
        if args.heuristics == 'add':
            h = h_add
        elif args.heuristics == 'max':
            h = h_max
        elif args.heuristics == 'ff':
            h = h_ff

        start_time = time.time()
        solution, explored, visited = planner.solve(args.weight, h)
        if not validate(problem, solution):
            print("ERROR: Invalid plan.")
            print('\n'.join(map(repr, solution)))
            exit(1)
        end_time = time.time()
        uptime['planning'] = end_time - start_time

        # print statistics
        print('>> solution length =', len(solution))
        print('>> time: parsing = {0:.4f}, grounding = {1:.4f}, planning = {2:.4f}'.format(
            uptime['parsing'], uptime['grounding'], uptime['planning']))
        print('>> nodes explored =', explored)
        print('>> nodes visited  =', visited)
        print('>> ramification factor = {0:.4f}'.format(visited / explored))
        print()

        if args.verbose:
            print('>> Initial state:')
            print(', '.join(sorted(problem.init)))
            print()
            print('>> Solution:')
            print('\n'.join(map(repr, solution)))
            print()
            print('>> Goal state:')
            print(', '.join(sorted(problem.goal)))

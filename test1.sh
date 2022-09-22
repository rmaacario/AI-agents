echo
echo '>> Solving pddl/robot/boxes/problem01.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem01.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/robot/boxes/problem02.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem02.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/robot/boxes/problem03.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem03.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/robot/boxes/problem04.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem04.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/robot/boxes/problem05.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem05.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/robot/boxes/problem06.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem06.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/robot/boxes/problem07.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem07.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/robot/boxes/problem08.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem08.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/robot/boxes/problem09.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem09.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/robot/boxes/problem10.pddl ...'
echo
python3 pystrips.py solve pddl/robot/domain.pddl pddl/robot/boxes/problem10.pddl --heuristics $1 --weight $2

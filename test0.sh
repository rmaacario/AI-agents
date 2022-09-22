echo
echo '>> Solving blocksworld/problems/probBLOCKS-04-0.pddl ...'
echo
python3 pystrips.py solve pddl/blocksworld/domain.pddl pddl/blocksworld/problems/probBLOCKS-04-0.pddl --heuristics $1 --weight $2

echo
echo '>> Solving blocksworld/problems/probBLOCKS-04-2.pddl ...'
echo
python3 pystrips.py solve pddl/blocksworld/domain.pddl pddl/blocksworld/problems/probBLOCKS-04-2.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/gitplanner/problems/p01.pddl ...'
echo
python3 pystrips.py solve pddl/gitplanner/domain.pddl pddl/gitplanner/problems/p01.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/gitplanner/problems/p02.pddl ...'
echo
python3 pystrips.py solve pddl/gitplanner/domain.pddl pddl/gitplanner/problems/p02.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/gitplanner/problems/p03.pddl ...'
echo
python3 pystrips.py solve pddl/gitplanner/domain.pddl pddl/gitplanner/problems/p03.pddl --heuristics $1 --weight $2

echo
echo '>> Solving pddl/gitplanner/problems/p04.pddl ...'
echo
python3 pystrips.py solve pddl/gitplanner/domain.pddl pddl/gitplanner/problems/p04.pddl --heuristics $1 --weight $2

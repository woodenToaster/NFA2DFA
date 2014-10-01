all: NFA2DFA.py
	python3 NFA2DFA.py < input.txt

test: TestNFA2DFA.py
	python3 TestNFA2DFA.py -v


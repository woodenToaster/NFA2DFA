import unittest
import re
import NFA2DFA

class TestRegex(unittest.TestCase):

	f = None

	def setUp(self):
		self.f = open('input.txt', 'r')

	def test_file_read(self):
		#Ensure we get the expected variables from the sample file input.txt
		first_line = self.f.readline()
		self.assertEqual(first_line, "Initial State: {1}\n")

	def test_regex_line1(self):
		#Regex should match '1'
		first_line = self.f.readline()
		regex = re.compile(r"\{(\d)\}")
		start_state = regex.search(first_line).group(1)
		self.assertEqual(start_state, '1')

	def test_regex_line2(self):
		#Regex should return a list of all final states
		second_line = "Final States: {11, 10, 9, 8}\n"
		regex = re.compile(r"\d+")
		final_states = regex.findall(second_line)
		self.assertEqual(final_states, ["11", "10", "9", "8"])

	def test_create_NFA_from_file(self):
		#Ensures NFA is initialized correctly
		nfa = NFA2DFA.NFA()
		nfa.create_NFA_from_file()
		self.assertEqual(nfa.start_state, "1")
		self.assertEqual(nfa.final_states, ["11"])
		self.assertEqual(nfa.total_states, "11")
		self.assertEqual(nfa.input_alphabet, ['a', 'b', 'E'])
		self.assertEqual(nfa.transition_table[1], {'a': '{}', 'b': '{}', 'E': '{2,5}'})
		self.assertEqual(nfa.transition_table[8], {'a': '{}', 'b': '{}', 'E': '{9,11}'})
		self.assertEqual(nfa.transition_table[9], {'a': '{10}', 'b': '{}', 'E': '{}'})

	def tearDown(self):
		self.f.close()

if __name__ == '__main__':
	unittest.main()
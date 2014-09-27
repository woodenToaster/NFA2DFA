import re
import sys

class NFA:
	"""Holds all state for a nondeterministic finite automaton"""
 
	def create_NFA_from_file(self):
		#Match one or more digits
		f = open('input.txt', 'r')
		regex1 = re.compile(r"\d+")
		self.start_state = regex1.search(f.readline()).group()
		#List of final states as strings
		self.final_states = regex1.findall(f.readline())
		self.total_states = regex1.search(f.readline()).group()
		#Find all lowercase letters (input alphabet). 
		regex2 = re.compile(r"\s([a-z])")
		self.input_alphabet = regex2.findall(f.readline())
		f.close()

nfa = NFA()
nfa.create_NFA_from_file()

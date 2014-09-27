# Chris Hogan
# EECS 665
# Project 1
# 10/3/2014

import re
import sys

class NFA:
	"""Holds all state for a nondeterministic finite automaton"""
 	
 	#Dictionary to hold the transitions for each state
	transition_table = {}

	def create_NFA_from_file(self):
		""" Creates the initial NFA from a file.  The file should be called input.txt
			and be located in the same directory as this script. """

		#Match one or more digits
		f = open('input.txt', 'r')
		regex1 = re.compile(r"\d+")
		self.start_state = regex1.search(f.readline()).group()

		#List of final states as strings
		self.final_states = regex1.findall(f.readline())
		self.total_states = regex1.search(f.readline()).group()

		#Find all lowercase letters (input alphabet). 
		regex2 = re.compile(r"\s([a-z])")

		#List of all alphabet symbols as strings.
		self.input_alphabet = regex2.findall(f.readline())
		#Add null transition symbol
		self.input_alphabet.append('E')

		#Initialize the transition table
		states = int(self.total_states)
		for i in range(1, states + 1):
			self.transition_table[i] = {}

		regex3 = re.compile(r"(\{\d+(,\d+)*\})|(\{\})")

		#Add all transitions
		for state in self.transition_table:
			line = f.readline()
			transitions = regex3.findall(line)
			for inputs in range(len(self.input_alphabet) - 1):
				for t in transitions[inputs]:
					if t:
						self.transition_table[state][self.input_alphabet[inputs]] = t
			#Handle null transitions
			for t in transitions[len(self.input_alphabet) - 1]:
				if re.match(r"\{", t):
					self.transition_table[state]['E'] = t

		f.close()

	def print_automaton(self):
		""" Prints a nicely formatted version of the automaton to a file called output.txt. """

		print("Initial State: {%s}" % (self.start_state))
		print("Final States: {%s}" % (','.join(self.final_states)))
		print("Total States: %s" % (self.total_states))
		print("State", end='')
		for symbol in self.input_alphabet:
			print("\t%s" % symbol, end='')
		print('')
		for state in range(1, int(self.total_states) + 1):
			print("%s" % state, end='')
			for symbol in self.input_alphabet:
				print("\t%s" % self.transition_table[state][symbol], end='')
			print('')


nfa = NFA()
nfa.create_NFA_from_file()
nfa.print_automaton()



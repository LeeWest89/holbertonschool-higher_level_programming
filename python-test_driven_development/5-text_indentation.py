#!/usr/bin/python3
"""Function that prints 2 new lines after . ? :"""


def text_indentation(text):
	"""Prints text and 2 new lines after . ? :"""
	i = ""
	if type(text) is not str:
		raise TypeError("text must be a string")
	for char in text:
		i += char
		if char in ['.', '?', ':']:
			i += "\n\n"
	print(i)

'''
 # @ Author: André Freire Ferreira
 # @ Create Time: 23-04-2023
 # @ Last Update: 23-04-2023
 # @ Links: 
			anfreire.me
			github.com/anfreire
			linkedin.com/in/anfreire
 '''

#----------------------------------------------#
# Modules

import os
import sys
import time
from pathlib import Path

#----------------------------------------------#
# Constants

YES_NO = {
	"yes": 'y',
	"no": 'n'
}
Color = {
    'reset'		: '\033[0m',
    'red'		: '\033[31m',
    'green'		: '\033[32m',
    'yellow'	: '\033[33m',
    'blue'		: '\033[34m',
    'magenta'	: '\033[35m',
    'cyan'		: '\033[36m',
    'white'		: '\033[37m',
    'black'		: '\033[38m'
}
Bold_Color = {
    'reset'		: '\033[0m',
    'red'		: '\033[1;31m',
    'green'		: '\033[1;32m',
    'yellow'	: '\033[1;33m',
    'blue'		: '\033[1;34m',
    'magenta'	: '\033[1;35m',
    'cyan'		: '\033[1;36m',
    'white'		: '\033[1;37m',
    'black'		: '\033[1;38m'
}
Background = {
    'reset'		: '\033[0m',
    'red'		: '\033[41m',
    'green'		: '\033[42m',
    'yellow'	: '\033[43m',
    'blue'		: '\033[44m',
    'magenta'	: '\033[45m',
    'cyan'		: '\033[46m',
    'white'		: '\033[47m',
    'black'		: '\033[48m'
}


#----------------------------------------------#
# Exceptions

class ColorNotFount(Exception):
	'''Exception raised when the color is not found.

	### Arguments
	-	Exception : (Exception)
		The base class for all exceptions.
	'''
	def __init__(self, color: str):
		self.color = color
		self.message = str_color('Color ', 'red') + str_color(color, 'white') + str_color(' not found.\n', 'red') + str_color('Available colors:\n', 'white') + list(Color.keys()).replace('[', '').replace(']', '').replace(',', '\n')
		super().__init__(self.message)

class BackgroundNotFount(Exception):
	'''Exception raised when the background is not found.

	### Arguments
	-	Exception : (Exception)
		The base class for all exceptions.
	'''
	def __init__(self, background: str):
		self.background = background
		self.message = str_color('Background ', 'red') + str_color(background, 'white') + str_color(' not found.\n', 'red') + str_color('Available backgrounds:\n', 'white') + list(Background.keys()).replace('[', '').replace(']', '').replace(',', '\n')
		super().__init__(self.message)

class CommandCannotBeEmpty(Exception):
	'''Exception raised when the command is empty or None.

	### Arguments
	-	Exception : (Exception)
		The base class for all exceptions.
	'''
	def __init__(self):
		self.message = str_color('Command cannot be empty or None.', 'red')
		super().__init__(self.message)



#----------------------------------------------#
# Functions			 		  		  Commands #

def extract_output(command: str, STDOUT: bool = True, STDERR: bool = True) -> str:
	'''Executes a command and returns its output.
	
	It does not print the output.
	
	### Arguments
	-	command : (str)
		The command to be executed.
	-	STDOUT : (bool, optional)
		Specifies if the standard output should be returned. Defaults to True.
	-	STDERR : (bool, optional)
		Specifies if the standard error should be returned. Defaults to True.

	### Exceptions
	-	CommandCannotBeEmpty
		If the command is empty or None.

	### Returns
	-	str
		The output of the command.
	'''
	if str == '' or command == None:
		raise CommandCannotBeEmpty()
	if STDOUT and STDERR:
		output = os.popen(command).read()
	else:
		with open(os.devnull, 'w') as devnull:
			if STDOUT:
				output = os.popen(command + ' 2> /dev/null').read()
			elif STDERR:
				output = os.popen(command + ' 2>&1').read()
			else:
				output = os.popen(command + ' > /dev/null 2>&1').read()
	return output



def execute_command(command: str, STDOUT: bool = True, STDERR: bool = True) -> None:
	'''Executes a command.

	### Arguments
	-	command : (str)
		The command to be executed.
	-	STDOUT : (bool, optional)
		Specifies if the standard output should be printed. Defaults to True.
	-	STDERR : (bool, optional)
		Specifies if the standard error should be printed. Defaults to True.

	### Exceptions
	-	Exception
		If the command is empty or None.
	'''
	if str == '' or command == None:
		raise CommandCannotBeEmpty()
	if STDOUT and STDERR:
		output = os.system(command)
	else:
		with open(os.devnull, 'w') as devnull:
			if STDOUT:
				output = os.system(command + ' > /dev/null')
			elif STDERR:
				output = os.system(command + ' 2>&1')
			else:
				output = os.system(command + ' > /dev/null 2>&1')
	if output != 0:
		print(str_color('Error executing command: ', 'red') + str_color(command, 'white'))




#----------------------------------------------#
# Functions			 		  		    Output #


def type_writting(text: str, delay: float = 0.05) -> None:
	'''Prints a text as if it was being typed.

	### Arguments
	-	text : (str)
		The text to be printed.
	-	delay : (float, optional)
		The delay between each character. Defaults to 0.05.
	'''
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(delay)

def str_padding(text: str, padding: 10) -> str:
	'''Pads a text.

	### Arguments
	-	text : (str)
		The text to be padded.
	-	padding : (int)
		The padding of the text.

	### Returns
	-	str
		The padded text.
	'''
	return text[:padding].center(padding)

def str_color(text: str, color: str, bold: bool = False) -> str:
	'''Adds a color to a text.

	### Arguments
	-	text : (str)
		The text to be styled.
	-	color : (str)
		The color of the text.
	-	bold : (bool, optional)
		Specifies if the text should be bold. Defaults to False.

	### Exceptions
	-	ColorNotFount
		If the color is not found.

	### Returns
	-	str
		The text with a color.
	'''
	if bold:
		color = [x for x in Bold_Color.keys() if x.find(color.lower()) != -1]
	else:
		color = [x for x in Color.keys() if x.find(color.lower()) != -1]
	if len(color) == 0:
		raise ColorNotFount(color)
	if bold:
		return Bold_Color[color[0]] + text + Bold_Color['reset']
	else:
		return Color[color[0]] + text + Color['reset']
	


def str_background(text: str, background: str) -> str:
	'''Adds a background to a text.

	### Arguments
	-	text : (str)
		The text to be styled.
	-	background : (str)
		The background of the text.

	### Returns
	-	str
		The text with a background.
	'''
	background = [x for x in Background.keys() if x.find(background.lower()) != -1]
	if len(background) == 0:
		raise BackgroundNotFount(background)
	return Background[background[0]] + text + Background['reset']




#----------------------------------------------#
# Functions			 		  		     Input #


def prompt_user(prompt: str, options: dict = YES_NO) -> str:
	'''Prompts the user for an input.

	### Arguments
	-	prompt : (str)
		The prompt to be displayed.
	-	options : (dict, optional)
		The options to be displayed. Defaults to YES_NO (yes/no).

	### Returns
	-	str
		The user's input (dict key)
	'''
	options_keys = list(options.keys())
	options_values = list(options.values())
	options_str = '['
	for i in range(len(options_keys)):
		options_str += options_values[i]
		if i != len(options_keys) - 1:
			options_str += '/'
	options_str += ']'
	while True:
		print(prompt)
		for i in range(len(options_keys)):
			print(f'[' + options_values[i] + '] ' + options_keys[i])
		response = input()
		if response in options_values:
			return response
		else:
			print(str_color('Invalid option.', 'red'))





#----------------------------------------------#
# Functions			 		     File Managing #


def check_file_exists(path: str) -> bool:
	'''Checks if a file exists.

	### Arguments
	-	path : (str)
		The path of the file.

	### Returns
	-	bool
		True if it exists, False otherwise.
	'''
	return Path(path).is_file()


def check_dir_exists(path: str) -> bool:
	'''Checks if a directory exists.

	### Arguments
	-	path : (str)
		The path of the directory.

	### Returns
	-	bool
		True if it exists, False otherwise.
	'''
	return Path(path).is_dir()
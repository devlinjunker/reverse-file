#! /usr/bin/python

def main():
	# counters
	lines = 0
	words = 0
	chars = 0
	
	# output 
	char = ''
	eol = ''
	buff1 = []
	buff2 = []
	
	# files
	input = open('../../../School/CS 372/Lab 2/alice.txt', 'r')
	output = open('morel.txt', 'w')
	
	# while characters to read
	while(len(input.read(1)) != 0):
		# reset location
		input.seek(-1, 1)
		
		# get character
		char = input.read(1)
		
		# increment character count (includes all EOL and EOF characters)
		chars += 1
			
		# if char is space and previous character was not space or EOL character
		if(chars > 0 and char == " " and buff1[-1] != " " and buff1[-1] != "\r" and buff1[-1]!= "\n"):
			# increment word count
			words += 1
		
		# if char is EOL character
		if(char == "\r" or char == "\n"):
			
			# if end of line character not set
			if(eol == ''):
				# set as first EOL character found
				eol = char
			
			if(char == eol):
				# if previous character was not eol or space
				if(chars > 0 and buff1[-1] != eol and buff1[-1] != " "):
					# increment word and line count
					words += 1
					lines += 1
				else:
					# only increment line count
					lines += 1
				
				# only append designated eol character to buffer
				buff1.append(char)
	
		# else if not EOL character
		else:
			# push on to buffer
			buff1.append(char)
	
	# Increment line count for EOF Character
	lines += 1
	
	# while characters in buffer 1
	while(len(buff1) > 0):
		# pop from buffer 1
		char = buff1.pop()
		
		# if character is not a word separator (space or EOL character)
		if(char != " " and char != eol):
			buff2.append(char)
		# once seperator found
		else:
			# add separator to beginning of buffer 2 (last to be popped)
			buff2.insert(0, char)
			while(len(buff2) > 0):
				char = buff2.pop()
				# write to output file
				output.write(char)	
			
		
	# print results
	print """output in morel.txt
	 lines: {0}
	 words: {1}
	 characters (including spaces, EOL and EOF characters): {2}
	 """.format(lines, words, chars)
	
	# close files
	input.close()
	output.close()
	
if __name__ == "__main__":
	main()
# # Python3 Program for Bad Character Heuristic
# # of Boyer Moore String Matching Algorithm

# NO_OF_CHARS = 256


# def badCharHeuristic(string, size):
# 	'''
# 	The preprocessing function for
# 	Boyer Moore's bad character heuristic
# 	'''

# 	# Initialize all occurrence as -1
# 	badChar = [-1]*NO_OF_CHARS

# 	# Fill the actual value of last occurrence
# 	for i in range(size):
# 		badChar[ord(string[i])] = i

# 	# return initialized list
# 	return badChar


# def search(txt, pat):
# 	'''
# 	A pattern searching function that uses Bad Character
# 	Heuristic of Boyer Moore Algorithm
# 	'''
# 	m = len(pat)
# 	n = len(txt)

# 	# create the bad character list by calling
# 	# the preprocessing function badCharHeuristic()
# 	# for given pattern
# 	badChar = badCharHeuristic(pat, m)

# 	# s is shift of the pattern with respect to text
# 	s = 0
# 	while(s <= n-m):
# 		j = m-1

# 		# Keep reducing index j of pattern while
# 		# characters of pattern and text are matching
# 		# at this shift s
# 		while j >= 0 and pat[j] == txt[s+j]:
# 			j -= 1

# 		# If the pattern is present at current shift,
# 		# then index j will become -1 after the above loop
# 		if j < 0:
# 			print("Pattern occur at shift = {}".format(s))

# 			'''
# 				Shift the pattern so that the next character in text
# 					aligns with the last occurrence of it in pattern.
# 				The condition s+m < n is necessary for the case when
# 				pattern occurs at the end of text
# 			'''
# 			s += (m-badChar[ord(txt[s+m])] if s+m < n else 1)
# 		else:
# 			'''
# 			Shift the pattern so that the bad character in text
# 			aligns with the last occurrence of it in pattern. The
# 			max function is used to make sure that we get a positive
# 			shift. We may get a negative shift if the last occurrence
# 			of bad character in pattern is on the right side of the
# 			current character.
# 			'''
# 			s += max(1, j-badChar[ord(txt[s+j])])


# # Driver program to test above function
# def main():
# 	txt = "ABAAABCD"
# 	pat = "ABC"
# 	search(txt, pat)


# if __name__ == '__main__':
# 	main()

# # This code is contributed by Atul Kumar
# # (www.facebook.com/atul.kr.007)

text = "This is a string"
pat = "string"
def boy(text = text, pat = pat):
    t_len = len(text) -1
    p_len = len(pat) -1
    j = 0 # correct character count
    i = 0
    while i <p_len - t_len:
        if pat[-1] == text[i+p_len]:
            for x in range(p_len):
                if pat[-1-x] == text[i+p_len-x]:
                    j+=1
                else:
                    break
                
            pass
    pass
text = 'AAEAA'
pt = 'BBE'
print(pt[-1] == text[len(pt)-1])
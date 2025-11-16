s = "Coding Factory"

s1 = s[7] # F
# String slicing
s2 = s[:]
s3 = s[:6]
s4 = s[7:]
s5 = s[:-1]

# Reverse string
s6 = s[-1:-len(s)-1:-1] # start, stop, step
s7 = s[::-1]            # alternative - pythonian

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
#slicing create a substring by extracting elements from an another string

#indexing[] or slice()

# Syntax: string[start:stop:step]


name = "David Dereje Mesganaw"
first_name = name[1:3] #start from index 1 and stop at index 3 but not include index 3
last_name = name[5:-7]
funky_name = name[::2] #start from index 0 and stop at the end of the string but not include the last index and step by 2
#funky_name = name[::3] #start from index 0 and stop at the end of the string but not include the last index and step by 3

reverse_name = name[::-1] #start from index 0 and stop at the end of the string but not include the last index and step by -1

print(first_name)
print(last_name)
print(funky_name)
print(reverse_name)


webstie = "https://www.google.com"

slice1 = webstie[8:] #start from index 8 and stop at the end of the string but not include the last index
slice2 = webstie[7:-4] #start from index 8 and stop at index -4 but not include index -4
slice3 = webstie[8:-4:2] #start from index 8 and stop at index -4 but not include index -4 and step by 2
print(slice1)
print(slice2)
print(slice3)



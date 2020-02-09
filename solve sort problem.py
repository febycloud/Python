#Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)
#
#Inputs
#- Original list of strings
#- List of strings to be added
#- List of strings to be removed
#
#Return
#- List shall only contain unique values
#- List shall be ordered as follows
#--- Most character count to least character count
#--- In the event of a tie, reverse alphabetical
#
#For example:
#
#Original List = ['one', 'two', 'three',]
#Add List = ['one', 'two', 'five', 'six]
#Delete List = ['two', 'five']
#Result List = ['three', 'six', 'one'] 



original=['one','two','three']
add=['one','two','five','six']
print(original)
print(add)
lst=original+add
delete=['two','five']
for i in delete:
	for j in lst:
		if(i==j):
			lst.remove(i)	
lst=list(set(lst))
print(lst)
res=sorted(lst,key=lambda x:len(x),reverse=True)
print(res)
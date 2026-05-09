# not editable, can't add or remove member ,unique , not in order ,immutable
s1 = frozenset {1,2,3,4}
print(s1)

# copy()  of frozensets : if delet s1 , s2 has not been removed
s2 = s1.copy()
print(s2)

# union() of frozensets === | or operator 
s1 = frozenset {1,2,3,4}
s2 ={1,2,3,5,7,8}
s3 = s1 .union(s2)
print(s3)

# intersection() of frozensets === & and operator 
s1 = frozenset {1,2,3,4}
s2 ={1,2,3,5,7,8}
s3 = s1 .union(s2)
print(s3)



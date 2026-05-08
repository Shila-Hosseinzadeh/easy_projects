# Join Sets
# union()
set1 = {1,2,3,4,5}
set2 = {"a","b","c",1,3}
set11 = {1,2,3,4,5,33,"G","d"}
set12 = {"a","b","c",1,3,"E",22,45}
set3 = set1.union(set2,set11,set12)
print(f"set1.union(set2,set11,set12,...) ---> set3 ={set3}")

# |
set4 = set1 | set1 |set11 |set12
print(f"set1 | set2 |se11 |set12 ---> set4 = {set4}")

#

set1={1,6}
fs1=frozenset(set1)
print(fs1)

set2={1,2,3,4,5,6}
fs2=frozenset(set2)
print(fs2)

f1=fs1.isdisjoint(fs2)
print(f1)

f2=fs1.issubset(fs2)
print(f2)

f3=fs2.issuperset(fs1)
print(f3)

f4=fs1.union(fs2)
print(f4)

f5=fs1.intersection(fs2)
print(f5)

f6=fs1.difference(fs2)
print(f6)

f7=fs1.symmetric_difference(fs2)
print(f7)


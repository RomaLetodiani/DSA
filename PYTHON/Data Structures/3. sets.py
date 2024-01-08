# https://www.w3schools.com/python/python_sets_methods.asp

# O(1)
# add() - Adds an element to the set

# O(1)
# in

# O(1)
# len()

# O(N)
# copy() - Returns a copy of the set
# O(N)
# clear() - Removes all the elements from the set

# O(1)
# discard() - Remove the specified item (does nothing if the value is not found)
# O(1)
# remove() - Removes the specified element (raises an exception if the value is not found)

# O(1)
# pop() - Removes and returns a random item from the set

# O(S1 + S2)
# union() - Return a set containing the union of sets
# O(S2)
# update() - Update the set with the union of this set and others

# O(S1)
# difference() - Returns a set containing the difference between two sets
# O(S1)
# difference_update() - Removes the items in this set that are also included in another, specified set

# O(min(S1, S2))
# intersection() - Returns a set, that is the intersection of two other sets
# O(S1)
# intersection_update() - Removes the items in this set that are not present in other, specified set

# O(S1 + S2)
# symmetric_difference() - Returns a set with the symmetric differences of two sets
# O(S2)
# symmetric_difference_update() - inserts the symmetric differences from this set and another

# O(min(S1, S2))
# isdisjoint() - Returns whether two sets have a intersection or not
# O(S1)
# issubset() - Returns whether another set contains this set or not
# O(S2)
# issuperset() - Returns whether this set contains another set or not

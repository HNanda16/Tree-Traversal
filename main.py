import tree_traversals

#1. Create your example tree data structure here
tree = [("CEO",[1,2,3]),("CTO", [4, 5, 6]), ("CFO", [7]), ("CMO", []), ("CIO", []), ("CDO", [8, 9]), ("COO", []), ("CBO", []), ("CPO", []), ("CSO", [])]


#2. Complete the functions in tree_traversals.py
#3. Invoke each function with your example tree, outputting the results in a nice way
print(tree_traversals.breadth_first_traversal(tree))
print(tree_traversals.pre_order_traversal(tree))
print(tree_traversals.in_order_traversal(tree))
print(tree_traversals.post_order_traversal(tree))
#4. Extension: Add automated tests to test your tree_traversals.py functions with a range of cases (erroneous, boundary, valid etc.)

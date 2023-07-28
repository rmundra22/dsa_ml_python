# Backtracking is a form of recursion. But it involves choosing only option 
# out of any possibilities. We begin by choosing an option and backtrack 
# from it, if we reach a state where we conclude that this specific option 
# does not give the required solution. We repeat these steps by going across 
# each available option until we get the desired solution.

# Below is an example of finding all possible order of arrangements of a 
# given set of letters. When we choose a pair we apply backtracking to verify 
# if that exact pair has already been created or not. If not already created, 
# the pair is added to the answer list else it is ignored.

def find_possible_arrangements(arrangement_length, list_of_elements):
   if arrangement_length == 1:
      return list_of_elements
   else:
      return [ 
         y + x
         for y in find_possible_arrangements(1, list_of_elements)
         for x in find_possible_arrangements(arrangement_length - 1, list_of_elements)
      ]

if __name__ == "__main__":
    print(find_possible_arrangements(1, ["a","b","c"]))
    print(find_possible_arrangements(2, ["a","b","c"]))
    print(find_possible_arrangements(3, ["a","b","c"]))

def isSubsetSum(set, n, sum):
     
    # The value of subset[i][j] will be 
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset =([[(False, []) for i in range(sum + 1)] 
            for i in range(n + 1)])
     
    # If sum is 0, then answer is true 
    for i in range(n + 1):
        subset[i][0] = (True, [])
         
    # If sum is not 0 and set is empty, 
    # then answer is false 
    for i in range(1, sum + 1):
         subset[0][i]= (False, [])
             
    # Fill the subset table in botton up manner
    for i in range(1, n + 1):
        print(i)
        for j in range(1, sum + 1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                if subset[i-1][j][0]:
                  subset[i][j] = subset[i-1][j]
                elif subset[i - 1][j-set[i-1]][0]:
                  subset[i][j] = (True, subset[i-1][j-set[i-1]][1] + [set[i-1]])
                else:
                  subset[i][j] = (False, [])
     
    # uncomment this code to print table 
    """
    for i in range(n + 1):
     for j in range(sum + 1):
      print (subset[i][j], end =" ")
     print()
     """
    return subset[n][sum]

v = [int(round(1000 * float(edge[1]), 0)) for edge in read_edges("inputs/medium-7.in")]
print(v)
sum = 389916
print(isSubsetSum(v, len(v), sum))

import numpy as np
def get_input(dim):
    n = range(dim) # --> To call the range only once intead of "dim" times.
    coeffs = [] # --> To store the matrix in, later will be turned into a NumPy ndarray.
    for i in n:
        coeffs.append(input(f"Insert here the #{i+1} equation, space separated, including the R.H.S constant\n").split()) # Get's the system as input.
    return np.array(coeffs, dtype = "float64") # --> Turns the list into a NumPy ndarray and returns it.

def singularity(matrix, deg): # --> Checks the singularity of the matrix
    mat = matrix[:, 0:deg] # --> To ignore the constants column
    det = np.linalg.det(mat) # --> Calculates the determinant of the matrix
    if det == 0:
        return 0
    else:
        return 1


def pivoting(matrix, deg): # --> turns the matrix into its R.E.F.
    num_of_eq = range(deg)
    for i in num_of_eq:
        n = 1 # --> Used in calulating the position of the row that will be operated on
        pivot = matrix[i, i]
        matrix[i] = matrix[i]/pivot # --> Turns the pivot into 1, and performs that operation on the entire row.
        
        while (i+n) <= (deg -1): # --> Loops over the following algorithm till the position is equal to the number of rows.
            pos = i + n # --> Position of the row to be operated on.
            x = matrix[pos, i]/pivot # --> get's the value which 
            matrix[pos] = matrix[pos] - (matrix[i]*x) # --> Does matrix operation on the target row to get the values below the pivot equal to 0.
            n += 1
    return matrix

def back_sub(reduced_matrix, deg): # Turns a reduced matrix into its R.R.E.F.
    # The next two lines are there to be able to reverse the order at which the for loop traverses over the matrix.
    order = list(range(deg)) 
    order.reverse()
    
    for i in order:
        n = 1
        while (i-n) >= 0: # --> Loops over the following algorithm till the position is equal to 0.
            pos = i - n
            reduced_matrix[pos] = reduced_matrix[pos] - (reduced_matrix[i]*reduced_matrix[pos, i]) # Turns the value above the pivot to zero, using proper row operations.
            n += 1
    return reduced_matrix


def sys_sol():
    deg = int(input("What's the dimension of the system?\n")) # Gets the degree of the system from the user.
    n = range(deg)
    # The next 2 lines gets the system from the user and checks its singularity.
    sys = get_input(deg)
    non_singular = singularity(sys, deg)
    if non_singular:
        reduced_matrix = pivoting(sys, deg)
        rref = back_sub(reduced_matrix, deg)
    
        sol = [] # --> Saves the solutinos to the system to it, to be able to output it properly.
        for i in n:
            sol.append(rref[i, deg])
        return tuple(sol) # --> Turns the list into a tupe (for space effeciency) and returns it.
    else:
        return None

solution = sys_sol()
if solution is not None:
    print(f"The solution to the system is = {solution}")
elif solution is None:
    print("The system is singular")

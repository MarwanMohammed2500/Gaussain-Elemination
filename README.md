# get_input:
    Gets the system of equations as input from the user
        
    Input:
        Takes one input arguments:
            1- degree of equation (number of variables)
    
    Output:
        Outputs a NumPy ndarray representing the matrix corrosponding to the system of equations


# singularity:
    Checks the singularity of the matrix

    Input:
        Takes two input arguments:
            1- The matrix
            2- Degree of the system

    Output:
        1 if the system is non-singular, 0 if the system is singular


# pivoting:
    Turns a matrix into it's row echelon form (R.E.F.):
        - Get's the row's pivot (left-most non-zero value)
        - Turns all values below the pivot into zeros using proper row operations
    
    Input:
        Takes 2 input arguments:
            - The augmented matrix
            - The degree of the system

    Output:
        Outputs a matrix in the row echelon form


# back_substitution:
    Turns a row reduced matrix into it's reduced row echelon form (R.R.E.F.):
        - Get's the pivot of the row
        - Turns all values above the pivot into zeros using proper row operations
    
    Input:
        - Matrix in R.E.F.
        - Number of rows
    Output:
        - A matrix in it's reduced row echelon form


# sys_sol:
    Uses all the previous functions to output a solution to the system

    Input:
        Takes no input

    Output:
        Outputs a tuple containing the solutions to the system

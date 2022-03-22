import argparse
import pandas as pd
import numpy as np

def step1():
    #Creamos la matriz 10x2 con enteros entre 0 y 10 y la almacenamos en b
    b = np.random.randint(0,11,(10, 2))
    #No se establece como se genera la variable a, asumimos mismo metodo de la variable b pero con 10x1
    a = np.random.randint(0,11,(10,1))
    #Concatenamos en una unica matriz
    c = np.concatenate((a,b),1)
    #Devolevmos las variables solicitadas
    return (a,b,c)
def main():
    """
    Step 1.
    Create an array of 10 rows and 2 columns with random integers between 0 and 10 inclusive.
    Store it in the variable "b". Concatenate variables a and b so that the result is an array of 10 rows and 3 columns.
    Store the result in the variable "c" and display it on the screen.
    """
    a,b,c = step1()
    """
    Step 2.
    Using the np.where function, replace all values of c less than 10 with zeros.
    Using a universal function, it lifts each element of the obtained array.
    Display the results on the screen.
    """

    """
    Step 3.
    Develop a function that reads "Titanic" dataset given in the assessment and count the number of rows.
    Display the results on the screen
    (Optional) Make sure that it could be any format file (zip, pickle,...)
    """
    """
    Step 4
    Using the *reindex* method, keep the "survived", "class", "sex", "age", "fare" and "embark_town" fields from the Titanic dataset.
    Add this into one function that returns the resulting dataframe.
    """
    """
    Step 5
    Install the Seaborn library using the command: pip install seaborn.
    Loads in the tips variable the DataFrame tips provided by the Seaborn library.
    Using only matplotlib functions, create a figure of size (8, 6) and display in it a scatter plot crossing the "tip" 
    and "total_bill" columns of the tips dataset.
    """


if __name__ == "__main__":
    main()

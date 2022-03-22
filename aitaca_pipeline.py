import argparse
import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib.pyplot as plot
class FileReadException(Exception):
    pass

def step1():
    #Creamos la matriz 10x2 con enteros entre 0 y 10 y la almacenamos en b
    b = np.random.randint(0,11,(10, 2))
    #No se establece como se genera la variable a, asumimos mismo metodo de la variable b pero con 10x1
    a = np.random.randint(0,11,(10,1))
    #Concatenamos en una unica matriz
    c = np.concatenate((a,b),1)
    #Devolevmos las variables solicitadas
    return (a,b,c)

def step2(c):
    #Empleo de funcion where, realizamos una copia del array
    c1 = c.copy()
    c1 = np.where(c1<10,0,c1)
    #Empleando funcion universal
    c[c<10] = 0
    #imprimimos en pantalla los dos arrays
    print("Empleando np.where:")
    print(c1)
    print("Empleando funcion universal")
    print(c)

def step3(file):
    #Leemos el archivo
    try:
        titanic = pd.read_csv(file)
        #obtenemos la cuenta de filas
        rowsCount = titanic.shape[0]
        #Imprimimos en pantalla el resultado
        print("Numero de filas:", rowsCount)
        #Devolvemos el DataFrame para el paso 4
        return titanic
    except:
        #En caso de no poder leer el archivo, lanzamos una excepcion FileReadException
        raise FileReadException("Error con el archivo")

def step4(dataSet):
    """
    Establecemos los nuevos indices del dataset.
    Modificamos los introducidos estableciendo la primera letra en mayuscula igual que en el dataset original.
    Asumimos class como Pclass.
    Asumimos que embark_town no existe en el dataset inicial
    """
    newIndex = [ 'Survived',
        'Pclass',
        'Sex',
        'Age',
        'Fare',
        'embark_town'
    ]
    #Generamos el nuevo dataset indicando el eje de las columnas en lugar de filas
    newDataSet = dataSet.reindex(newIndex, axis=1)
    return newDataSet

def step5():
    #Obtenemos dataset
    tips = sea.load_dataset('tips')
    #Extraemos las columnas de interes
    x = tips['tip']
    y = tips['total_bill']
    #Establecemos las dimensiones de la figura
    fg = plot.figure()
    fg.set_figwidth(8)
    fg.set_figheight(6)
    #Establecemos los titulos de los ejes
    plot.xlabel('Tips')
    plot.ylabel('Total bill')
    #Generamos el grafico
    plot.scatter(x,y)
    plot.show()
    #Devolvemos el dataset para cumplir con el requerimiento
    return tips
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
    step2(c)
    """
    Step 3.
    Develop a function that reads "Titanic" dataset given in the assessment and count the number of rows.
    Display the results on the screen
    (Optional) Make sure that it could be any format file (zip, pickle,...)
    """
    titanic = step3("titanic.csv")
    """
    Step 4
    Using the *reindex* method, keep the "survived", "class", "sex", "age", "fare" and "embark_town" fields from the Titanic dataset.
    Add this into one function that returns the resulting dataframe.
    """
    newTitanic = step4(titanic)
    """
    Step 5
    Install the Seaborn library using the command: pip install seaborn.
    Loads in the tips variable the DataFrame tips provided by the Seaborn library.
    Using only matplotlib functions, create a figure of size (8, 6) and display in it a scatter plot crossing the "tip" 
    and "total_bill" columns of the tips dataset.
    """
    tips = step5()


if __name__ == "__main__":
    main()

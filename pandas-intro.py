import os
import pandas as pd

pandaTablesPath = os.path.abspath("./resources/panda-tables")
# print(os.listdir(pandaTablesPath))

print(pandaTablesPath)

allFiles = os.listdir(pandaTablesPath)
fileNames = []
dataFrames = []

for fileName in allFiles:
    print(fileName)

dataFrames.append = pd.read_csv(os.path.join(pandaTablesPath,"\\Dimensions.csv"))
print(dataFrames)



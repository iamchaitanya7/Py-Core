BatchName = ["PPA", "Python", "LB", "Angular", "LSP", "C#"]
BatchFees = [18500, 18700, 19000, 19200, 18200, 21000]

#print(BatchName[0], BatchFees[0]) Access Index wise

for i in range(len(BatchName)):
    print("BatchName", BatchName[i] , "BatchFees", BatchFees[i])

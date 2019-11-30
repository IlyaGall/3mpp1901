from cvxopt.modeling import variable, op  # подключение библиотеки для работы скрипта
import time # подключение библиотеки для работы таймера
start = time.time()  # старт таймера
x = variable(25, 'x')
c= [10, 26, 39,  7,  27, 19, 11, 24,  8,  12, 44, 14, 12,  33, 15, 36, 33, 7,   25, 5, 34, 32, 13,  23, 3] # коэффициенты целевой функции
z=(c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4] + c[5]*x[5] + c[6]*x[6] + c[7]*x[7] + c[8]*x[8] + c[9]*x[9] + c[10]*x[10] + c[11]*x[11] + c[12]*x[12] + c[13]*x[13] + c[14]*x[14] + c[15]*x[15] + c[16]*x[16] + c[17]*x[17] + c[18]*x[18] + c[19]*x[19] + c[20]*x[20] + c[21]*x[21] + c[22]*x[22] + c[23]*x[23] + c[24]*x[24])
mass1 = (x[0] + x[1] + x[2] + x[3] + x[4] <= 40)
mass2 = (x[5] + x[6] + x[7] + x[8] + x[9] <= 15)
mass3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= 7)
mass4 = (x[15] + x[16] + x[17] + x[18] + x[19] <= 10)
mass5 = (x[20] + x[21] + x[22] + x[23] + x[24] <= 8)
mass6 = (x[0] + x[5] + x[10] + x[15] + x[20]  == 10)
mass7 = (x[1] + x[6] + x[11] + x[16] + x[21]  == 8)
mass8 = (x[2] + x[7] + x[12] + x[17] + x[22]  == 40)
mass9 = (x[3] + x[8] + x[13] + x[18] + x[23]  == 20)
mass10 = (x[4] + x[9] + x[14] + x[19] + x[24]  == 1)#ограничение mass1-10
x_non_negative = (x >= 0)    # так как путь не мб отрицательным
problem =op(z,[mass1,mass2,mass3,mass4 ,mass5,mass6, mass7,mass8 ,mass9, mass10,x_non_negative])
problem.solve(solver='glpk')  
print("Результат Xopt:")
for i in x.value:
         print(i)
print("Стоимость доставки:")
print(problem.objective.value()[0])
stop = time.time()
print ("Время :")
print(stop - start)
from pulp import * 
#"подключаем библиотеку" 
#conda install -c conda-forge pulp  прописать в anaconda Prompt от имени администратора
# если не устанавливать, то anaconda пишет error pulp
import time # нужно для расчёта времи выполнения программы
start = time.time() # старт счётчика времени
x0 = pulp.LpVariable("x0", lowBound=0) # думал как через цикл заполнить так и не предумал
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
x5 = pulp.LpVariable("x5", lowBound=0)
x6 = pulp.LpVariable("x6", lowBound=0)
x7 = pulp.LpVariable("x7", lowBound=0)
x8 = pulp.LpVariable("x8", lowBound=0)
x9 = pulp.LpVariable("x9", lowBound=0)
x10 = pulp.LpVariable("x10", lowBound=0)
x11 = pulp.LpVariable("x11", lowBound=0)
x12 = pulp.LpVariable("x12", lowBound=0)
x13 = pulp.LpVariable("x13", lowBound=0)
x14 = pulp.LpVariable("x14", lowBound=0)
x15 = pulp.LpVariable("x15", lowBound=0)
x16 = pulp.LpVariable("x16", lowBound=0)
x17 = pulp.LpVariable("x17", lowBound=0)
x18 = pulp.LpVariable("x18", lowBound=0)
x19 = pulp.LpVariable("x19", lowBound=0)
x20 = pulp.LpVariable("x20", lowBound=0)
x21 = pulp.LpVariable("x21", lowBound=0)
x22 = pulp.LpVariable("x22", lowBound=0)
x23 = pulp.LpVariable("x23", lowBound=0)
x24 = pulp.LpVariable("x24", lowBound=0)
costWay = [10, 26, 39,  7,  27, 
            19, 11, 24,  8,  12, 
            44, 14, 12,  33, 15,
            36, 33, 7,   25, 5,
            34, 32, 13,  23, 3]# стоимость перевозки 1-го комплекта заказа по маршруту аn(склада) до bn (потребителя)
problem = pulp.LpProblem('0',pulp.LpMaximize)
problem += -costWay[0]*x0- costWay[1]*x1-costWay[2]*x2-costWay[3]*x3-costWay[4]*x4- costWay[5]*x5- costWay[6]*x6-costWay[7]*x7-costWay[8]*x8-costWay[9]*x9-costWay[10]*x10- costWay[11]*x11-costWay[12]*x12-costWay[13]*x13-costWay[14]*x14-        costWay[15]*x15- costWay[16]*x16-costWay[17]*x17-costWay[18]*x18-costWay[19]*x19-        costWay[20]*x20- costWay[21]*x21-costWay[22]*x22-costWay[23]*x23-costWay[24]*x24, "Функция цели"
problem +=x0 + x1 +x2 + x3 + x4 <= 40,"1" 
problem +=x5 + x6 +x7 + x8 + x9 <= 15, "2"
problem +=x10 + x11 +x12 + x13 + x14 <= 7, "3"
problem +=x15 + x16 +x17 + x18 + x19 <= 10, "4"
problem +=x20 + x21 +x22 + x23 + x24 <= 8, "5"
problem +=x0+ x5+ x10 + x15 + x20 == 10, "6"
problem +=x1+ x6+ x11 + x16 + x21 == 8, "7"
problem +=x2+ x7+ x12 + x17 + x22 == 40, "8"
problem +=x3+ x8+ x13 + x18 + x23 == 20, "9"
problem +=x4+ x9+ x14 + x19 + x24 == 1, "10"                 
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Стоимость доставки:")
print (abs(value(problem.objective)))
stop = time.time()
print ("Время :")
print(stop - start)


def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

def unionList(lst1, lst2): 
    lst3 = lst1
    for value in lst2:
        if value not in lst1:
            lst3.append(value)
    return lst3

def SumUp(square):

    for kk in range(0, square.__len__()):
        #print(sorted(square[kk][1], key=str))
        square[kk][1] = sorted(square[kk][1], key=str)
        #print(square[kk])

    squareMod = []
    for elem in square[:]:
        if elem not in square:
            continue
        square.remove(elem)
        sumElem = elem[0]
        for elem2 in square[:]:
            if elem[1]==elem2[1]:
                sumElem += elem2[0]            
                square.remove(elem2)
        squareMod.append([sumElem,elem[1]])
        #print(square)
        #print()

    #print(squareMod)
    return squareMod

def squareEq(stringEq):
    data = ''
    data2 = ''
    output = []
    ii=0

    for val in stringEq:
        ii += 1
        if val !='+' and val !='-':
            data += data2
            data += val
            data2 = ''
        else:
            if val =='+':
                output.append(data)
                data = ''
            else:
                data2 = '-'
                output.append(data)
                data = ''
        
        if ii == (stringEq.__len__()):
            output.append(data)

    #print(output)

    data = []

    for elem in output:
        if '*' in elem:
            sq = elem.split('*',1)
            if sq[0].lstrip('-').isdigit():   #isdigit():
                sq1 = int(sq[0])
                data.append([sq1,sq[1].split('*')])
            else:
                #sq[1] = sq[1].split('*')
                #sq = [sq[0], sq[1]]
                data.append([1,sq])
        else:
            sq = elem.split('*',1)
            if sq[0].lstrip('-').isdigit():
                sq1 = int(sq[0])
                if sq.__len__()>1:
                    data.append([sq1,sq[1].split('*')])
                else:
                    data.append([sq1,[]])
            else:
                data.append([1,[sq[0]]])
    #print(data)

    square = []
    for elem in data:
        squareDigit = elem[0] * elem[0]
        squareLiteral = elem[1]
        square.append([squareDigit, squareLiteral])
    #print(square)

    multyRange = data.__len__()-1
    kk = 1
    for elem in data:
        if kk < multyRange + 1:
            for count in range(kk, multyRange+1):
                doubleProd = 2 *elem[0]*data[count][0]
                if intersection(elem[1], data[count][1]):
                    doubleProdLit = unionList(elem[1], data[count][1]) 
                else:
                    doubleProdLit = elem[1]+data[count][1]
                square.append([doubleProd, doubleProdLit])
            kk += 1


    #print(square)
    #print()

    return SumUp(square)


input1 = '2*p2+2*p1*q1+2*q2-8*c2-4*c1+p1+q1-3'
input2 = '2*q1+2*p2*q2+2*p1+2*c2-8*c4-4*c3+p2*q1+p1*q2+c1+1'
input3 = 'q2+p2+c3+2*c4-2'

#print('a')
a = squareEq(input1)
#print('b')
b = squareEq(input2)
#print('c')
c = squareEq(input3)

functionCost = []

functionCost = a + b + c

functionCost = SumUp(functionCost)

print('functionCost')
print(functionCost)
print()

reducer = []
for elem in functionCost:
    if elem[1].__len__() == 3:
        print(elem)

        if 'p1' in elem[1] and 'q1' in elem[1]:
            elem[1].remove('p1')
            elem[1].remove('q1')
            elem[1].append('t1')
            reducer.append([elem[0],elem[1]])
            if elem[0]>0:
                reducer.append([2*elem[0],['p1', 'q1']])
                reducer.append([-4*elem[0],['p1', 't1']])
                reducer.append([-4*elem[0],['q1', 't1']])
                reducer.append([6*elem[0],['t1']])
            else:
                reducer.append([-2*elem[0],['p1', 'q1']])
                reducer.append([4*elem[0],['p1', 't1']])
                reducer.append([4*elem[0],['q1', 't1']])
                reducer.append([-6*elem[0],['t1']])
        if 'p1' in elem[1] and 'p2' in elem[1]:
            elem[1].remove('p1')
            elem[1].remove('p2')
            elem[1].append('t2')
            reducer.append([elem[0],elem[1]])
            if elem[0]>0:
                reducer.append([2*elem[0],['p1', 'p2']])
                reducer.append([-4*elem[0],['p1', 't2']])
                reducer.append([-4*elem[0],['p2', 't2']])
                reducer.append([6*elem[0],['t2']])
            else:
                reducer.append([-2*elem[0],['p1', 'p2']])
                reducer.append([4*elem[0],['p1', 't2']])
                reducer.append([4*elem[0],['p2', 't2']])
                reducer.append([-6*elem[0],['t2']])

        if 'p2' in elem[1] and 'q2' in elem[1]:
            elem[1].remove('p2')
            elem[1].remove('q2')
            elem[1].append('t3')
            reducer.append([elem[0],elem[1]])
            if elem[0]>0:
                reducer.append([2*elem[0],['p2', 'q2']])
                reducer.append([-4*elem[0],['p2', 't3']])
                reducer.append([-4*elem[0],['q2', 't3']])
                reducer.append([6*elem[0],['t3']])
            else:
                reducer.append([-2*elem[0],['p2', 'q2']])
                reducer.append([4*elem[0],['p2', 't3']])
                reducer.append([4*elem[0],['q2', 't3']])
                reducer.append([-6*elem[0],['t3']])

print()






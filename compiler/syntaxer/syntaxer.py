class Syntaxer (object):
    def __init__(self, *arg):
        self.lexemes = arg
        # print('arg = ', arg)

    # statemenize method - create statement list from lexemes
    def syntaxer(self):
        lexemes = list(self.lexemes[0])
        begin = 0

        print('len(lexemes) = ', len(lexemes))


        
        while begin < len(lexemes) and begin >= 0:

            isCheck, result, newBegin = checkAllRules(lexemes, begin)


            # print('isCheck = ', isCheck)
            print('Result = ', result)
           
            begin = newBegin
            print('\n\n')


        print('after while')
     

# ==============================================
# End class here
# ==============================================

def checkAllRules(arg, begin):

    availableLen = len(arg) - begin
    print('availableLen = ', availableLen)

    isDeclare, resultDeclare, newBeginDeclare = isDeclarative (arg, begin)

    if isDeclare:
        newBeginDeclare = begin + 3
        return isDeclare, resultDeclare, newBeginDeclare


    isAss, resultAssign, newBeginAssign, totalexplength = isAssign (arg, begin)

    if isAssign:
        newBeginAssign = begin + totalexplength
        return isAss, resultAssign, newBeginAssign

    else:
        print ('Something go wrong1')

        begin = 99999999999999999
        return -1, -2, begin



def getKeyValue (mydict):
    for key, value in mydict.items():
        return key, value

def getSpecificKV (lexemelist,myvalue,beginval):
    positionval = beginval
    for x in range(beginval):
        positionval = positionval + 1
        for key,value in x.items():
            if value == myvalue :
                return key,value,positionval
        


#       Example : int a
#<Statement> -> <Declarative>
#<Declarative> -> <Type> <id>
def isDeclarative (arg, begin):
    myType = ['int', 'float', 'bool']
    print()

    key0, value0 = getKeyValue(arg[begin])
    key1, value1 = getKeyValue(arg[begin + 1])
    key2, value2 = getKeyValue(arg[begin + 2])

    if (value0 in myType) and key1 == 'IDENTIFIER' and value2 == ';':
        result = []
        result.append( {
            'Token': key0,
            'Lexeme': value0,
            'Grammar': '<Statement> -> <Declarative>' 
                        '<Declarative> -> <Type> <id>',
            'Token2': key1,
            'Lexeme2': value1,
            'Grammar2': '<Statement> -> <Declarative>' 
                        '<Declarative> -> <Type> <id>',
            'Token3': key2,
            'Lexeme3': value2,
            'Grammar3': '<Statement> -> <Declarative>' 
                        '<Declarative> -> <Type> <id>'
        })
        return True, result, begin
    else:
        return False, -1, 999999999999
  

#<Statement> -> <Assign>
#<Assign> -> <ID> = <Expression>;
def isAssign(arg, begin):
    print("Inside Assign")


    key0, value0 = getKeyValue(arg[begin])
    key1, value1 = getKeyValue(arg[begin + 1])
    key2, value2 , posval = getSpecificKV(arg,';',begin + 2)
    
    if key0 == 'IDENTIFIER' and value1 == '=':
        result = {
            'Token' : 'Assign',
            'Lexeme': ''
        }
        isExp, resultExpress, newbegin, totaladded = isExpress (arg, begin + 2,posval)
        result += resultExpress
        total = totaladded
        return isExp, result, begin, total
    else:
        return False, -1, 999999999999

def isExpress(arg,begin,posval):
    print("Inside Expression")

    

# # <A1> -> <ID> = <NUM> ;      a = 1
# # <Define> -> <IDs> = <NUM> ;       Example: a = 1
# def isDefine1 (arg, begin):
#     print()
#     print('begin in isDefine1 = ', begin)
#     # print('arg in isDefine1 = ')
#     # for i in arg:
#     #     print(f'{i}')
#     # print()
#     myNum = ['INT', 'FLOAT']
#     myBool = ['true', 'false']


#     # print(f'arg[{ begin }] = { arg[begin] }')
#     # print(f'arg[{ begin + 1 }] = { arg[begin + 1] }')
#     # print(f'arg[{ begin + 2 }] = { arg[begin + 2] }')
#     # print(f'arg[{ begin + 3 }] = { arg[begin + 3] }')
#     # print()

#     key0, value0 = getKeyValue(arg[begin])
#     key1, value1 = getKeyValue(arg[begin + 1])
#     key2, value2 = getKeyValue(arg[begin + 2])
#     key3, value3 = getKeyValue(arg[begin + 3])

#     # print()
#     # print('key0   = ', key0)
#     # print('value0 = ', value0)
#     # print()
#     # print('key1   = ', key1)
#     # print('value1 = ', value1)
#     # print()
#     # print('key2   = ', key2)
#     # print('value2 = ', value2)
#     # print()
#     # print('key3   = ', key3)
#     # print('value3 = ', value3)
#     # print()


#     if key0 == 'IDENTIFIER' and value1 == '=' and value2 in myBool and value3 == ';':
#         result = {
#             'Token': 'Define',
#             'Lexeme': '',
#             'BNF': '<Define> -> <Identifier>  = true/false ;'
#         }
#         return True, result, begin
#     elif key0 == 'IDENTIFIER' and value1 == '=' and key2 in myNum and value3 == ';':
#         result = {
#             'Token': 'Define',
#             'Lexeme': '',
#             'BNF': '<Define> -> <Identifier>  = number ;'
#         }
#         return True, result, begin
#     else:
#         return False, -1, 9999999999



# # <A2> -> <ID> = <ID> ;       a = b
# def isDefine2 (arg, begin):
# # B
# # 1
# # n
# # h
# # Tr 4 n 


#     print()
#     # print('arg in isDefine2 = ')
#     # for i in arg:
#     #     print(f'{i}')
#     # print()

#     # print('begin in isDefine2 = ', begin)

#     # print(f'arg[{ begin }] = { arg[begin] }')
#     # print(f'arg[{ begin + 1 }] = { arg[begin + 1] }')
#     # print(f'arg[{ begin + 2 }] = { arg[begin + 2] }')
#     # print(f'arg[{ begin + 3 }] = { arg[begin + 3] }')
#     # print()

#     key0, value0 = getKeyValue(arg[begin])
#     key1, value1 = getKeyValue(arg[begin + 1])
#     key2, value2 = getKeyValue(arg[begin + 2])
#     key3, value3 = getKeyValue(arg[begin + 3])

#     # print()
#     # print('key0   = ', key0)
#     # print('value0 = ', value0)
#     # print()
#     # print('key1   = ', key1)
#     # print('value1 = ', value1)
#     # print()
#     # print('key2   = ', key2)
#     # print('value2 = ', value2)
#     # print()
#     # print('key3   = ', key3)
#     # print('value3 = ', value3)
#     # print()


#     if key0 == 'IDENTIFIER' and value1 == '=' and key2 == 'IDENTIFIER' and value3 == ';':
#         result = {
#             'Token': 'Define2',
#             'Lexeme': '',
#             'BNF': '<Define2> -> <Identifier>  = <Identifier> ;'
#         }
#         return True, result, begin
    
#     else:
#         return False, -1, 9999999999








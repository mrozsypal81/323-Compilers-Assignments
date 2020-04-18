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

            print('Returned from CheckAllRules')

            print('isCheck = ', isCheck)
            for i in result:
                print(i)
           
            begin = newBegin
            print('\n\n')


        print('Done with all Lexemes')
     

# ==============================================
# End class here
# ==============================================

def checkAllRules(arg, begin):

    availableLen = len(arg) - begin
    print('availableLen = ', availableLen)

    #This returns the next semicolon position so that you can tell where to end
    print("Begin value")
    print(begin)
    semicolkey,semicolval,semicolpos = getSpecificKV(arg,";",begin)
    templist = arg[begin:semicolpos+1]

    print("++++++++++++++++++++templist++++++++++++++++")
    print(templist)
    print("++++++++++++++++++++after templist++++++++++++++++")

    #testkey,testval,testpos = getSpecificKVreverse(arg,"+",semicolpos)

    if len(templist) == 3: 
        isDeclare, resultDeclare = isDeclarative (templist)

        if isDeclare:
            newBeginDeclare = begin + 3
            return isDeclare, resultDeclare, newBeginDeclare

    
        # isAss, resultAssign, newBeginAssign = isAssign (arg, begin)

        # if isAss:
        #     return isAss, resultAssign, newBeginAssign

        # isExp, resultExpress, newbegin = isExpress (arg, begin,begin)
        
        # if isExp:
        #     return isExp,resultExpress,newbegin

    print('End of CheckAllRules')
    return False,[],-1

# x + y = z;

def getKeyValue (mydict):
    for key, value in mydict.items():
        return key, value

def getSpecificKV (arg,myvalue,beginval):
    positionval = beginval
    for x in arg[beginval:]:   
        for key,value in x.items():
            print("Next in specific function")
            print(key,value,positionval)
            print("++++++++++++++++++++++++++++++++++++++")
            if value == myvalue :
                print("Match in specific function")
                print(key,value,positionval)
                print("++++++++++++++++++++++++++++++++++++++")
                return key,value,positionval
        positionval = positionval + 1
    return None,None,-1

# def getSpecificKVreverse (arg,myvalue,beginval):
#     positionval = 0
#     reversedlist = 
#     for i,x in reversed(list(enumerate(arg[beginval:]))):  
#         for key,value in x.items():
#             print("Next in reverse function")
#             print(key,value,i)
#             print("++++++++++++++++++++++++++++++++++++++")
#             if value == myvalue :
#                 print("found Value")
#                 print(key,value,i)
#                 print("++++++++++++++++++++++++++++++++++++++")
#                 positionval = i
#                 return key,value,positionval
#     return None,None,-1
        

#                   0 1 2  3 4 5  6  7 8
#       Example : int a; int b; int x ;
#<Statement> -> <Declarative>
#<Declarative> -> <Type> <id>;
def isDeclarative (arg):
    myType = ['int', 'float', 'bool']
    print('Inside isDeclarative')

    key0, value0 = getKeyValue(arg[0])
    key1, value1 = getKeyValue(arg[1])
    key2, value2 = getKeyValue(arg[2])

    if (value0 in myType) and key1 == 'IDENTIFIER' and value2 == ';':
        result = []
        result.append( {
            'Token': key0,
            'Lexeme': value0,
            'Grammar': '<Statement> -> <Declarative>' 
                        '<Declarative> -> <Type> <id>;'
        })
        result.append({            
            'Token': key1,
            'Lexeme': value1,
            'Grammar': '<Statement> -> <Declarative>' 
                        '<Declarative> -> <Type> <id>;'
        })
        result.append({            
            'Token': key2,
            'Lexeme': value2,
            'Grammar': '<Statement> -> <Declarative>' 
                        '<Declarative> -> <Type> <id>;'
        })
        return True, result
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
        result = []
        result.append( {
            'Token': key0,
            'Lexeme': value0,
            'Grammar': '<Statement> -> <Assign>' 
                        '<Assign> -> <ID> = <Expression>;'

        })
        result.append({            
            'Token': key1,
            'Lexeme': value1,
            'Grammar': '<Statement> -> <Assign>' 
                        '<Assign> -> <ID> = <Expression>;'
        })
        isExp, resultExpress, newbegin = isExpress (arg, begin + 2,posval)

        if isExp:
            begin = newbegin + 1
            result.extend(resultExpress)
            result.append({            
                'Token': key2,
                'Lexeme': value2,
                'Grammar': '<Statement> -> <Assign>' 
                            '<<Assign> -> <ID> = <Expression>;'
            })
        else:
            print('Assign Error at lexeme '+ begin)

        


        return isExp, result, begin
    else:
        print('Assign Error at lexeme ', begin)
        return False, -1, 999999999999

#<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>
def isExpress(arg,begin,posval):
    #print("Inside Expression")

    result = []
    isresult = False
    
    pkey,pvalue,posval = getSpecificKV(arg,';',begin)

    #key, value , plusval = getSpecificKVreverse(arg,'+',posval)
    #key2, value2 , minusval = getSpecificKVreverse(arg,'-',posval)


    if value == '+':
        print("Inside Expression +")
        isExp, resultExpress, newbegin = isExpress (arg, begin ,plusval-1)
        
        if isExp:
            isresult = isExp
            result.extend(resultExpress)
            result.append( {
                'Token': key,
                'Lexeme': value,
                'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'

            })
        else:
            print('Expression Error at lexeme '+ begin)

        print("Inside Expression + term")
        isTe, resultTerm, newbegin = isTerm (arg,plusval+1,posval)
        
        if isTe:
            isresult = isTe
            begin = newbegin
            result.extend(resultTerm)
        else:
            print('Expression Error at lexeme '+ begin)


    if value2 == '-':
        print("Inside Expression -")
        isExp, resultExpress, newbegin = isExpress (arg, begin ,minusval-1)
        
        if isExp:
            isresult = isExp
            result.extend(resultExpress)
            result.append( {
                'Token': key2,
                'Lexeme': value2,
                'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'

            })
        else:
            print('Expression Error at lexeme '+ begin)

        print("Inside Expression - term")

        isTe, resultTerm, newbegin = isTerm (arg,minusval+1,posval)
        
        if isTe:
            isresult = isTe
            begin = newbegin + 1
            result.extend(resultTerm)
        else:
            print('Expression Error at lexeme '+ begin)

    if value == None and value2 == None:
        print("Inside Expression term")
        isTe, resultTerm, newbegin = isTerm (arg,begin,posval)
        
        if isTe:
            isresult = isTe
            begin = newbegin
            result.extend(resultTerm)
        else:
            print('Expression Error at lexeme '+ begin)
    
    if isresult:
        return isresult,result,begin


#<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>
def isTerm(arg,begin,posval):
    #print('Inside isTerm')

    
    result = []
    isresult = False

    #key, value , starval = getSpecificKVreverse(arg,'*',posval)
    #key2, value2 , divVal = getSpecificKVreverse(arg,'/',posval)


    if value == '*':
        isTe, resultTerm, newbegin = isTerm (arg, begin ,starval-1)
        
        if isTe:
            isresult = isTe
            result.extend(resultTerm)
            result.append( {
                'Token': key,
                'Lexeme': value,
                'Grammar': '<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>'

            })
        else:
            print('Term Error at lexeme '+ begin)

        isFac, resultFac, newbegin = isFactor (arg,starval+1,posval)
        
        if isFac:
            isresult = isFac
            begin = newbegin + 1
            result.extend(resultFac)
        else:
            print('Term Error at lexeme '+ begin)


    if value2 == '/':
        isTe, resultTerm, newbegin = isTerm (arg, begin ,divVal-1)
        
        if isTe:
            isresult = isTe
            result.extend(resultTerm)
            result.append( {
                'Token': key2,
                'Lexeme': value2,
                'Grammar': '<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>'

            })
        else:
            print('Term Error at lexeme '+ begin)

        isFac, resultFac, newbegin = isFactor (arg,divVal+1,posval)
        
        if isFac:
            isresult = isFac
            begin = newbegin + 1
            result.extend(resultFac)
        else:
            print('Term Error at lexeme '+ begin)

    if value == None and value2 == None:
        isFac, resultFac, newbegin = isFactor (arg,begin,posval)
        
        if isFac:
            isresult = isFac
            begin = newbegin
            result.extend(resultFac)
        else:
            print('Term Error at lexeme '+ begin)
    
    if isresult:
        return isresult,result,begin


#<Factor> -> ( <Expression> ) | <ID> | <num> 
def isFactor (arg,begin,posval):
    print('Inside isFactor')


    
    result = []
    isresult = False

    key, value , forwardparenval = getSpecificKV(arg,'(',begin)
    #key2, value2 , backwardparenval = getSpecificKVreverse(arg,')',posval)

    if value == '(' and value2 == ')':
        isExp, resultExpress, newbegin = isExpress (arg, forwardparenval + 1,backwardparenval)
        
        if isExp:
            result.append( {
                'Token': key,
                'Lexeme': value,
                'Grammar': '<Factor> -> ( <Expression> ) | <ID> | <num> '

            })
            isresult = isExp
            begin = newbegin + 2
            result.extend(resultExpress)
            
            result.append( {
                'Token': key2,
                'Lexeme': value2,
                'Grammar': '<Factor> -> ( <Expression> ) | <ID> | <num> '

            })

        else:
            print('Term Error at lexeme '+ begin)


    if value == None and value2 == None:
        isIDcheck, resultID, newbegin = isID (arg,begin,posval)
        
        if isIDcheck:
            isresult = isIDcheck
            begin = newbegin
            result.extend(resultID)
        else:
            print('Term Error at lexeme '+ begin)
    
    if isresult:
        return isresult,result,begin

#<ID> -> id
def isID (arg,begin,posval):
    print('Inside isID')

    result = []
    isresult = False
    key, value = getKeyValue(arg[begin])
    #print('Inside isID2')

    if key == 'IDENTIFIER' or key == 'KEYWORD' or key == 'FLOAT' or key == 'INT':
        #print('Inside isID3')
        isresult = True
        result.append( {
                'Token': key,
                'Lexeme': value,
                'Grammar': '<ID> -> id'
        })
        begin = begin + 1
    #print('Inside isID4')
    if isresult:
        #print('Inside isID5')
        return isresult,result,begin

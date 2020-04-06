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


    isAss, resultAssign, newBeginAssign = isAssign (arg, begin)

    if isAssign:
        newBeginAssign = begin
        return isAss, resultAssign, newBeginAssign

    else:
        print ('Something go wrong1')

        begin = 99999999999999999
        return -1, -2, begin



def getKeyValue (mydict):
    for key, value in mydict.items():
        return key, value

def getSpecificKV (arg,myvalue,beginval):
    positionval = beginval
    for x in arg[beginval:]:   
        for key,value in x.items():
            if value == myvalue :
                return key,value,positionval
        positionval = positionval + 1
    return None,None,-1

def getSpecificKVreverse (arg,myvalue,beginval):
    positionval = beginval
    for x in  arg[beginval::-1]:  
        for key,value in x.items():
            if value == myvalue :
                return key,value,positionval
        positionval = positionval - 1
    return None,None,-1
        


#       Example : int a
#<Statement> -> <Declarative>
#<Declarative> -> <Type> <id>;
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
            begin = newbegin
            result.extend(resultExpress)
        else:
            print('Assign Error at lexeme '+ begin)

        

        result.append({            
            'Token': key2,
            'Lexeme': value2,
            'Grammar': '<Statement> -> <Assign>' 
                        '<<Assign> -> <ID> = <Expression>;'
        })
        return isExp, result, begin
    else:
        return False, -1, 999999999999

#<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>
def isExpress(arg,begin,posval):
    print("Inside Expression")

    result = []
    isresult = False

    key, value , plusval = getSpecificKVreverse(arg,'+',posval)
    key2, value2 , minusval = getSpecificKVreverse(arg,'-',posval)


    if value == '+':
        isExp, resultExpress, newbegin = isExpress (arg, begin ,plusval-1)
        
        if isExp:
            isresult = isExp
            begin = newbegin
            result.extend(resultExpress)
            result.append( {
                'Token': key,
                'Lexeme': value,
                'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'

            })
        else:
            print('Expression Error at lexeme '+ begin)

        isTe, resultTerm, newbegin = isTerm (arg,plusval+1,posval)
        
        if isTe:
            isresult = isTe
            begin = newbegin
            result.extend(resultTerm)
        else:
            print('Expression Error at lexeme '+ begin)


    if value2 == '-':
        isExp, resultExpress, newbegin = isExpress (arg, begin ,minusval-1)
        
        if isExp:
            isresult = isExp
            begin = newbegin
            result.extend(resultExpress)
            result.append( {
                'Token': key2,
                'Lexeme': value2,
                'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'

            })
        else:
            print('Expression Error at lexeme '+ begin)

        isTe, resultTerm, newbegin = isTerm (arg,minusval+1,posval)
        
        if isTe:
            isresult = isTe
            begin = newbegin
            result.extend(resultTerm)
        else:
            print('Expression Error at lexeme '+ begin)

    if value == None and value2 == None:
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
    print('Inside isTerm')

    
    result = []
    isresult = False

    key, value , starval = getSpecificKVreverse(arg,'*',posval)
    key2, value2 , divVal = getSpecificKVreverse(arg,'/',posval)


    if value == '*':
        isTe, resultTerm, newbegin = isTerm (arg, begin ,starval-1)
        
        if isTe:
            isresult = isTe
            begin = newbegin
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
            begin = newbegin
            result.extend(resultFac)
        else:
            print('Term Error at lexeme '+ begin)


    if value2 == '/':
        isTe, resultTerm, newbegin = isTerm (arg, begin ,divVal-1)
        
        if isTe:
            isresult = isTe
            begin = newbegin
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
            begin = newbegin
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

def isFactor (arg,begin,posval):
    print('Inside isFactor')


    
    result = []
    isresult = False

    key, value , forwardparenval = getSpecificKV(arg,'(',begin)
    key2, value2 , backwardparenval = getSpecificKVreverse(arg,')',posval)
    key3, value3 = getKeyValue(begin)


    if value == '(' and value2 == ')':
        isExp, resultExpress, newbegin = isExpress (arg, forwardparenval + 1,backwardparenval)
        
        if isExp:
            isresult = isExp
            begin = newbegin
            result.extend(resultExpress)

        else:
            print('Term Error at lexeme '+ begin)


    if value == None and value2 == None:
        isID, resultID, newbegin = isID (arg,begin,posval)
        
        if isID:
            isresult = isID
            begin = newbegin
            result.extend(resultID)
        else:
            print('Term Error at lexeme '+ begin)
    
    if isresult:
        return isresult,result,begin


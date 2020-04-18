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

    eqkey,eqval = getKeyValue(templist)
    
    if eqval == "=":
    
        isAss, resultAssign, newBeginAssign = isAssign (arg)

        if isAss:
            return isAss, resultAssign, newBeginAssign

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
def isAssign(arg):
    print("Inside Assign")

    count = 0
    key0, value0 = getKeyValue(arg[0])
    key1, value1 = getKeyValue(arg[1])
    key2, value2 = getKeyValue(arg[len(arg)-1]) 
    
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
        count += 2
        isExp, resultExpress, AddCount = isExpress (arg,0)

        if isExp:
            count = count + AddCount + 1
            result.extend(resultExpress)
            result.append({            
                'Token': key2,
                'Lexeme': value2,
                'Grammar': '<Statement> -> <Assign>' 
                            '<<Assign> -> <ID> = <Expression>;'
            })
        else:
            print('Assign Error at lexeme '+ count)

        


        return isExp, result, count
    else:
        print('Assign Error at lexeme ', count)
        return False, -1, 999999999999

#<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>
def isExpress(arg,posval):
    #print("Inside Expression")

    count = 0
    result = []
    isresult = False
    
    pkey,pvalue,pluspos = getSpecificKV(arg,'+',posval)
    mkey,mvalue, minuspos = getSpecificKV(arg,'-',posval)

    #key, value , plusval = getSpecificKVreverse(arg,'+',posval)
    #key2, value2 , minusval = getSpecificKVreverse(arg,'-',posval)


    if pvalue == '+':
        print("Inside Expression +")
        isExp, resultExpress, AddCount = isExpress (arg, pluspos+1)
        
        if isExp:
            isresult = isExp
            result.extend(resultExpress)
            count += (AddCount + 1)
            result.append( {
                'Token': pkey,
                'Lexeme': pvalue,
                'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'

            })
        else:
            print('Expression Error at lexeme '+ pluspos)
        
        print("Inside Expression + term")
        isTe, resultTerm, AddCount = isTerm (arg,pluspos+1)
        
        if isTe:
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)
        else:
            print('Expression Error at lexeme '+ pluspos)


    if mvalue == '-':
        print("Inside Expression -")
        isExp, resultExpress, AddCount = isExpress (arg, minuspos+1)
        
        if isExp:
            isresult = isExp
            count += (AddCount + 1)
            result.extend(resultExpress)
            result.append( {
                'Token': mkey,
                'Lexeme': mvalue,
                'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'

            })
        else:
            print('Expression Error at lexeme '+ minuspos)

        print("Inside Expression - term")

        isTe, resultTerm, AddCount = isTerm (arg,minuspos+1)
        
        if isTe:
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)
        else:
            print('Expression Error at lexeme '+ minuspos)

    if pvalue == None and mvalue == None:
        print("Inside Expression term")
        isTe, resultTerm, AddCount = isTerm (arg,posval)
        
        if isTe:
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)
        else:
            print('Expression Error at lexeme '+ posval)
    
    if isresult:
        return isresult,result,count


#<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>
def isTerm(arg,posval):
    #print('Inside isTerm')

    count = 0
    result = []
    isresult = False

    skey,svalue,starpos = getSpecificKV(arg,'*',posval)
    dkey,dvalue, divpos = getSpecificKV(arg,'/',posval)

    #key, value , starval = getSpecificKVreverse(arg,'*',posval)
    #key2, value2 , divVal = getSpecificKVreverse(arg,'/',posval)


    if svalue == '*':
        #may have to rethink the positioning of the start of the next isterm same with isexpression
        #it does not know when to stop running 
        isTe, resultTerm, AddCount = isTerm (arg,starpos+1)
        
        if isTe:
            isresult = isTe
            count += (AddCount + 1)
            result.extend(resultTerm)
            result.append( {
                'Token': skey,
                'Lexeme': svalue,
                'Grammar': '<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>'

            })
        else:
            print('Term Error at lexeme '+ starpos)

        isFac, resultFac, AddCount = isFactor (arg,starpos+1)
        
        if isFac:
            isresult = isFac
            count += AddCount
            result.extend(resultFac)
        else:
            print('Term Error at lexeme '+ starpos)


    if dvalue == '/':
        isTe, resultTerm, newbegin = isTerm (arg,divpos+1)
        
        if isTe:
            isresult = isTe
            count += (AddCount + 1)
            result.extend(resultTerm)
            result.append( {
                'Token': dkey,
                'Lexeme': dvalue,
                'Grammar': '<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>'

            })
        else:
            print('Term Error at lexeme '+ divpos)

        isFac, resultFac, newbegin = isFactor (arg,divpos+1)
        
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

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
    print("Inside Expression")

    count = 0

    isresult = False
    
    result = []

    print("Going into isTerm")
    isTe, resultTerm, AddCount = isTerm (arg,posval)
        
    if isTe:
        isresult = isTe
        count += AddCount
        result.extend(resultTerm)
    else:
        print('Expression Error at lexeme '+ posval)

    print("Going into isExpressPrime")
    isExp, resultExpress, AddCount = isExpressPrime (arg, posval)
        
    if isExp:
        isresult = isExp
        result.extend(resultExpress)
        count += AddCount
    else:
        print('Expression Error at lexeme '+ posval)

    if isresult:
        return isresult,result,count
        
def isExpressPrime(arg,posval):
    print("Inside isExpressPrime")
    count = 0
    result = []
    isresult = False
    
    pkey,pvalue,pluspos = getSpecificKV(arg,'+',posval)
    mkey,mvalue, minuspos = getSpecificKV(arg,'-',posval)


    if pvalue == '+':
        print("Inside Express + appending to result")

        result.append( {
            'Token': pkey,
            'Lexeme': pvalue,
            'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'
        })
        #the +1 is to account for the append
        count += 1

        print("Inside ExpressPrime + going into Term")
        isTe, resultTerm, AddCount = isTerm (arg,pluspos+1)
        
        if isTe:
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)
        else:
            print('ExpressionPrime Error at lexeme '+ pluspos)

        print("Inside ExpressPrime + going into ExpressPrime")
        isExp, resultExpress, AddCount = isExpressPrime (arg, pluspos+1)
        
        if isExp:
            isresult = isExp
            result.extend(resultExpress)
            count += AddCount
        else:
            print('ExpressionPrime Error at lexeme '+ pluspos)
        
    if pvalue == '-':
        print("Inside Express - appending to result")

        result.append( {
            'Token': mkey,
            'Lexeme': mvalue,
            'Grammar': '<Expression> -> <Expression> + <Term> | <Expression> - <Term> | <Term>'
        })
        
        #the +1 is to account for the append
        count += 1
        
        print("Inside ExpressPrime - going into Term")
        isTe, resultTerm, AddCount = isTerm (arg,minuspos+1)
        
        if isTe:
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)
        else:
            print('ExpressionPrime Error at lexeme '+ minuspos)

        print("Inside ExpressPrime + going into ExpressPrime")
        isExp, resultExpress, AddCount = isExpressPrime (arg, minuspos+1)
        
        if isExp:
            isresult = isExp
            result.extend(resultExpress)
            count += AddCount
        else:
            print('ExpressionPrime Error at lexeme '+ minuspos)

    if pvalue == None and mvalue == None:
        print("Inside ExpressPrime Epsilon")
        #This does nothing really it just returns whatever it found which should be nothing

        return True,result,count
        
    
    if isresult:
        return isresult,result,count

#<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>
def isTerm(arg,posval):
    print('Inside isTerm')


    count = 0

    isresult = False
    
    result = []

    print("Going into isFactor")
    isFac, resultFac, AddCount = isFactor (arg,posval)
        
    if isFac:
        isresult = isFac
        count += AddCount
        result.extend(resultFac)
    else:
        print('Term Error at lexeme '+ posval)

    print("Going into isTermPrime")
    isTe, resultTerm, AddCount = isTermPrime (arg,posval)
        
    if isTe:
        isresult = isTe
        count += AddCount
        result.extend(resultTerm)
    else:
        print('Term Error at lexeme '+ posval)

    if isresult:
        return isresult,result,count
        

def isTermPrime(arg,posval):
    print("Inside isTermPrime")

    count = 0
    result = []
    isresult = False

    skey,svalue,starpos = getSpecificKV(arg,'*',posval)
    dkey,dvalue, divpos = getSpecificKV(arg,'/',posval)

    if svalue == '*':
        print("Inside isTermPrime * appending")

        result.append( {
            'Token': skey,
            'Lexeme': svalue,
            'Grammar': '<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>'

        })
        #the +1 is to account for the append
        count += 1

        print("INside isTermPrime going into isFactor in *")
        isFac, resultFac, AddCount = isFactor (arg,starpos+1)
        
        if isFac:
            isresult = isFac
            count += AddCount
            result.extend(resultFac)
        else:
            print('TermPrime Error at lexeme '+ starpos)

        isTe, resultTerm, AddCount = isTermPrime (arg,starpos+1)
        
        if isTe:
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)

        else:
            print('TermPrime Error at lexeme '+ starpos)




    if dvalue == '/':
        print("Inside isTermPrime / appending")

        result.append( {
            'Token': dkey,
            'Lexeme': dvalue,
            'Grammar': '<Term> -> <Term> * <Factor> | <Term> / <Factor> | <Factor>'

        })
        #the +1 is to account for the append
        count += 1
        print("Inside isTermPrime going into isFactor in /")
        isFac, resultFac, AddCount = isFactor (arg,divpos+1)
        
        if isFac:
            isresult = isFac
            count += AddCount
            result.extend(resultFac)
        else:
            print('TermPrime Error at lexeme '+ divpos)

        isTe, resultTerm, AddCount = isTermPrime (arg,divpos+1)
        
        if isTe:
            isresult = isTe
            count += AddCount
            result.extend(resultTerm)

        else:
            print('TermPrime Error at lexeme '+ divpos)

    if svalue == None and dvalue == None:
        print("Inside TermPrime Epsilon")
        #This does nothing really it just returns whatever it found which should be nothing

        return True,result,count

    if isresult:
        return isresult,result,count

#<Factor> -> ( <Expression> ) | <ID> | <num> 
def isFactor (arg,posval):
    print('Inside isFactor')


    
    result = []
    isresult = False

    fkey, fvalue , fpos = getSpecificKV(arg,'(',posval)
    bkey2, bvalue2 , bpos = getSpecificKV(arg,')',posval)

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
def isID (arg,posval):
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

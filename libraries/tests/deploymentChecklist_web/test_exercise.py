# import pytest

# # Exercise 1: # print by brand, model and year   --   INFO = 'TOYOTA - INNOVA - 1997, HONDA - JAZZ - 1995, BMW - IX3 - 2000, FORD - ECOSPORTS - 1992, NISSAN - VERSA - 2002'
# # Exercise 2: Associate a-z to numbers then get the total equivalent points of the word HARDWORK, CONFIDENCE, TEAMWORK, ATTITUDE
# def test_exercise1(page):
#     INFO = 'TOYOTA - INNOVA - 1997, HONDA - JAZZ - 1995, BMW - IX3 - 2000, FORD - ECOSPORTS - 1992, NISSAN - VERSA - 2002'
#     # print by brand, model and year
    
    
#     print(1)
#     print(2)
#     print(INFO)
#     breakpoint()



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# @pytest.mark.thisTestExercise()
# def test_exercise1(page):
#     INFO = 'TOYOTA - INNOVA - 1997, HONDA - JAZZ - 1995, BMW - IX3 - 2000, FORD - ECOSPORTS - 1992, NISSAN - VERSA - 2002'
#     # 1. print brand name, carname, year
    
#     arrCar = INFO.split(',')
    
#     strBrand = ''
#     strType = ''
#     strYear = ''
#     for item in arrCar:
#         arrSplice = item.split(' - ')
#         arrBrand = arrSplice[0]
#         arrType = arrSplice[1]
#         arrYear = arrSplice[2]
        
#         if strBrand == '':
#             strBrand = arrBrand
#             strType = arrType
#             strYear = arrYear
#         else:
#             strBrand = f'{strBrand}, {arrBrand}'
#             strType = f'{strType}, {arrType}'
#             strYear = f'{strYear}, {arrYear}'
        
     
     
#     print(strBrand)
#     breakpoint()
#     print(strType)
#     breakpoint()
#     print(strYear)

# def test_exercise2(page):
#     # strWord = 'HARDWORK'
#     # strWord = 'CONFIDENCE'
#     # strWord = 'TEAMWORK'
#     strWord = 'ATTITUDE'
#     intWord = len(strWord)
#     intTotalCount = 0
#     for item in range(intWord):
#         strLetter = strWord[item:item+1]
#         arrAlphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#         intCnt = 1
#         for item in range(len(arrAlphabets)):
#             if strLetter == arrAlphabets[item].upper():
#                 intInitialCount = intCnt
#                 break
#             intCnt = intCnt + 1
#         intTotalCount = intTotalCount + intInitialCount
    
#     print(f'{strWord} score is {intTotalCount}')
#     breakpoint()
class orders:
    def param(strOrderID):
        return f'page=1&limit=10&search={strOrderID}'
    
    
    
    
    
class products:
    def param(strProductName):
        strParam = f'{strProductName.replace(" ", "%20")}&page=1&limit=10'
        return strParam
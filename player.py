class Player:
    def __init__(self,nombre,estado,bola,posx,posy,imagen):
        self.__nombre=nombre
        self.__estado=estado
        self.__bola=bola
        self.posx=posx
        self.posy=posy
        self.imagen=imagen

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nNombre):
        self.__nombre=nNombre
    
    def getEstado(self):
        return self.__estado
    def setEstado(self,nEstado):
        self.__estado=nEstado
    
    def getBola(self):
        return self.__bola
    def setBola(self,nBola):
        self.__bola=nBola
    
        
    
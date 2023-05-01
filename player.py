class Player:
    """Trae los metodos y atibutos de cada jugador"""
    def __init__(self,nombre,estado,bola,posx,posy,imagen):
        """Crea los atributos de la funcion"""
        self.__nombre=nombre
        self.__estado=estado
        self.__bola=bola
        self.posx=posx
        self.posy=posy
        self.imagen=imagen

    def getNombre(self):
        """es un get"""
        return self.__nombre
    def setNombre(self,nNombre):
        """es un set"""
        self.__nombre=nNombre
    
    def getEstado(self):
        """es un get"""
        return self.__estado
    def setEstado(self,nEstado):
        """es un set"""
        self.__estado=nEstado
    
    def getBola(self):
        """es un get"""
        return self.__bola
    def setBola(self,nBola):
        """es un set"""
        self.__bola=nBola
    
        
    
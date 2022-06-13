def AutoPartes(ventas: list):
    partesA = {}
    for x in range(len(ventas)): 
        partesA[x]= [ventas[x]]
    return partesA

def consultaRegistro(ventas, idProductos):
    conRe = {}
    for i in ventas:
        if idProductos == ventas[i][0][0]:
            conRe[i] = ventas[i]
    conRe2 =''
    if len(conRe)==0:
        conRe2 ="No hay registro de venta de ese producto"
    else:
        for i in conRe:
            j=0
            #conRe2+='Producto consultado : ventasDescripción {}{}{}{}{}{}{}{}\n'.format(ventas[i][j][0], ventas[i][j][1], ventas[i][j][2], ventas[i][j][3], ventas[i][j][4], ventas[i][j][5], ventas[i][j][6], ventas[i][j][7], ventas[i][j][8])
            conRe2+='Producto consultado : {}  Descripción  {}  #Parte  {}  Cantidad vendida  {}  Stock  {}  Comprador {}  Documento  {}  Fecha Venta  {}\n'.format(ventas[i][j][0], ventas[i][j][1], ventas[i][j][2], ventas[i][j][3], ventas[i][j][4], ventas[i][j][5], ventas[i][j][6], ventas[i][j][7])
            j+=1
    return print(conRe2)

consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]),9251)
print()

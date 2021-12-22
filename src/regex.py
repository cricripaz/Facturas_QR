import pandas as pd



#           First|second|third|fourth|fifth|sixth|7|8|9|10|11|12
text = "6180524016|8546|384401100212133|11/12/2021|72.00|72.00|FB-90-01-FA-7C|9993925|0.00|0.00|0.00|0.00"

# Solucion Buena

textxd = text.rsplit("|")

print(textxd)

print("cantidad parametros factura " , len(textxd))


listNIT = []
listNAutorizacion = []
listNFactura = []
listImporte = []
listFecha = []
listCodigoControl = []

data_factura ={

        'NIT': listNIT,
        'Numero Autorizacion': listNAutorizacion,
        'Numero Factura': listNFactura,
        'Importe': listImporte,
        'Fecha': listFecha,
        'Codigo Control': listCodigoControl,

              }


columnas = ['NIT','Numero Autorizacion','Numero Factura','Importe','Fecha','Codigo Control']



def add_data_excel(string):
    lista_datos = string.rsplit("|")

    listNIT.append(lista_datos[0])
    listNAutorizacion.append(lista_datos[2])
    listNFactura.append(lista_datos[1])
    listImporte.append(lista_datos[4])
    listFecha.append(lista_datos[3])
    listCodigoControl.append(lista_datos[6])

    df = pd.DataFrame(data_factura,columns=[columnas[0], columnas[1], columnas[2], columnas[3], columnas[4], columnas[5]])

    df.to_excel("testFinalxd.xlsx", sheet_name='Facturas')



def f(n):
    return n * n



add_data_excel(text)








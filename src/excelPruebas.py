import pandas as pd




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


listNIT.append("NItxs")
listNAutorizacion.append("2")
listNFactura.append("3")
listImporte.append("4")
listFecha.append("5")
listCodigoControl.append("6")



df = pd.DataFrame(data_factura, columns= [ columnas[0],columnas[1],columnas[2],columnas[3],columnas[4],columnas[5] ])


df.to_excel("testFinalxd.xlsx", sheet_name='Facturas')


print(data_factura)

print(df)

import cv2
import keyboard
import pandas as pd
from pyzbar.pyzbar import decode
import numpy as np

cap = cv2.VideoCapture(0)

listNIT = []
listNAutorizacion = []
listNFactura = []
listImporte = []
listFecha = []
listCodigoControl = []

data_factura = {

    'NIT': listNIT,
    'Numero Autorizacion': listNAutorizacion,
    'Numero Factura': listNFactura,
    'Importe': listImporte,
    'Fecha': listFecha,
    'Codigo Control': listCodigoControl,

}

columnas = ['NIT', 'Numero Autorizacion', 'Numero Factura', 'Importe', 'Fecha', 'Codigo Control']






def add_data_excel(string):
    lista_datos = string.rsplit("|")

    if len(listCodigoControl) == 0:

        print("LISta vacia")
        listNIT.append(lista_datos[0])
        listNAutorizacion.append(lista_datos[2])
        listNFactura.append(lista_datos[1])
        listImporte.append(lista_datos[4])
        listFecha.append(lista_datos[3])
        listCodigoControl.append(lista_datos[6])
        df = pd.DataFrame(data_factura,
                          columns=[columnas[0], columnas[1], columnas[2], columnas[3], columnas[4], columnas[5]])

        df.to_excel("Facturas_Qr_1.xlsx", sheet_name='Facturas')

    else:
        print("Else")

        if lista_datos[2] in listNAutorizacion:
            print("Factura Repetida")
        else:
                listNIT.append(lista_datos[0])
                listNAutorizacion.append(lista_datos[2])
                listNFactura.append(lista_datos[1])
                listImporte.append(lista_datos[4])
                listFecha.append(lista_datos[3])
                listCodigoControl.append(lista_datos[6])
                df = pd.DataFrame(data_factura,
                                  columns=[columnas[0], columnas[1], columnas[2], columnas[3], columnas[4],
                                           columnas[5]])

                df.to_excel("Facturas_Qr_4.xlsx", sheet_name='Facturas')




def get_qr_data(input_frame):
    try:
        return decode(input_frame)
    except:
        return []


def draw_polygon(frame_in, qrObj):
    if len(qrObj) == 0:
        return frame_in
    else:
        for obj in qrObj:
            text = obj.data.decode('utf-8')
            print(text)
            add_data_excel(text)
            pts = obj.polygon
            pts = np.array([pts], np.int32)
            pts = pts.reshape((4, 1, 2))
            cv2.polylines(frame_in, [pts], True, (255, 55, 5), 2)
            cv2.putText(frame_in, text, (50, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 200, 1), 2)

            # if keyboard.read_key() == "p":
            #    add_data_excel(text)

            return frame_in


title = "Reconocimiento Facturas QR"

while True:
    #  if keyboard.read_key() == "p":
    _, frame = cap.read()

    qr_obj = get_qr_data(frame)
    frame = draw_polygon(frame, qr_obj)

    cv2.imshow(title, frame)
    cv2.waitKey(1)

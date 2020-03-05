import csv
import os
from pathlib import Path
import shutil
import datetime

cedulas = []
with open("./assets/cedulas.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
    for row in reader:  
        cedulas.append(row)

rucs = []
with open("./assets/rucs.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        rucs.append(row)

class PageIndex:
    def __init__(self, myDriver):
        self.driver = myDriver

    def login(self,username,password):
        self.driver.find_element_by_id('txtLogin').send_keys(username)
        self.driver.find_element_by_id('txtClave').send_keys(password)
        self.driver.find_element_by_id('BLogin').click()

    def buscar_reporte_generico(self,id_report,x):
        self.driver.find_element_by_id('dtlFinal_rdbReporte_'+str(id_report)).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('txtNumeroDocumento').send_keys(cedulas[x])
        self.driver.find_element_by_id('btnConsultarDocumento').click()

    def buscar_reporte_generico_no_generico(self,x):
        self.driver.find_element_by_id('txtNumeroDocumentoSolicitante').send_keys(cedulas[x])
        self.driver.find_element_by_id('btnAceptar').click()
        self.take_screenshot("Reporte_Cheque",x)
        self.driver.find_element_by_id('imbNuevaConsulta').click()

    def take_screenshot(self,nombre_reporte,x):
        now = str(datetime.datetime.now())[:19]
        now = now.replace(":","_").replace(" ","_")
        ruta = 'screenshots/'
        ruta_reporte = os.path.join(ruta,nombre_reporte)
        cedula = str(cedulas[x])
        cedula = cedula.replace("[","_").replace("]","_").replace("'","")
        Path(ruta_reporte).mkdir(parents=True, exist_ok=True)
        self.driver.save_screenshot(ruta_reporte+cedula+now+'.png')
        shutil.move(ruta_reporte+cedula+now+'.png', ruta_reporte)

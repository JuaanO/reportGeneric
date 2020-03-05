from selenium import webdriver
import unittest
from pages.PageIndex import *
from pages.reportesTest import *
import HtmlTestRunner
from selenium.webdriver.common.by import By

EXE_PATH = r'.\assets\geckodriver.exe'

class Items(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=EXE_PATH)
        self.driver.get('https://172.23.141.88/Decida/Login.aspx')
        self.page_index = PageIndex(self.driver)
        self.page_test = reportesTest(self.driver)
        self.page_index.login('juan1','burocr')

    #VALE
    @unittest.skip("Aun se trabajan en la plantilla")
    def test_consulta_reporte_Cheque(self):
        self.page_test.Reporte_Cheque(2)
    #VALE
    #@unittest.skip("Aun se trabajan en la plantilla")
    def test_Reporte_Generico_Full(self):
        self.page_test.Reporte_Generico_Full(30)
    #VALE
    @unittest.skip("Aun se trabajan en la plantilla")
    def test_Reporte_Generico_Pichincha_Decida(self):
        self.page_test.Reporte_Generico_Pichincha_Decida(2)
    #NO VALE EL BOTON ATRAS 
    @unittest.skip("Aun se trabajan en la plantilla")
    def test_Reporte_Movistar(self):
        self.page_test.Reporte_Movistar(2)

    @unittest.skip("Aun se trabajan en la plantilla")
    def test_Reporte_Generico_Califica_Score_Produbanco(self):
        self.page_test.Reporte_Generico_Califica_Score_Produbanco(2)

    @unittest.skip("Aun se trabajan en la plantilla")
    def test_Reporte_Generico_Full_Gold(self):
        self.page_test.Reporte_Generico_Full_Gold(2)
    #OK, Se encuentra funcional. 
    @unittest.skip("Aun se trabajan en la plantilla")
    def test_Reporte_Generico_Jep_Decida(self):
        self.page_test.Reporte_Generico_Jep_Decida(2)

    def tearDown(self):        
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
    )

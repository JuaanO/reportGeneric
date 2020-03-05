import csv
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.PageIndex import *
import os
import sys
import unittest

class reportesTest:

    def __init__(self, myDriver):
        self.driver = myDriver

    def Reporte_Cheque(self,request):
        self.driver.set_window_size(800,1000)
        decision_xpath = '/html/body/form/div[2]/div[3]/div[5]/div/table[2]/tbody/tr[1]/td[2]/span'       
        self.page_index = PageIndex(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('dtlFinal_imbReporte_137').click()
        #self.page_index.buscar_reporte_generico_no_generico(137,x)
        for x in range(0, request):
            self.page_index.buscar_reporte_generico_no_generico(x)
            self.driver.implicitly_wait(10)

    def Reporte_Movistar(self,request):
        self.driver.set_window_size(800,1000)
        decision_xpath = '/html/body/form/div[2]/div[3]/div[5]/div/table[2]/tbody/tr[1]/td[2]/span'       
        self.page_index = PageIndex(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('dtlFinal_imbReporte_94').click()
        #self.page_index.buscar_reporte_generico_no_generico(137,x)
        for x in range(0, request):
            self.page_index.buscar_reporte_generico_no_generico(x)
            self.driver.implicitly_wait(10)
            self.page_index.take_screenshot("Reporte_Movistar",x)

    def Reporte_Generico_Full(self,request):
        self.driver.set_window_size(800,2800)
        cedula_xpath_full= '/html/body/form/div[2]/div[3]/div[4]/table[2]/tbody/tr[1]/td/table/tbody/tr/td[2]/span/span'
        cuota_estimada_xpath_full = '/html/body/form/div[2]/div[3]/div[9]/div[2]/table[3]/tbody/tr[1]/td[2]/span/span[1]'
        cuota_estimada_xpath_full1 = '/html/body/form/div[2]/div[3]/div[12]/div[2]/table[3]/tbody/tr[1]/td[2]/span/span[1]'
                                      /html/body/form/div[2]/div[3]/div[11]/div[2]/table[3]/tbody/tr[1]/td[2]/span/span
        self.page_index = PageIndex(self.driver)
        self.driver.implicitly_wait(10)
        for x in range(0, request):
            self.page_index.buscar_reporte_generico(9,x)
            self.driver.implicitly_wait(10)
            self.page_index.take_screenshot("Generico_Full",x)
            try:
                cedula_generico_full = self.driver.find_element_by_xpath(cedula_xpath_full).text
                cuota_estimada_full = self.driver.find_element_by_xpath(cuota_estimada_xpath_full).text
                if(cedula_generico_full != ""):
                    print(str(int(x+1))+"<strong>:  Identificacion Consultada: </strong>"+cedula_generico_full+" | <strong>Cuota Estimada Mensual: </strong>"+cuota_estimada_full+" | <strong>Resultado: </strong>"+cedula_generico_full+"<br>")
                else:
                    #decision1 = self.driver.find_element_by_xpath(decision_xpath1).text
                    print("Mal")
                    #print(str(int(x+1))+"<strong>:  Identificacion Consultada: </strong>"+decision1+" | <strong>Score: </strong>"+decision1+" | <strong>Resultado: </strong>"+decision1+"<br>")
            except NoSuchElementException:
                decision = ""
                if(decision != ""):
                    print("Iteracion: ",str(int(x+1)))
                    print("<strong>Correcta</strong><br>")
                    print("<strong>Score: </strong>"+decision+"<br>")
                else:
                    cuota_estimada_full1 = self.driver.find_element_by_xpath(cuota_estimada_xpath_full1).text
                    cedula_generico_full1 = self.driver.find_element_by_xpath(cedula_xpath_full).text
                    print(str(int(x+1))+"<strong>:  Identificacion Consultada: </strong>"+cedula_generico_full1+" | <strong>Cuota Estimada Mensual: </strong>"+cuota_estimada_full1+"$ | <strong>Resultado: </strong>"+cedula_generico_full1+"<br>")
                    x += 1
                    if x <= request:
                        continue
                    else:
                        assert False, "Test unitario, fallo. "
            finally:
                self.driver.find_element_by_id('HyperLink1').click()

    def Reporte_Generico_Pichincha_Decida(self,request):
        self.driver.set_window_size(800,2800)
        cedula_xpath_pichincha = '/html/body/form/div[2]/div[3]/div[2]/table[2]/tbody/tr[1]/td/table/tbody/tr/td[2]/span/span'
        cedula_xpath_pichincha1 = '/html/body/form/div[2]/div[3]/div[1]/table[2]/tbody/tr[1]/td/table/tbody/tr/td[2]/span/span'
        score_xpath_pichincha = '/html/body/form/div[2]/div[3]/div[4]/div/table[2]/tbody/tr[1]/td[2]/span'
        score_xpath_pichincha1 = '/html/body/form/div[2]/div[3]/div[3]/div/table[2]/tbody/tr[1]/td[2]/span'
        resultado_xpath_pichincha = '/html/body/form/div[2]/div[3]/div[4]/div/table[2]/tbody/tr[2]/td[2]/span'
        resultado_xpath_pichincha1 = '/html/body/form/div[2]/div[3]/div[3]/div/table[2]/tbody/tr[2]/td[2]/span'
        self.page_index = PageIndex(self.driver)
        self.driver.implicitly_wait(10)
        for x in range(0, request):
            self.page_index.buscar_reporte_generico(61,x)
            self.driver.implicitly_wait(10)
            self.page_index.take_screenshot("Pichincha_Decida",x)
            try:
                cedula_consultada_pichincha = self.driver.find_element_by_xpath(cedula_xpath_pichincha).text
                score_pichincha = self.driver.find_element_by_xpath(score_xpath_pichincha).text
                resultado_pichincha = self.driver.find_element_by_xpath(resultado_xpath_pichincha).text
                if(cedula_consultada_pichincha != "" and score_pichincha != "" and resultado_pichincha != ""):
                    print(str(int(x+1))+"<strong>:  Identificacion Consultada: </strong>"+cedula_consultada_pichincha+" | <strong>Score: </strong>"+score_pichincha+" | <strong>Resultado: </strong>"+resultado_pichincha+"<br>")
                else:
                    #decision1 = self.driver.find_element_by_xpath(decision_xpath1).text
                    print("Mal")
                    #print(str(int(x+1))+"<strong>:  Identificacion Consultada: </strong>"+decision1+" | <strong>Score: </strong>"+decision1+" | <strong>Resultado: </strong>"+decision1+"<br>")
            except NoSuchElementException:
                decision = ""
                if(decision != ""):
                    print("Iteracion: ",str(int(x+1)))
                    print("<strong>Correcta</strong><br>")
                    print("<strong>Score: </strong>"+decision+"<br>")
                else:
                    score_resultado_pichincha1 = self.driver.find_element_by_xpath(score_xpath_pichincha1).text
                    cedula_pichincha1 = self.driver.find_element_by_xpath(cedula_xpath_pichincha1).text
                    resultado_pichincha1 = self.driver.find_element_by_xpath(resultado_xpath_pichincha1).text
                    print(str(int(x+1))+"<strong>:  Identificacion Consultada: </strong>"+cedula_pichincha1+" | <strong>Score: </strong>"+score_resultado_pichincha1+" | <strong>Resultado: </strong>"+resultado_pichincha1+"<br>")
                    x += 1
                    if x <= request:
                        continue
                    else:
                        assert False, "Test unitario, fallo. "
            finally:
                self.driver.find_element_by_id('HyperLink1').click()

    def Reporte_Generico_Califica_Score_Produbanco(self,request):
        self.driver.set_window_size(800,2800)
        decision_xpath = '/html/body/form/div[2]/div[3]/div[2]/div[3]/table/tbody/tr/td[2]/span'       
        self.page_index = PageIndex(self.driver)
        self.driver.implicitly_wait(10)
        for x in range(0, request):
            self.page_index.buscar_reporte_generico(324,x)
            self.driver.implicitly_wait(10)
            self.page_index.take_screenshot("Califica_Score_Produbanco",x)
            decision = self.driver.find_element_by_xpath(decision_xpath).text
            print(decision)           
            self.driver.find_element_by_id('HyperLink1').click()
            self.driver.implicitly_wait(10)

    def Reporte_Generico_Full_Gold(self,request):
        self.driver.set_window_size(800,2800)
        decision_xpath = '/html/body/form/div[2]/div[3]/div[6]/div/div/table/tbody/tr[1]/td[2]/center/div/span'       
        self.page_index = PageIndex(self.driver)
        self.driver.implicitly_wait(10)
        for x in range(0, request):
            self.page_index.buscar_reporte_generico(38,x)
            self.driver.implicitly_wait(10)
            self.page_index.take_screenshot("Full_Gold",x)
            decision = self.driver.find_element_by_xpath(decision_xpath).text
            print(decision)           
            self.driver.find_element_by_id('HyperLink1').click()
            self.driver.implicitly_wait(10)

    def Reporte_Generico_Jep_Decida(self,request):
        self.driver.set_window_size(800,2800)
        decision_xpath1 = '/html/body/form/div[2]/div[3]/div[4]/div/table[2]/tbody/tr[1]/td[2]/span'
        decision_xpath = '/html/body/form/div[2]/div[3]/div[5]/div/table[2]/tbody/tr[1]/td[2]/span'
        cedula_xpath = '/html/body/form/div[2]/div[3]/div[2]/table[2]/tbody/tr[1]/td/table/tbody/tr/td[2]/span/span'
        cedula_xpath1 = '/html/body/form/div[2]/div[3]/div[1]/table[2]/tbody/tr[1]/td/table/tbody/tr/td[2]/span/span'
        resultado_xpath = '/html/body/form/div[2]/div[3]/div[5]/div/table[2]/tbody/tr[2]/td[2]/span'
        resultado_xpath1 = '/html/body/form/div[2]/div[3]/div[4]/div/table[2]/tbody/tr[2]/td[2]/span'
        self.page_index = PageIndex(self.driver)
        self.driver.implicitly_wait(10)
        for x in range(0, request):
            self.page_index.buscar_reporte_generico(62,x)
            self.driver.implicitly_wait(10)
            self.page_index.take_screenshot("Jep_Decida",x)
            try:
                decision = self.driver.find_element_by_xpath(decision_xpath).text
                cedula_consultada = self.driver.find_element_by_xpath(cedula_xpath).text
                resultado = self.driver.find_element_by_xpath(resultado_xpath).text
                if(decision != "" and cedula_consultada != "" and resultado != ""):
                    print(str(int(x+1))+"<strong>:  Identificacion Consultada: </strong>"+cedula_consultada+" | <strong>Score: </strong>"+decision+" | <strong>Resultado: </strong>"+resultado+"<br>")
                else:
                    decision1 = self.driver.find_element_by_xpath(decision_xpath1).text
                    print(str(int(x+1))+"<strong>:  Identificacion Consultada: </strong>"+decision1+" | <strong>Score: </strong>"+decision1+" | <strong>Resultado: </strong>"+decision1+"<br>")
            except NoSuchElementException:
                decision = ""
                if(decision != ""):
                    print("Iteracion: ",str(int(x+1)))
                    print("<strong>Correcta</strong><br>")
                    print("<strong>Score: </strong>"+decision+"<br>")
                else:
                    decision1 = self.driver.find_element_by_xpath(decision_xpath1).text
                    cedula_consultada1 = self.driver.find_element_by_xpath(cedula_xpath1).text
                    resultado1 = self.driver.find_element_by_xpath(resultado_xpath1).text
                    print(str(int(x+1))+"<strong>:  Identificacion Consultada: </strong>"+cedula_consultada1+" | <strong>Score: </strong>"+decision1+" | <strong>Resultado: </strong>"+resultado1+"<br>")
                    x += 1
                    if x <= request:
                        continue
                    else:
                        assert False, "Test unitario, fallo. "
            finally:
                self.driver.find_element_by_id('HyperLink1').click()

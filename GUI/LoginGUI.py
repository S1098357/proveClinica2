from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Amministrazione.Calendario import Calendario
from Amministrazione.Segreteria import Segreteria
from Amministrazione.Sistema import Sistema
from Servizio.Cliente import Cliente
from Servizio.Dottore import Dottore


class LoginGUI(QDialog):

    def __init__(self):
        super(LoginGUI, self).__init__()
        loadUi("LoginGUI.ui", self)
        self.segreteria = Segreteria()
        self.cliente = Cliente()
        self.calendario = Calendario()
        self.sistema = Sistema(self.calendario.Dottori)
        self.dottore=Dottore()
        self.accesso=None
        self.username=None
        self.password=None
        self.risposta=None

    def login(self):
        if self.segreteria.leggiClienti() == False:
            self.cliente.registrazione(False)
        while self.accesso==None:
            self.GUI()
            if self.risposta == True:
                if self.username != None and self.password != None:
                    if self.username == 'segreteria' and self.password == 'seg':
                        #accesso = 'segreteria'
                        self.segreteria.menuSegreteria()
                    for dottore in self.calendario.Dottori:
                        if self.username == dottore.nomeCognome and self.password == 'doc':
                            #accesso = 'dottore'
                            self.dottore=dottore
                            self.dottore.dottorePre(self.sistema.listaPrenotazioni, self.segreteria.listaClienti)
                            self.dottore.menuDottore()
                    for cliente in self.segreteria.listaClienti:
                        if self.username == cliente.nomeCognome and self.password == cliente.password:
                            #accesso = 'cliente'
                            self.cliente=cliente
                            self.cliente.menuCliente()
            else:
                #accesso = True
                self.cliente.registrazione()

    def GUI(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.commandLinkButton.clicked.connect(self.registazione)

    def avanti(self):
        self.risposta=True
        self.username=self.lineEdit.text()
        self.password=self.lineEdit_2.text()
        self.close()

    def registrazione(self):
        self.risposta = False
        self.username = None
        self.password = None
        self.close()


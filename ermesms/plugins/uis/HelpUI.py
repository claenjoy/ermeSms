# -*- coding: utf-8 -*-

import sys

from ermesms.CodingManager import CodingManager
from ermesms.plugins.Sender import Sender
from ermesms.plugins.UI import UI

class HelpUI(UI):
    """Interfaccia utente quando-tutto-il-resto-fallisce: una spiegazione
    dell'uso del programma."""

    def isAvailable(self):
        """Questa interfaccia è sempre utilizzabile."""
        return True

    def getPriority(self):
        """Priorità minima."""
        return 0

    def run(self):
        """Avvia questa interfaccia."""
        print "ermeSms by Thomas Bertani, https://github.com/sylarpowa/ermeSms\n"
        print "USO:"
        print "MODALITA' INTERATTIVA: MoioSMS\n"
        print "MODALITA' A LINEA DI COMANDO: "
        print "MoioSMS numero \"testo\" (invia un SMS a un numero)"
        print "MoioSMS nome \"testo\" (invia un SMS a un numero in rubrica)"
        print "MoioSMS -a nome numero (aggiunge un numero in rubrica)"
        print "MoioSMS -m (mostra la rubrica)\n"
        print "Per usare un sito in particolare, aggiungere uno dei parametri"
        print "seguenti:"
        for i in Sender.getPlugins():
            print i
        print "\nPer usare un proxy, aggiungere -p indirizzo:porta in coda"
        print "(usare -p no per disabilitare)"
        print "Address book, password and settings are into the file .ermesms/config.ini."
        print "Comments/Suggests/Bugs: sylar@anche.no"

    def showFatalException(self, message):
        """Questo metodo viene richiamato nel caso in cui venga catturata
        un'eccezione non gestita nel programma principale."""
        sys.stdout.write('\a')#Beep
        sys.stdout.flush()
        print CodingManager.getInstance().encodeStdout(message)

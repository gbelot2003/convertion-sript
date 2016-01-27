import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Llamamos al builder
builder = Gtk.Builder()
builder.add_from_file("converson.glade")

# Instancia de Widgets
txtFrecuencia = builder.get_object("txtFrecuencia")
rbBandaC = builder.get_object("rbBandaC")
rbBandaL = builder.get_object("rbBandaL")
rbBandaIF = builder.get_object("rbBandaIF")
lblBandaC = builder.get_object("lblBandaC")
lblBandaL = builder.get_object("lblBandaL")
lblBandaIF = builder.get_object("lblBandaIF")

# Metodo Handler de cierre de ventana
def window1_destroy(self, data=None):
    print("Quit with cancel")
    Gtk.main_quit()

# Conversor de Banda
def conversor(banda, valor=None):
    if valor != None:
        banda = float(banda)
        total = valor - banda
        total = round(total, 2)
        total = str(total)
        return total
    else:
        banda = float(banda)
        banda = round(banda, 2)
        banda = str(banda)
        return banda

# Metodo Handler de ejecución de Boton
def button_convert(self, data=None):
    try:
        val = float(txtFrecuencia.get_text())
        txtFrecuencia.set_text(str(val))
    except ValueError:
        txtFrecuencia.set_text('Solo Numeros')
        lblBandaC.set_text('')
        lblBandaL.set_text('')
        lblBandaIF.set_text('')
        pass

    if txtFrecuencia.get_text() == False:
        pass

    elif rbBandaC.get_active():

        bandaC = conversor(txtFrecuencia.get_text())
        lblBandaC.set_text(bandaC)

        bandaL = conversor(txtFrecuencia.get_text(), 7375)
        lblBandaL.set_text(bandaL)

        bandaIF = conversor(txtFrecuencia.get_text(), 6335)
        lblBandaIF.set_text(bandaIF)

    elif rbBandaL.get_active():
        bandaC = conversor(txtFrecuencia.get_text(), 7375)
        lblBandaC.set_text(bandaC)

        bandaL = conversor(txtFrecuencia.get_text())
        lblBandaL.set_text(bandaL)

        bandaIF = conversor(txtFrecuencia.get_text(), 1040)
        lblBandaIF.set_text(bandaIF)

    elif rbBandaIF.get_active():
        bandaC = conversor(txtFrecuencia.get_text(), 6335)
        lblBandaC.set_text(bandaC)

        bandaL = conversor(txtFrecuencia.get_text(), 1040)
        lblBandaL.set_text(bandaL)

        bandaIF = conversor(txtFrecuencia.get_text())
        lblBandaIF.set_text(bandaIF)

# Instanciación de Handlers
handlers = {
    "on_window1_destroy": window1_destroy,
    "button_convert": button_convert
}
builder.connect_signals(handlers)

#Construcción de Ventana
win = builder.get_object("window1")
win.show_all()
Gtk.main()

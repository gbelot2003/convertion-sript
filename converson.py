from gi.repository import Gtk

# Llamamos al builder
builder = Gtk.Builder()
builder.add_from_file("converson.glade")

txtFrecuencia = builder.get_object("txtFrecuencia")

rbBandaC = builder.get_object("rbBandaC")
rbBandaL = builder.get_object("rbBandaL")
rbBandaIF = builder.get_object("rbBandaIF")

lblBandaC = builder.get_object("lblBandaC")
lblBandaL = builder.get_object("lblBandaL")
lblBandaIF = builder.get_object("lblBandaIF")

def window1_destroy(self, data=None):
    print("Quit with cancel")
    Gtk.main_quit()

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

        bandaC = txtFrecuencia.get_text()
        bandaC = float(bandaC)
        bandaC = round(bandaC, 2)
        bandaC = str(bandaC)
        lblBandaC.set_text(bandaC)

        bandaL = txtFrecuencia.get_text()
        bandaL = float(bandaL)
        totalL = 7375 - bandaL
        totalL = round(totalL, 2)
        totalL = str(totalL)
        lblBandaL.set_text(totalL)

        bandaIF = txtFrecuencia.get_text()
        bandaIF = float(bandaIF)
        bandaIF = 6335 - bandaIF
        totalIF = round(bandaIF, 2)
        totalIF = str(totalIF)
        lblBandaIF.set_text(totalIF)

    elif rbBandaL.get_active():
        bandaC = txtFrecuencia.get_text()
        bandaC = float(bandaC)
        TotalC = 7375 - bandaC
        TotalC = round(TotalC, 2)
        TotalC = str(TotalC)
        lblBandaC.set_text(TotalC)

        bandaL = txtFrecuencia.get_text()
        bandaL = float(bandaL)
        bandaL = round(bandaL, 2)
        bandaL = str(bandaL)
        lblBandaL.set_text(bandaL)

        bandaIF = txtFrecuencia.get_text()
        bandaIF = float(bandaIF)
        bandaIF = 1040 - bandaIF
        totalIF = round(bandaIF, 2)
        totalIF = str(totalIF)
        lblBandaIF.set_text(totalIF)

    elif rbBandaIF.get_active():
        bandaC = txtFrecuencia.get_text()
        bandaC = float(bandaC)
        TotalC = 6335 - bandaC
        TotalC = round(TotalC, 2)
        TotalC = str(TotalC)
        lblBandaC.set_text(TotalC)

        bandaL = txtFrecuencia.get_text()
        bandaL = float(bandaL)
        totalL = 1040 - bandaL
        totalL = round(totalL, 2)
        totalL = str(totalL)
        lblBandaL.set_text(totalL)

        bandaIF = txtFrecuencia.get_text()
        bandaIF = float(bandaIF)
        bandaIF = round(bandaIF, 2)
        bandaIF = str(bandaIF)
        lblBandaIF.set_text(bandaIF)

handlers = {
    "on_window1_destroy": window1_destroy,
    "button_convert": button_convert
}

builder.connect_signals(handlers)


win = builder.get_object("window1")
win.show_all()
Gtk.main()

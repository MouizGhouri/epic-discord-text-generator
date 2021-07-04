import tkinter
import pyperclip

alphabets = 'abcdefghijklmnopqrstuvwxyz'

def generate () :

	final_text = list (message_text.get ())

	for n, i in enumerate (final_text) :
		if i.lower () in list (alphabets) :
			final_text [n] = ':regional_indicator_' + i.lower () + ':'

	pyperclip.copy ('‎'.join (final_text))

window = tkinter.Tk()
window.title ("Discord Text Generator")

message_text = tkinter.StringVar ()

tkinter.Label (window, text = "Message :").grid (row = 0, column = 0, padx=11, pady=10)
tkinter.Entry (window, textvariable = message_text).grid (row = 0, column = 1, padx=11, pady=10)
tkinter.Button (window, text = "Copy", command = generate).grid (row = 0, column = 3, padx=11, pady=10)

window.mainloop ()

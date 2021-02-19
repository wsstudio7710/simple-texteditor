from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter import filedialog
import os
from tkinter.messagebox import askokcancel


class EditorSederhana (Frame):
    def __init__(self, parent=None, file=None):
        Frame.__init__(self, parent)
        self.frm = Frame(parent)
        self.frm.pack(fill=X)
        self.layoutKolom = Frame(root)
        self.buatNamefile()
        parent.title('text editor')
        self.buatTombol()
        self.kolomTeksUtama()
        self.indeks = 1.0
        self.path = ''

    def buatTombol(self):
        Button(self.frm, text='Open', relief='flat',
               command=self.openFile).pack(side=LEFT)
        Button(self.frm, text='Save', relief='flat',
               command=self.perintahSimpan).pack(side=LEFT)
        Button(self.frm, text='Exit', relief='flat',
               command=self.perintahKeluar).pack(side=LEFT)

    def kolomTeksUtama(self):
        scroll = Scrollbar(self)
        kolomTeks = Text(self, relief=SUNKEN)
        scroll.config(command=kolomTeks.yview)
        kolomTeks.config(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        kolomTeks.pack(side=LEFT, expand=YES, fill=BOTH)
        self.kolomTeks = kolomTeks
        self.pack(expand=YES, fill=BOTH)

    def perintahSimpan(self):
        print(self.path)
        if self.path:
            alltext = self.gettext()
            open(self.path, 'w').write(alltext)
            messagebox.showinfo('Berhasil', 'Selamat File telah tersimpan ! ')
        else:
            tipeFile = [('Text file', '*.txt'), ('Python file',
                                                 '*asdf.py'), ('All files', '.*')]
            filename = asksaveasfilename(filetypes=(
                tipeFile), initialfile=self.kolomJudul.get())
            if filename:
                alltext = self.gettext()
                open(filename, 'w').write(alltext)
                self.path = filename

    def perintahKeluar(self):
        ans = askokcancel('Exit', "anda yakin ingin keluar?")
        if ans:
            Frame.quit(self)

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
            self.kolomTeks.delete('1.0', END)
            self.kolomTeks.insert('1.0', text)
            self.kolomTeks.mark_set(INSERT, '1.0')
            self.kolomTeks.focus()

    def gettext(self):
        return self.kolomTeks.get('1.0', END+'-1c')

    def buatNamefile(self):
        self.layoutKolom.pack(fill=BOTH, expand=1, padx=17, pady=5)
        judul = Label(self.layoutKolom, text="Nama file : ")
        judul.pack(side="left")
        self.kolomJudul = Entry(self.layoutKolom)
        self.kolomJudul.pack(side="left")

    def openFile(self):
        extensiFile = [('All files', '*'), ('Text files',
                                            '*.txt'), ('Python files', '*.py')]
        open = filedialog.askopenfilename(filetypes=extensiFile)
        if open != '':
            text = self.readFile(open)
            if text:
                self.path = open
                nama = os.path.basename(open)
                self.kolomJudul.delete(0, END)
                self.kolomJudul.insert(END, nama)
                self.kolomTeks.delete('0.1', END)
                self.kolomTeks.insert(END, text)

    def readFile(self, filename):
        try:
            f = open(filename, "r")
            text = f.read()
            return text
        except:
            messagebox.showerror("Error!!")
            return None


root = Tk()
EditorSederhana(root)
mainloop()

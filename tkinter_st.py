from googletrans import Translator
import tkinter as tk

class EnJpTrans():
    def __init__(self, EnSrc):
        self.EnSrc = EnSrc

    def EnJpTransExe(self):
        ts = Translator()
        JpTrans = ts.translate(self.EnSrc, src="en", dest="ja")
        return JpTrans.text

def TransExe():
    getEnSrc = EnInputSrc.get(1.0, tk.END)

    ET = EnJpTrans(getEnSrc)
    JpSrc = ET.EnJpTransExe()
    DisplayJp.insert(1.0, JpSrc)

def ClearExe():
    EnInputSrc.delete(1.0, tk.END)
    DisplayJp.delete(1.0, tk.END)

if __name__ == "__main__":
    baseGround = tk.Tk()
    baseGround.geometry('500x500')
    baseGround.title('English translation app')

    EnLabel = tk.Label(baseGround, text="English")
    EnLabel.pack()

    EnInputSrc = tk.Text(width=60, height=10)
    EnInputSrc.pack()

    JpTransBtn = tk.Button(
        baseGround,
        text = "English -> Japanese",
        command = TransExe
    ).pack()

    ClearBtn = tk.Button(
        baseGround,
        text = "Clear",
        command = ClearExe
    ).pack()

    JpLabel = tk.Label(baseGround, text="Japanese")
    JpLabel.pack()

    DisplayJp = tk.Text(width=60, height=10)
    DisplayJp.pack()

    var = tk.IntVar()
    def getRdoVar():
#        selectNo = var.get()
#        if selectNo = 0
        print(var.get())

    JpEnRdo = tk.Radiobutton(
        value=0,
        variable=var,
        text='Jp -> En',
        command=getRdoVar)

    JpEnRdo.pack()

    EnJpRdo = tk.Radiobutton(
        value=1,
        variable=var,
        text='Jp -> En',
        command=getRdoVar)

    EnJpRdo.pack()

    baseGround.mainloop()
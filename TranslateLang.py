from googletrans import Translator
import tkinter as tk

#Languageを変換するオブジェクト。日本語<->英語に翻訳可能。
class langTrans():
    def __init__(self, langSrc):
        self.langSrc = langSrc

    def EnJpTransExe(self):
        ts = Translator()
        JpTrans = ts.translate(self.langSrc, src="en", dest="ja")
        return JpTrans.text

    def JpEnTransExe(self):
        ts = Translator()
        EnTrans = ts.translate(self.langSrc, src="ja", dest="en")
        return EnTrans.text

#入力した値を削除するオブジェクト。
class clearSrc():
    def clearExe(self):
        inputLangSrc.delete(1.0, tk.END)
        outputLangSrc.delete(1.0, tk.END)

    def partClearExe(self):
        outputLangSrc.delete(1.0, tk.END)

#ラジオボタンで選択した内容で翻訳を実行するオブジェクト。
#翻訳に必要な変数も保持できる。
class selectTrans():
    def __init__(self):
        self.selectNo = 0
        self.langSrc = ""
        self.exeCounter = 0

    def getRdoVar(self):
        self.selectNo = var.get()

    def getInputSrc(self):
        CS = clearSrc()
        self.langSrc = inputLangSrc.get(1.0, tk.END)
        #入力値がない場合に翻訳実行するとExceptionが起きるため回避策。
        if len(self.langSrc) >= 2:
            LT = langTrans(self.langSrc)
            #選択した翻訳を実行する
            if self.selectNo == 0 and not self.selectNo == 1:

                #一度でも翻訳を実行したらText内を翻訳前に削除する
                if self.exeCounter >= 1:
                    CS.partClearExe()
                else:
                    pass

                EnTrans = LT.JpEnTransExe()
                #一度でも翻訳実行したら翻訳した結果が残っているため
                #それを翻訳時に削除できるように記録しておく。
                self.exeCounter += 1
                outputLangSrc.insert(1.0, EnTrans)

            elif self.selectNo == 1:
                if self.exeCounter >= 1:
                    CS.partClearExe()
                else:
                    pass

                JpTrans = LT.EnJpTransExe()
                self.exeCounter += 1
                outputLangSrc.insert(1.0, JpTrans)
        else:
            pass

if __name__ == "__main__":
    baseGround = tk.Tk()
    baseGround.geometry('500x500')
    baseGround.title('English, Japanese translation app')

    #オブジェクトの生成
    ST = selectTrans()
    CS = clearSrc()

    #radioボタン生成
    var = tk.IntVar()
    JpEnRdo = tk.Radiobutton(
        value=0,
        variable=var,
        text='Japanese -> English',
        command=ST.getRdoVar)
    JpEnRdo.pack()

    EnJpRdo = tk.Radiobutton(
        value=1,
        variable=var,
        text='English -> Jpapanese',
        command=ST.getRdoVar)
    EnJpRdo.pack()

    #入力form
    InputFormLabel = tk.Label(baseGround, text = "--- Input form ---").pack()
    inputLangSrc = tk.Text(width=60, height=10)
    inputLangSrc.pack()

    #翻訳ボタン
    langTransBtn = tk.Button(
        baseGround,
        text = "Translate",
        command = ST.getInputSrc)
    langTransBtn.pack()

    #clearボタン
    clearBtn = tk.Button(
        baseGround,
        text = "Clear",
        command = CS.clearExe)
    clearBtn.pack()

    #翻訳後のTextが記述される
    ResultLabel = tk.Label(baseGround, text = "--- Translation Results ---").pack()
    outputLangSrc = tk.Text(width=60, height=10)
    outputLangSrc.pack()

    #tkinterを起動状態にする
    baseGround.mainloop()

#設計
#radioボタンを選択
#Jpを選択したら日本語を入力する
#変換ボタンを押したら英語が表示される
#Clearをクリックしたら内容が削除される
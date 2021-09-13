import time
import os
import sys
from typing import Counter
from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageFilter

root = Tk()
root.title('tkinter frame')
frameLeft = Frame(root)
frameRight = Frame(root)
frameLeft.pack(padx=10, pady=10, side=LEFT)
frameRight.pack(padx=10, pady=10, side=RIGHT,
                expand=YES, fill=BOTH)


class CommonInfo():
    def __init__(self):
        self.winW = root.winfo_screenwidth()
        self.winH = root.winfo_screenheight()
        self.rootW = round(self.winW / 1.25)
        self.rootH = round(self.winH / 2)
        self.ipadx = self.padx = self.rootW / 30
        self.ipady = self.pady = self.rootH / 100
        self.relief = 'solid'
        self.font = 'Helvetica %d bold' % round(self.winW * 0.006)
        self.centerStr = '%dx%d+%d+%d' % (self.rootW, self.rootH,
                                          (self.winW-self.rootW) / 2, (self.winH-self.rootH) / 2)
        self.CRTPATH = os.path.abspath(sys.path[0])
        self.INPUT_PATH = self.CRTPATH + '\input'
        self.OUTPUT_PATH = self.CRTPATH + '\output'
        self.ALL = os.listdir(self.CRTPATH)
        self.WEBP_PRE = '.webp'
        self.NotWebp = ['blur', '.svg', '.webp']
        self.BLUR_PRE = '-blur.'
        self.NotBlur = ['@2x', '.webp', '.svg', '-blur.']
        self.labelInit = 'Not set yet...'
        self.pathfile = 'pathrecoding.txt'
        self.inputvar = StringVar()
        self.outputvar = StringVar()
        self.imgNumb = int(0)
        self.quality = int(95)
        self.thumbsize = int(3)
        self.thumbquality = int(20)
        self.maxsize = int(1 * 1024 * 1024)
        self.compressquality = int(80)
        self.acc = 1
        self.sizeAcc = 0.8
        self.compressfolder = 'compressed'

        self.CreateBtn('Convert to .webp', self.ConvertToWebp)
        self.CreateBtn('Generate blur imgs', self.GenerateBlur)
        self.CreateBtn('Harmless Compress', self.HarmlessCompress)
        self.CreateBtn('Little Compress', self.SlightlyCompress)
        self.CreateBtn('Delete All .webp', self.DeleteWebpImgs)
        self.CreateBtn('Delete All blur imgs', self.DeleteBlurImgs)
        # self.CreateBtn('Empty This Input', self.DeleteInputImgs)
        # self.CreateBtn('Empty This Output', self.DeleteOutputImgs)
        self.CreateBtn('Select Input path', self.SetInputPath)
        self.CreateLable(self.labelInit, 'input')
        # self.CreateBtn('Select Output path', self.SetOutputPath)
        # self.CreateLable(self.labelInit, 'output')
        self.CreateBtn('Exit', root.quit)
        self.CreateText()
        self.GetPathFile()
        self.LogInsert('-----Ready-----')

    def RecodePath(self, t):
        self.LogInsert('-----Path Record-----')
        with open(self.pathfile, 'w') as f:
            f.write(t)

    def GetPathFile(self):
        self.LogInsert('-----Get Path-----')
        if os.path.exists(self.pathfile):
            self.LogInsert('-----PathFile Found-----')
            with open(self.pathfile, 'r') as f:
                t = f.read()
                self.inputvar.set(t)
                self.LogInsert(self.inputvar.get())
        else:
            self.LogInsert('-----PathFile not Found-----')

    def ResetNumb(self):
        self.imgNumb = int(0)

    def CreateBtn(self, t, c):
        Button(frameLeft, text=t, font=self.font, relief=self.relief, command=c).pack(
            ipadx=self.ipadx, ipady=self.ipady, padx=self.padx, pady=self.pady)

    def CreateLable(self, t, b):
        if b == 'input':
            self.inputvar.set(t)
            Label(frameLeft, textvariable=self.inputvar).pack()
        if b == 'output':
            self.outputvar.set(t)
            Label(frameLeft, textvariable=self.outputvar).pack()

    def CreateText(self):
        self.logText = Text(frameRight)
        self.logText.pack(side=TOP, expand=YES, fill=BOTH)

    def LogInsert(self, t):
        self.logText.insert('end', t+'\n')
        self.logText.see('end')

    def ConvertToWebp(self):
        self.LogInsert('-----To Webp-----')
        self.ResetNumb()
        inputAll = os.walk(self.INPUT_PATH) if self.inputvar.get(
        ) == self.labelInit else os.walk(os.path.abspath(self.inputvar.get()))
        for r, dirs_name, fns in inputAll:
            for i in fns:
                if not any(n in i for n in self.NotWebp):
                    self.imgNumb += 1
                    inputName = os.path.join(r, i)
                    nameOnly = os.path.splitext(i)[0]
                    outputName = nameOnly + self.WEBP_PRE
                    inputPath = os.path.join(r, inputName)
                    outputPath = os.path.join(r, outputName)
                    img = Image.open(inputPath)
                    img.save(outputPath, quality=self.quality)
                    self.LogInsert('Generated .webp: ' + outputPath)
        self.LogInsert('Total generated ' + '%d' %
                       self.imgNumb + ' .webp images.')

    def GenerateBlur(self):
        self.LogInsert('-----Generate blur imgs-----')
        self.ResetNumb()
        inputAll = os.walk(self.INPUT_PATH) if self.inputvar.get(
        ) == self.labelInit else os.walk(os.path.abspath(self.inputvar.get()))
        for r, dirs_name, fns in inputAll:
            for i in fns:
                if not any(n in i for n in self.NotBlur):
                    self.imgNumb += 1
                    inputName = os.path.join(r, i)
                    nameOnly = os.path.splitext(i)[0]
                    imgType = os.path.splitext(i)[1]
                    outputName = nameOnly + self.BLUR_PRE + imgType[1:]
                    inputPath = os.path.join(r, inputName)
                    outputPath = os.path.join(r, outputName)
                    img = Image.open(inputPath)
                    w, h = img.size
                    img.thumbnail((w / self.thumbsize, h / self.thumbsize))
                    img.save(outputPath, quality=self.thumbquality)
                    self.LogInsert('Generated blur img: ' + outputPath)
        self.LogInsert('Total generated ' + '%d' %
                       self.imgNumb + ' blur images.')

    def HarmlessCompress(self):
        self.LogInsert('-----Compressing images-----')
        self.ResetNumb()
        inputAll = os.walk(self.INPUT_PATH) if self.inputvar.get(
        ) == self.labelInit else os.walk(os.path.abspath(self.inputvar.get()))
        for r, dname, fns in inputAll:
            for f in fns:
                if not any(n in f for n in self.NotWebp):
                    eachInput = os.path.join(r, f)
                    nameOnly = os.path.splitext(f)[0]
                    imgType = os.path.splitext(f)[1]
                    outputName = nameOnly + '.' + imgType[1:]
                    outputPath = os.path.join(r, self.compressfolder)
                    if(os.path.getsize(eachInput) > self.maxsize):
                        if not self.compressfolder in eachInput:
                            self.imgNumb += 1
                            if not os.path.exists(outputPath):
                                os.mkdir(outputPath)
                            outputFile = os.path.join(outputPath, outputName)

                            img = Image.open(eachInput)
                            w, h = img.size
                            outimg = img.resize(
                                (int(w * 1), int(h * 1)), Image.ANTIALIAS)
                            outimg.save(
                                outputFile, optimize=True, quality=95)
                            outimg = Image.open(outputFile)
                            self.LogInsert(
                                'Compressed image: ' + str(int(len(outimg.fp.read()) // 1024)) + 'KB - ' + eachInput)
        self.LogInsert('Total Compressed ' + '%d' %
                       self.imgNumb + ' images.')

    def SlightlyCompress(self):
        self.LogInsert('-----Compressing a little bit-----')
        self.ResetNumb()
        inputAll = os.walk(self.INPUT_PATH) if self.inputvar.get(
        ) == self.labelInit else os.walk(os.path.abspath(self.inputvar.get()))
        for r, dname, fns in inputAll:
            for f in fns:
                if not any(n in f for n in self.NotWebp):
                    eachInput = os.path.join(r, f)
                    nameOnly = os.path.splitext(f)[0]
                    imgType = os.path.splitext(f)[1]
                    outputName = nameOnly + '.' + imgType[1:]
                    outputPath = os.path.join(r, self.compressfolder)
                    if(os.path.getsize(eachInput) > self.maxsize):
                        if not self.compressfolder in eachInput:
                            self.imgNumb += 1
                            if not os.path.exists(outputPath):
                                os.mkdir(outputPath)
                            outputFile = os.path.join(outputPath, outputName)

                            img = Image.open(eachInput)
                            w, h = img.size
                            outimg = img.resize(
                                (int(w * self.sizeAcc), int(h * self.sizeAcc)), Image.ANTIALIAS)
                            outimg.save(
                                outputFile, optimize=True, quality=self.compressquality)
                            outimg = Image.open(outputFile)
                            self.LogInsert(
                                'Little Compressed: ' + str(int(len(outimg.fp.read()) // 1024)) + 'KB - ' + eachInput)
        self.LogInsert('Total little Compressed ' + '%d' %
                       self.imgNumb + ' images.')

    def DeleteWebpImgs(self):
        self.LogInsert('-----Delete Webp-----')
        self.ResetNumb()
        inputAll = os.walk(self.INPUT_PATH) if self.inputvar.get(
        ) == self.labelInit else os.walk(os.path.abspath(self.inputvar.get()))
        for r, dname, fns in inputAll:
            for f in fns:
                if self.WEBP_PRE in f:
                    self.imgNumb += 1
                    eachInput = os.path.join(r, f)
                    os.remove(eachInput)
                    self.LogInsert('Deleted .webp: ' + eachInput)
        self.LogInsert('Total deleted ' + '%d' %
                       self.imgNumb + ' .webp images.')

    def DeleteBlurImgs(self):
        self.ResetNumb()
        inputAll = os.walk(self.INPUT_PATH) if self.inputvar.get(
        ) == self.labelInit else os.walk(os.path.abspath(self.inputvar.get()))
        for r, dname, fns in inputAll:
            for f in fns:
                if self.BLUR_PRE in f:
                    self.imgNumb += 1
                    eachInput = os.path.join(r, f)
                    os.remove(eachInput)
                    self.LogInsert('Deleted blur img: ' + eachInput)
        self.LogInsert('Total deleted ' + '%d' %
                       self.imgNumb + ' blur images.')

    # def DeleteInputImgs(self):
    #     self.LogInsert('-----Empty Input-----')
    #     self.ResetNumb()
    #     inputAll = os.walk(self.INPUT_PATH) if self.inputvar.get(
    #     ) == self.labelInit else os.walk(os.path.abspath(self.inputvar.get()))
    #     for r, dname, fns in inputAll:
    #         for f in fns:
    #             self.imgNumb += 1
    #             eachInput = os.path.join(r, f)
    #             os.remove(eachInput)
    #             self.LogInsert('Deleted img: ' + eachInput)
    #     self.LogInsert('Total deleted ' + '%d' % self.imgNumb + ' images.')

    # def DeleteOutputImgs(self):
    #     self.LogInsert('-----Set input path-----')
    #     self.ResetNumb()
    #     inputAll = os.walk(self.OUTPUT_PATH) if self.outputvar.get(
    #     ) == self.labelInit else os.walk(os.path.abspath(self.outputvar.get()))
    #     for r, dname, fns in inputAll:
    #         for f in fns:
    #             self.imgNumb += 1
    #             eachOutput = os.path.join(r, f)
    #             # os.remove(eachOutput)
    #             print('Deleted img: ' + eachOutput)
    #     print('Total deleted ' + '%d' % self.imgNumb + ' images.')

    def SetInputPath(self):
        self.LogInsert('-----Set input path-----')
        path = tkinter.filedialog.askdirectory()
        self.inputvar.set(path)
        self.RecodePath(self.inputvar.get())
        self.LogInsert(self.inputvar.get())

    # def SetOutputPath(self):
    #     self.LogInsert('-----Set output path-----')
    #     path = tkinter.filedialog.askdirectory()
    #     self.outputvar.set(path)
    #     print(self.outputvar.get())


if __name__ == '__main__':
    cmn = CommonInfo()
    root.geometry(cmn.centerStr)
    root.mainloop()

# 生成 AEM 版的 html css js
# 多线程
# 删掉打印的path
# 添加耗费的时间
# 添加进度条

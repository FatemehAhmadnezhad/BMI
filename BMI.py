from tkinter import *

bmi =0
def bmi_calculator():
    global bmi, height, weight
    try:
        H = int(height.get())
        W = int(weight.get())
        if W<= 0 or H<=0:
            bmi_result.config(text="BMI: Height and Weight \n cannot be zero or negative! \n Please Try Again ",font=('',10), fg='red')
        else:
            if hChoice.get() == 'cm':
                H *= 0.01
            elif hChoice.get() == 'inch':
                H *= 0.0254

            if wChoice.get() == 'g':
                W *= 0.001
            elif wChoice.get() == 'pound':
                W *= 0.4535
            bmi = W/(H**2)
            if bmi<18.5:
                bmi_result.config(text="BMI: {} \n LOW WEIGHT ".format(bmi), fg='cyan')
            elif 18.5<=bmi<24.5:
                bmi_result.config(text="BMI: {} \n NORMAL ".format(bmi), fg='green')
            elif 24.5<=bmi<29.9:
                bmi_result.config(text="BMI: {} \n OVER WEIGHT ".format(bmi), fg='#FFA500')
            else:
                bmi_result.config(text="BMI: {} \n VERY HIGH WEIGHT ".format(bmi), fg='#FF00FF')
    except ValueError:
        e=bmi_result.config(text="Enter Numbers!!! ",font=('',10), fg='red')
    except TypeError:
        bmi_result.config(text=" Enter Numbers!!! ",font=('',10), fg='red')
    except:
        bmi_result.config(text=" Somthing went wrong! ",font=('',10), fg='red')
    finally:
      weight.delete(0,'end')  
      height.delete(0,'end')  

Window = Tk()
Window.title('BMI Calculator')
Label(Window, text='BMI Calculator', font=('', 20), foreground='blue').pack()
Window.geometry("600x500")
Window.minsize(600, 500)
Window.maxsize(1080, 1080)
Label(Window, text="Weight",font=('Times', 10)).pack()
weight = Entry(Window,width=40)
weight.pack(pady=10)
Label(Window, text="Height",font=("Times", 12)).pack()
height = Entry(Window,width=40)
height.pack(pady=10)
hMode = [('m', 'm'), ('cm', 'cm'), ('inch', 'inch')]
wMode = [('Kg', 'Kg'), ('g', 'g'), ('pound', 'pound')]
hChoice = StringVar()
hChoice.set('m')
wChoice = StringVar()
wChoice.set('Kg')
for i, j in hMode:
    Radiobutton(Window, text=i,font=("Times", 12), variable=hChoice, value=j).pack(side='left')
for i, j in wMode:
    Radiobutton(Window, text=i,font=("Times", 12), variable=wChoice, value=j).pack(side='right')
bmi_result = Label(Window, text='BMI: ---  ',font=("Times", 12))
bmi_result.pack(pady=10)
Button(Window, text='ENTER', font=("Times", 12), command=bmi_calculator,
       bg='black', fg='white', width=40, bd=10,).pack(pady=10)
Window.mainloop()
























    




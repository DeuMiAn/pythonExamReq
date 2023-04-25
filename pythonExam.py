import tkinter as tk
from math import factorial

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Display
        self.display_frame = tk.Frame(master, bg="white")
        self.display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.equation = tk.StringVar()
        self.result = tk.StringVar()

        self.equation_label = tk.Label(self.display_frame, textvariable=self.equation, anchor="e", padx=5, pady=5, font=("Arial", 14))
        self.equation_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.result_label = tk.Label(self.display_frame, textvariable=self.result, anchor="e", padx=5, pady=5, font=("Arial", 20))
        self.result_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side=tk.TOP, padx=5, pady=5)

        self.buttons = [
            "반올림","소수점2","소수점1","소수점0",
            "CUT", "CE", "C", "(BS)",
            "n!", "X^y", "mod", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "x/-", "0", ".", "="
        ]

        # Button creation
        self.button_dict = {}
        row, col = 0, 0
        for button in self.buttons:
            self.button_dict[button] = tk.Button(self.button_frame, text=button, width=5, height=2, font=("Arial", 12), command=lambda x=button: self.button_click(x))
            self.button_dict[button].grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, button):
        if button == "=":
            try:
                result = str(eval(self.equation.get()))
                decimal_index = result.find('.')
                if decimal_index > 0:
                    decimal_places = len(result) - decimal_index - 1
                    if decimal_places > 2:
                        result = str(round(float(result), 2))
                self.result.set(result)
            except:
                self.result.set("Error")
        elif button == "C":
            self.equation.set("")
            self.result.set("")
        elif button == "CE":
            self.equation.set(self.equation.get()[:-1])
        elif button == "(BS)":
            self.equation.set(self.equation.get()[:-1])
        elif button == "CUT":
            result = float(self.equation.get())
            decimal_place = self.decimal_place.get() # 소수점 자릿수 가져오기
            if decimal_place > 0:
                result = int(result * (10 ** decimal_place)) / (10 ** decimal_place) # 소수점 자릿수까지 곱하고 나누기
            else:
                result = int(result) # 소수점 자릿수가 0이면 정수 부분만 반환
            self.result.set(result)
        elif button == "x!":
            try:
                result = str(factorial(int(self.equation.get())))
                self.equation.set(result)
            except:
                self.result.set("Error")
        elif button == "X^y":
            try:
                result = str(round(float(self.equation.get()) ** 0.5, 2))
                self.result.set(result)
            except:
                self.result.set("Error")
        elif button == "^":
            self.equation.set(self.equation.get() + "**")
        elif button == "반올림":
            # 소수점 이하 자리수 지정
            precision = int(self.precision.get())
            # 입력받은 수식에서 '=' 제거
            equation = self.equation.get().replace("=", "")
            # 결과 계산
            try:
                result = eval(equation)
                # 입력된 수식이 실수인 경우에만 반올림 적용
                if isinstance(result, float):
                    # 반올림 적용
                    rounded = round(result, precision+1)
                    # 소수점 이하 자리수만큼 잘라냄
                    formatted = "{:.{}f}".format(rounded, precision)
                    # 결과값 표시
                    self.result.set(formatted)
            except Exception as e:
                # 계산 불가능한 경우 에러 메시지 표시
                self.result.set("Error")
        elif button == "소수점2":
            try:
                result = eval(self.equation.get())
                self.result.set(round(result, 2))
                self.equation.set(str(result) + " ≈ " + str(round(result, 2)))
            except:
                self.result.set("Error")
                
        elif button == "소수점1":
            try:
                result = eval(self.equation.get())
                self.result.set(round(result, 1))
                self.equation.set(str(result) + " ≈ " + str(round(result, 1)))
            except:
                self.result.set("Error")
                
        elif button == "소수점0":
            try:
                result = eval(self.equation.get())
                self.result.set(round(result, 0))
                self.equation.set(str(result) + " ≈ " + str(round(result, 0)))
            except:
                self.result.set("Error")
        else:
            self.equation.set(self.equation.get() + button)


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
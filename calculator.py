import calendar
import datetime

import dateutil.relativedelta as relativedelta
import dateutil.rrule as rrule
from tkinter import Tk, W, Label, IntVar, Checkbutton, StringVar, N, Button
from tkinter.ttk import Frame, Entry, Combobox

WEEK_DAYS = ('Mon', 'Tue', "Wed", 'Thu', 'Fri', "Sat", 'Sun')
schedule = dict()
result = None
result2 = None
price = None
month = None
month_mapping = dict()


class Calculator(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Calculator")
        self.config(padding=10)
        global result
        result = StringVar()
        global result2
        result2 = StringVar()
        global price
        price = StringVar(value='300')
        today = datetime.datetime.now()
        months = []
        for i in range(4, -5, -1):
            dt = today - relativedelta.relativedelta(months=i)
            month_name = calendar.month_name[dt.month]
            months.append(month_name)
            month_mapping[month_name] = dt
        global month
        month = StringVar(value=calendar.month_name[today.month])
        cmb = Combobox(self, values=months, textvariable=month)
        cmb.grid(row=0, column=0, sticky=W)
        label = Label(self, text="Set lesson price:")
        label.grid(row=1, column=0, sticky=W)
        ent = Entry(self, textvariable=price)
        ent.grid(row=2, columnspan=1)
        frame = Frame(self)
        frame.grid(row=3, column=0, sticky=W, pady=20)
        row, column = 0, 0
        for i, weekday in enumerate(WEEK_DAYS):
            if i <= 3:
                row = i
            else:
                row = i - 4
                column = 1
            schedule[i] = IntVar()
            chb = Checkbutton(frame, text=weekday, variable=schedule[i])
            chb.grid(row=row, column=column, sticky=W + N)
        lbl = Label(self, textvariable=result, pady=5)
        lbl.grid(row=4, column=0, sticky=W)
        lbl = Label(self, textvariable=result2, pady=5)
        lbl.grid(row=5, column=0, sticky=W)
        frame2 = Frame(self)
        frame2.grid(row=6, column=0, sticky=W)
        button_calc = Button(frame2, text='Calculate', command=calculate_price, pady=10, width=7)
        button_calc.grid(row=0, column=0, sticky=W)
        button_calc.config()
        button_quit = Button(frame2, text='Close', command=self.quit, pady=10, width=7)
        button_quit.grid(row=0, column=1, sticky=W)
        self.pack()


def calculate_price():
    dt = month_mapping.get(month.get())
    before = datetime.datetime(dt.year, dt.month, 1)
    dt_range = calendar.monthrange(dt.year, dt.month)
    after = datetime.datetime(dt.year, dt.month, dt_range[1])
    count = 0
    for weekday, value in schedule.items():
        if value.get():
            rr = rrule.rrule(rrule.WEEKLY, byweekday=weekday, dtstart=before)
            days = rr.between(before, after, inc=True)
            count += len(days)
    if result and price:
        result.set(f"Lessons: {count}")
        result2.set(f"Total of {month.get()}: {count * int(price.get())}")


if __name__ == '__main__':
    root = Tk()
    app = Calculator()
    root.mainloop()

from tkinter import *
from pandastable import Table, TableModel
import pandas as pd
import os


class TestApp(Frame):

        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('600x400+200+100')
            self.main.title('Table app')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            # df = TableModel.getSampleData() # here is the sample data order by the library
            # here you should change the file location
            df = pd.read_csv('/Users/yangyong/Documents/文稿/HKUST/MSDM5051/proj1/sort_exercises_with_data/TDCS_M06A_20190830_080000.csv', header= None)
            # df = df
            self.table = pt = Table(f, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
            pt.show()
            return

app = TestApp()
#launch the app
app.mainloop()

# vacation_gui.py
import tkinter as tk
from tkinter import ttk
import pandas as pd

class VacationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dentist Vacation Planner")

        # Label at the top
        self.label = ttk.Label(master, text="Recommended Days for Vacation", font=("Arial", 16))
        self.label.pack(pady=10)

        # Setup the Treeview to show data
        self.tree = ttk.Treeview(master, columns=('Date', 'Predicted Attendance'))
        self.tree.heading('#0', text='Index')
        self.tree.column('#0', width=50, anchor='center')
        self.tree.heading('Date', text='Date')
        self.tree.column('Date', width=150, anchor='center')
        self.tree.heading('Predicted Attendance', text='Predicted Attendance')
        self.tree.column('Predicted Attendance', width=150, anchor='center')
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        # Load and display the data
        self.load_data("forecast.csv")

        # Close button
        self.close_button = ttk.Button(master, text="Close", command=master.quit)
        self.close_button.pack(pady=20)

    def load_data(self, filename):
        """
        Load forecast data from a CSV file and display in the GUI.
        Args:
            filename (str): The path to the CSV file containing the forecast data.
        """
        df = pd.read_csv(filename)
        # Assuming 'yhat_lower' as a threshold to identify low attendance days
        threshold = df['yhat_lower'].quantile(0.10)  # adjust threshold as needed
        for index, row in df.iterrows():
            if row['yhat_lower'] <= threshold:
                self.tree.insert("", 'end', text=str(index), values=(row['ds'], round(row['yhat'], 2)))

def main():
    root = tk.Tk()
    app = VacationGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()

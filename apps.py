import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class ExcelAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Data Analyzer")
        
        # Variables
        self.df = None
        self.sort_column = tk.StringVar()

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Load Excel File
        load_button = tk.Button(self.root, text="Load Excel File", command=self.load_file)
        load_button.pack(pady=10)

        # Dropdown for selecting column to sort
        self.column_label = tk.Label(self.root, text="Select column to sort:")
        self.column_label.pack(pady=5)

        self.column_dropdown = ttk.Combobox(self.root, textvariable=self.sort_column)
        self.column_dropdown.pack(pady=5)

        # Sort Button
        sort_button = tk.Button(self.root, text="Sort Data", command=self.sort_data)
        sort_button.pack(pady=10)

        # Analyze Data Button
        analyze_button = tk.Button(self.root, text="Analyze Data", command=self.analyze_data)
        analyze_button.pack(pady=10)

        # Treeview for displaying data
        self.tree = ttk.Treeview(self.root, show='headings')
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

        # Scrollbars
        self.scrollbar_y = ttk.Scrollbar(self.root, orient='vertical', command=self.tree.yview)
        self.scrollbar_x = ttk.Scrollbar(self.root, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)

        self.scrollbar_y.pack(side='right', fill='y')
        self.scrollbar_x.pack(side='bottom', fill='x')

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
        if file_path:
            try:
                self.df = pd.read_excel(file_path)
                self.column_dropdown['values'] = self.df.columns.tolist()
                self.display_data(self.df)
                messagebox.showinfo("Success", "File loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")

    def display_data(self, data):
        # Clear existing data in the treeview
        self.tree.delete(*self.tree.get_children())
        
        # Set columns
        self.tree["columns"] = list(data.columns)
        for column in data.columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, anchor='center')

        # Insert data into treeview
        for index, row in data.iterrows():
            self.tree.insert("", "end", values=list(row))

    def sort_data(self):
        if self.df is not None and self.sort_column.get():
            try:
                sorted_df = self.df.sort_values(by=self.sort_column.get())
                self.display_data(sorted_df)
                messagebox.showinfo("Success", "Data sorted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to sort data: {e}")
        else:
            messagebox.showwarning("Warning", "Please load a file and select a column to sort.")

    def analyze_data(self):
        if self.df is not None:
            summary = self.df.describe(include='all')
            summary_str = summary.to_string()
            self.display_data(summary)
            messagebox.showinfo("Analysis Complete", summary_str)
        else:
            messagebox.showwarning("Warning", "Please load a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelAnalyzerApp(root)
    root.mainloop()

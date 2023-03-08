import tkinter as tk
from tkinter import filedialog, messagebox

import config
import main
class PlottingApp:
    def __init__(self, master):
        self.master = master
        master.title("Plotting App")

        self.file_type_var = tk.StringVar()
        self.file_path_var = tk.StringVar()
        self.plot_type_var = tk.StringVar()
        self.x_label_var = tk.StringVar()
        self.y_label_var = tk.StringVar()
        self.column_name_var = tk.StringVar()
        self.labels_var = tk.StringVar()
        self.x_col_name_var = tk.StringVar()
        self.y_col_name_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # File Type Label
        file_type_label = tk.Label(self.master, text="File Type:")
        file_type_label.grid(row=0, column=0)

        # File Type Radio Buttons
        file_type_radio_frame = tk.Frame(self.master)
        file_type_radio_frame.grid(row=0, column=1)

        local_file_radio = tk.Radiobutton(file_type_radio_frame, text="Local File", variable=self.file_type_var,
                                           value="local", command=self.show_file_dialog)
        local_file_radio.pack()

        online_file_radio = tk.Radiobutton(file_type_radio_frame, text="Online File",
                                            variable=self.file_type_var, value="online", command=self.show_url_entry)
        online_file_radio.pack()

        # File Path Label and Entry
        file_path_label = tk.Label(self.master, text="File Path:")
        file_path_label.grid(row=1, column=0)

        file_path_entry = tk.Entry(self.master, textvariable=self.file_path_var, width=50)
        file_path_entry.grid(row=1, column=1)

        # Plot Type Label and Dropdown
        plot_type_label = tk.Label(self.master, text="Plot Type:")
        plot_type_label.grid(row=2, column=0)

        plot_type_dropdown = tk.OptionMenu(self.master, self.plot_type_var, *config.PLOT_TYPES)
        plot_type_dropdown.grid(row=2, column=1)

        # X Label Label and Entry
        x_label_label = tk.Label(self.master, text="X Label:")
        x_label_label.grid(row=3, column=0)

        x_label_entry = tk.Entry(self.master, textvariable=self.x_label_var, width=50)
        x_label_entry.grid(row=3, column=1)

        # Y Label Label and Entry
        y_label_label = tk.Label(self.master, text="Y Label:")
        y_label_label.grid(row=4, column=0)

        y_label_entry = tk.Entry(self.master, textvariable=self.y_label_var, width=50)
        y_label_entry.grid(row=4, column=1)

        # Column Name Label and Entry
        column_name_label = tk.Label(self.master, text="Column Name:")
        column_name_label.grid(row=5, column=0)

        column_name_entry = tk.Entry(self.master, textvariable=self.column_name_var, width=50)
        column_name_entry.grid(row=5, column=1)

        # Labels Label and Entry
        labels_label = tk.Label(self.master, text="Labels:")
        labels_label.grid(row=6, column=0)

        labels_entry = tk.Entry(self.master, textvariable=self.labels_var, width=50)
        labels_entry.grid(row=6, column=1)

        # X Column Name Label and Entry
        x_col_name_label = tk.Label(self.master, text="X Column Name:")
              self.x_col_name_entry.grid(row=7, column=1)

        self.y_col_name_label = tk.Label(master, text="Y Column Name:")
        self.y_col_name_label.grid(row=8, column=0)

        self.y_col_name_entry = tk.Entry(master, textvariable=self.y_col_name_var, width=50)
        self.y_col_name_entry.grid(row=8, column=1)

        self.plot_button = tk.Button(master, text="Plot", command=self.plot)
        self.plot_button.grid(row=9, column=0, columnspan=2, pady=10)

    def show_file_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        self.file_path_var.set(file_path)

    def show_url_entry(self):
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, "https://")
        self.file_path_entry.config(state="normal")

    def plot(self):
        file_type = self.file_type_var.get()
        file_path = self.file_path_var.get()
        plot_type = self.plot_type_var.get()
        x_label = self.x_label_var.get()
        y_label = self.y_label_var.get()
        column_name = self.column_name_var.get()
        labels = self.labels_var.get()
        x_col_name = self.x_col_name_var.get()
        y_col_name = self.y_col_name_var.get()

        # Check if file path is provided
        if not file_path:
            messagebox.showerror("Error", "Please select a file or provide a URL.")
            return

        # Check if column name is provided
        if not column_name:
            messagebox.showerror("Error", "Please enter a column name.")
            return

        # Convert labels string to list
        if labels:
            labels = labels.split(",")

        # Call the main function to plot the graph
        main.plot_graph(file_type, file_path, plot_type, x_label, y_label, column_name, labels, x_col_name, y_col_name)

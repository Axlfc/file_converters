import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from data.audio import audio_extensions


class WavToMp3ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Converter")

        self.file_extension_var = tk.StringVar(value="WAV")  # Default to WAV extension
        self.file_extension_label = tk.Label(root, text="Select File Extension:")
        self.file_extension_label.pack()

        self.file_extension_dropdown = tk.OptionMenu(root, self.file_extension_var, *audio_extensions.keys(),
                                                     command=self.update_labels)
        self.file_extension_dropdown.pack()

        self.mode_var = tk.StringVar(value="single")  # Default to single mode
        self.mode_label = tk.Label(root, text="Select Conversion Mode:")
        self.mode_label.pack()

        self.single_radio = tk.Radiobutton(root, text="Single", variable=self.mode_var, value="single",
                                           command=self.update_labels)
        self.single_radio.pack()

        self.batch_radio = tk.Radiobutton(root, text="Batch", variable=self.mode_var, value="batch",
                                          command=self.update_labels)
        self.batch_radio.pack()

        self.input_label_text = tk.StringVar()
        self.input_label_text.set("Input WAV File:")

        self.input_path_label = tk.Label(root, textvariable=self.input_label_text)
        self.input_path_label.pack()

        self.input_path_frame = tk.Frame(root)
        self.input_path_entry = tk.Entry(self.input_path_frame, width=50)
        self.input_path_entry.pack(side=tk.LEFT)

        self.browse_input_button = tk.Button(self.input_path_frame, text="Browse", command=self.browse_input)
        self.browse_input_button.pack(side=tk.RIGHT)

        self.input_path_frame.pack()

        self.exclude_var = tk.StringVar(value="MP3")  # Default to MP3 for exclude
        self.exclude_label = tk.Label(root, text=f"Convert to:")
        self.exclude_label.pack()

        self.exclude_options = [format for format in audio_extensions.keys() if format != self.exclude_var.get()]
        self.exclude_dropdown = tk.OptionMenu(root, self.exclude_var, *self.exclude_options)
        self.exclude_dropdown.pack()

        self.output_label_text = tk.StringVar()
        self.output_label_text.set("Output MP3 File/Folder:")

        self.output_path_label = tk.Label(root, textvariable=self.output_label_text)
        self.output_path_label.pack()

        self.output_path_frame = tk.Frame(root)
        self.output_path_entry = tk.Entry(self.output_path_frame, width=50)
        self.output_path_entry.pack(side=tk.LEFT)

        self.browse_output_button = tk.Button(self.output_path_frame, text="Browse", command=self.browse_output)
        self.browse_output_button.pack(side=tk.RIGHT)

        self.output_path_frame.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_file)
        self.convert_button.pack()

    def update_labels(self, *args):
        extension = self.file_extension_var.get()
        exclude = self.exclude_var.get()

        # Update options for the exclude dropdown based on the selected extension
        self.exclude_options = [format for format in audio_extensions.keys() if format != exclude]
        self.exclude_var.set(self.exclude_options[0])  # Set the first option as default

        mode = self.mode_var.get()

        if mode == "single":
            self.input_label_text.set(f"Input {extension} File:")
            self.output_label_text.set(f"Output {exclude} File:")
            self.exclude_label.config(text=f"Convert to {exclude}:")
        else:
            self.input_label_text.set("Input Folder:")
            self.output_label_text.set("Output Folder:")
            self.exclude_label.config(text=f"Convert to {exclude}:")

    def browse_input(self):
        mode = self.mode_var.get()
        extension = self.file_extension_var.get()

        if mode == "batch":
            selected_path = filedialog.askdirectory()
        else:
            selected_path = filedialog.askopenfilename(
                filetypes=[(f"{extension} Files", f"*{audio_extensions[extension]}")])

        self.input_path_entry.delete(0, tk.END)
        self.input_path_entry.insert(0, selected_path)

    def browse_output(self):
        selected_path = filedialog.askdirectory()
        self.output_path_entry.delete(0, tk.END)
        self.output_path_entry.insert(0, selected_path)

    def convert_file(self):
        mode = self.mode_var.get()
        extension = self.file_extension_var.get()
        input_path = self.input_path_entry.get()
        output_path = self.output_path_entry.get()

        if input_path:
            try:
                exclude_format = self.exclude_var.get()
                exclude_extension = audio_extensions[exclude_format]

                if mode == "single":
                    exclude_option = f"--convert-to={exclude_extension}={input_path}"
                    pass
                    messagebox.showinfo("Conversion Complete",
                                        f"{extension} to {exclude_format} conversion successful!")
                elif mode == "batch":
                    if not output_path:
                        output_path = os.path.join(input_path, f"converted_{exclude_format.lower()}")
                        messagebox.showwarning("Warning",
                                               f"No output path provided. A folder named 'converted_{exclude_format.lower()}' will be created.")
                    pass
                    messagebox.showinfo("Batch Conversion Complete",
                                        f"Batch {extension} to {exclude_format} conversion successful!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showerror("Error", "Please provide input path.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WavToMp3ConverterApp(root)
    root.mainloop()

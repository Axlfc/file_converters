import os
import tkinter as tk
from tkinter import filedialog, messagebox
from data.audio import audio_extensions
from tkinter import ttk


class WavToMp3ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio File Converter")

        self.file_name = ""  # Initialize an empty file name

        self.previous_extension = "wav"

        self.file_extension_var = tk.StringVar(value="wav")  # Default to wav extension
        self.file_extension_label = tk.Label(root, text="Select File Extension:")
        self.file_extension_label.pack()

        self.file_extension_dropdown = tk.OptionMenu(
            root, self.file_extension_var, *audio_extensions, command=self.update_labels
        )
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

        self.exclude_var = tk.StringVar(value="mp3")
        self.exclude_label = tk.Label(root, text=f"Convert to MP3:")
        self.exclude_label.pack()

        self.exclude_options = audio_extensions.keys()
        self.exclude_dropdown = tk.OptionMenu(root, self.exclude_var, *self.exclude_options, command=self.update_labels)
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

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_wav)
        self.convert_button.pack()

        style = ttk.Style()
        style.configure("green.Horizontal.TProgressbar", background="green")
        self.progress_bar_value = 0
        self.progress_bar = ttk.Progressbar(self.root, style="green.Horizontal.TProgressbar", orient="horizontal", mode="determinate")
        self.progress_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=0, pady=0)

    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.root.update_idletasks()

    def update_labels(self, *args):
        mode = self.mode_var.get()
        extension = self.file_extension_var.get()
        exclude = self.exclude_var.get().upper()

        if extension != self.previous_extension:  # Check if extension has changed
            self.input_path_entry.delete(0, tk.END)  # Clear the input path entry

        self.previous_extension = extension  # Update the previous_extension

        if mode == "single":
            print("SINGLE EXCLUDE:", exclude)
            self.input_label_text.set(f"Input {extension.upper()} File:")
            self.output_label_text.set(f"Output {exclude} File/Folder:")
            self.exclude_label.config(text=f"Convert to {exclude}:")
        else:
            print("BATCH EXCLUDE:", exclude)
            self.input_label_text.set("Input Folder:")
            self.output_label_text.set("Output Folder:")
            self.exclude_label.config(text=f"Convert to {exclude}:")

    def browse_input(self):
        mode = self.mode_var.get()
        extension = self.file_extension_var.get()

        if mode == "batch":
            selected_path = filedialog.askdirectory()
        else:
            selected_path = filedialog.askopenfilename(filetypes=[(f"{extension.upper()} Files", f"*.{extension}")])

        self.input_path_entry.delete(0, tk.END)
        self.input_path_entry.insert(0, selected_path)

    def browse_output(self):
        selected_path = filedialog.askdirectory()
        self.output_path_entry.delete(0, tk.END)
        self.output_path_entry.insert(0, selected_path)

    def convert_to_mp3(self, input_path, output_path, progress_callback=None):
        # Convert audio to MP3 using FFmpeg
        if progress_callback:
            progress_callback(self.progress_bar_value)
        os.system(f'ffmpeg -y -i "{input_path}" "{output_path}"')
        if progress_callback:
            progress_callback(100)

    def convert_wav(self):
        mode = self.mode_var.get()
        extension = self.file_extension_var.get()
        input_path = self.input_path_entry.get()
        output_path = self.output_path_entry.get()

        if input_path:
            try:
                if extension == self.exclude_var.get():
                    messagebox.showerror("Error", "Input and output file extensions cannot be the same.")
                    return

                if mode == "single":
                    self.progress_bar_value = 0
                    self.update_progress_bar(0)

                    if not os.path.isfile(input_path):
                        messagebox.showerror("Error", "Input must be a valid file in single mode.")
                        return

                    if not output_path:
                        output_path = os.path.splitext(input_path)[0] + f".{self.exclude_var.get()}"
                    elif os.path.isdir(output_path):
                        output_path = os.path.join(output_path, os.path.splitext(os.path.basename(input_path))[
                            0] + f".{self.exclude_var.get()}")

                    self.progress_bar_value = 50
                    self.convert_to_mp3(input_path, output_path, progress_callback=self.update_progress_bar)
                    messagebox.showinfo("Conversion Complete", "Conversion successful!")
                elif mode == "batch":
                    self.progress_bar_value = 0
                    self.update_progress_bar(0)
                    if not output_path:
                        output_path = os.path.join(input_path, "converted_mp3")
                    elif os.path.splitext(output_path)[1]:
                        messagebox.showerror("Error", "For batch conversion, output path cannot have a file extension. Please provide a directory path.")
                        return

                    if not os.path.exists(output_path):
                        os.makedirs(output_path)

                    files_to_convert = [file for file in os.listdir(input_path) if
                                        file.lower().endswith(f".{extension}")]
                    total_files = len(files_to_convert)
                    progress_increment = round(1 / total_files, 2)  # Calculate the progress increment

                    completed_files = 0

                    for root, dirs, files in os.walk(input_path):
                        for file in files:
                            if file.lower().endswith(f".{extension}"):
                                input_file_path = os.path.join(root, file)
                                output_file_path = os.path.join(output_path, file)
                                output_file_path = os.path.splitext(output_file_path)[0] + f".{self.exclude_var.get()}"
                                self.convert_to_mp3(input_file_path, output_file_path, progress_callback=self.update_progress_bar)
                                completed_files += 1
                                progress_value = completed_files * progress_increment * 100
                                print("PROGRESS INCREMENT VALUE =", progress_value)
                                self.progress_bar_value = int(progress_value + progress_increment)
                                print("PROGRESS BAR SELF VALUE=", self.progress_bar_value)
                                self.update_progress_bar(self.progress_bar_value)
                    self.update_progress_bar(100)
                    messagebox.showinfo("Batch Conversion Complete", "Batch conversion successful!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showerror("Error", "Please provide input path.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WavToMp3ConverterApp(root)
    root.mainloop()

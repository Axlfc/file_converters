import os
import tkinter as tk
from tkinter import filedialog, messagebox
from data.audio import audio_extensions
from data.video import video_extensions
from tkinter import ttk
import yt_dlp as yt


def get_playlist_title(url):
    info = yt.YoutubeDL().extract_info(url, download=False)
    return info.get('title', 'unknown_playlist')


def convert_to_mp3(input_path, output_path):
    # Convert audio to MP3 using FFmpeg
    os.system(f'ffmpeg -y -i "{input_path}" "{output_path}"')


def video_options(format, output_directory):
    return {
        'format': format,
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
    }


def download_video(url, output_directory=".", format="mp4"):
    with yt.YoutubeDL(video_options(format, output_directory)) as ydl:
        ydl.download([url])


def audio_options(codec, output_directory):
    return {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
    }


def download_audio(url, output_directory=".", codec="wav"):
    with yt.YoutubeDL(audio_options(codec, output_directory)) as ydl:
        ydl.download([url])


def video_playlist_options(codec, output_directory):
    return {
        'yes_playlist': True,
        'format': codec,
        'outtmpl': f'{output_directory}/%(playlist_title)s/%(title)s.%(ext)s',
    }


def download_video_playlist(url, output_directory="."):
    with yt.YoutubeDL(video_playlist_options("mp4", output_directory)) as ydl:
        ydl.download([url])


def audio_playlist_options(codec, output_directory):
    return {
        'yes_playlist': True,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_directory}/%(playlist_title)s/%(title)s.%(ext)s',
    }


def download_audio_playlist(url, output_directory=".", codec="wav"):
    with yt.YoutubeDL(audio_playlist_options(codec, output_directory)) as ydl:
        ydl.download([url])


class VideoDownloadApp:
    def download_progress_hook(self, d):
        if d['status'] == 'downloading':
            if 'downloading item' in d['filename']:
                progress_info = d['filename'].split('of')
                if len(progress_info) == 2:
                    item_number = int(progress_info[0].split()[-1])
                    total_items = int(progress_info[1].split()[-1])
                    total_progress = (item_number / total_items) * 100
                    self.update_progress_bar(total_progress)
                    self.update_progress()  # Update the progress variable

    def download_video_action(self):
        url = self.input_path_entry.get()
        if url:
            output_directory = self.output_path_entry.get()  # Get the selected output directory
            if not output_directory:
                output_directory = "."

            if self.mode_var.get() == "single":
                if self.audio_only_var.get():
                    if self.mp3_var.get():
                        download_audio(url, output_directory, "mp3")
                        return
                    download_audio(url, output_directory)
                else:
                    download_video(url, output_directory)
            else:
                if self.audio_only_var.get():
                    if self.mp3_var.get():
                        download_audio_playlist(url, output_directory, "mp3")
                        return
                    download_audio_playlist(url, output_directory)
                else:
                    download_video_playlist(url, output_directory)

            self.update_progress_bar(100)
            self.update_progress()  # Update the progress variable
        else:
            messagebox.showerror("Error", "Please provide a valid URL.")

    def __init__(self, root):
        self.root = root
        self.root.title("URL Video downloader")

        self.input_label_text = tk.StringVar()
        self.input_label_text.set("Input URL:")

        self.input_path_label = tk.Label(root, textvariable=self.input_label_text)
        self.input_path_label.pack()

        self.input_path_frame = tk.Frame(root)
        self.input_path_entry = tk.Entry(self.input_path_frame, width=50)
        self.input_path_entry.pack(side=tk.LEFT)
        self.input_path_frame.pack()

        self.previous_extension = "wav"

        self.file_extension_var = tk.StringVar(value="mp4")

        self.mode_var = tk.StringVar(value="single")  # Default to single mode
        self.mode_label = tk.Label(root, text="Select Download Mode:")
        self.mode_label.pack()

        self.single_radio = tk.Radiobutton(root, text="Single", variable=self.mode_var, value="single")
        self.single_radio.pack()

        self.batch_radio = tk.Radiobutton(root, text="Playlist", variable=self.mode_var, value="batch")
        self.batch_radio.pack()

        self.output_label_text = tk.StringVar()
        self.output_label_text.set("Output Folder:")

        self.output_path_label = tk.Label(root, textvariable=self.output_label_text)
        self.output_path_label.pack()

        self.output_path_frame = tk.Frame(root)
        self.output_path_entry = tk.Entry(self.output_path_frame, width=50)
        self.output_path_entry.pack(side=tk.LEFT)

        self.browse_output_button = tk.Button(self.output_path_frame, text="Browse", command=self.browse_output)
        self.browse_output_button.pack(side=tk.RIGHT)

        self.output_path_frame.pack()

        self.audio_only_var = tk.BooleanVar()
        self.audio_only_checkbox = tk.Checkbutton(root, text="Audio Only", variable=self.audio_only_var,
                                                  command=self.toggle_mp3_checkbox)
        self.audio_only_checkbox.pack()

        self.mp3_var = tk.BooleanVar()
        self.mp3_checkbox = tk.Checkbutton(root, text="Convert to MP3", variable=self.mp3_var,
                                           state=tk.DISABLED)  # Disabled by default
        # Hide the MP3 checkbox by default
        self.mp3_checkbox.pack_forget()

        self.convert_button = tk.Button(root, text="Download", command=self.download_video_action)
        self.convert_button.pack()

        style = ttk.Style()
        style.configure("green.Horizontal.TProgressbar", background="green")
        self.progress_bar_value = 0
        self.progress_bar = ttk.Progressbar(self.root, style="green.Horizontal.TProgressbar", orient="horizontal", mode="determinate")
        self.progress_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=0, pady=0)

        self.total_files = 0  # Initialize the total number of files
        self.completed_files = 0  # Initialize the number of completed files

    def toggle_mp3_checkbox(self):
        if self.audio_only_var.get():
            self.mp3_checkbox.pack()  # Show the MP3 checkbox when Audio Only is selected
            self.mp3_checkbox.config(state=tk.NORMAL)  # Enable the MP3 checkbox
        else:
            self.mp3_checkbox.pack_forget()  # Hide the MP3 checkbox when Audio Only is unselected
            self.mp3_var.set(False)  # Uncheck the MP3 checkbox
            self.mp3_checkbox.config(state=tk.DISABLED)  # Disable the MP3 checkbox

    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.root.update_idletasks()

    def update_progress(self):
        if self.total_files == 0:
            return 0  # Avoid division by zero

        progress_percentage = (self.completed_files / self.total_files) * 100
        return progress_percentage

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


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoDownloadApp(root)
    root.mainloop()

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


def video_options(format, output_directory):
    return {
        'format': format,
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
    }


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


def video_playlist_options(codec, output_directory):
    return {
        'yes_playlist': True,
        'format': codec,
        'outtmpl': f'{output_directory}/%(playlist_title)s/%(title)s.%(ext)s',
    }


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


def download_video(url, output_directory=".", format="mp4"):
    with yt.YoutubeDL(video_options(format, output_directory)) as ydl:
        ydl.download([url])


def download_audio(url, output_directory=".", codec="wav"):
    with yt.YoutubeDL(audio_options(codec, output_directory)) as ydl:
        ydl.download([url])


def download_video_playlist(url, output_directory="."):
    with yt.YoutubeDL(video_playlist_options("mp4", output_directory)) as ydl:
        ydl.download([url])


def download_audio_playlist(url, output_directory=".", codec="wav"):
    with yt.YoutubeDL(audio_playlist_options(codec, output_directory)) as ydl:
        ydl.download([url])


class VideoDownloadApp:
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
        else:
            messagebox.showerror("Error", "Please provide a valid URL.")

    def __init__(self, root):
        self.root = root
        self.root.title("URL Media Downloader")

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

    def toggle_mp3_checkbox(self):
        if self.audio_only_var.get():
            self.mp3_checkbox.pack()  # Show the MP3 checkbox when Audio Only is selected
            self.mp3_checkbox.config(state=tk.NORMAL)  # Enable the MP3 checkbox
        else:
            self.mp3_checkbox.pack_forget()  # Hide the MP3 checkbox when Audio Only is unselected
            self.mp3_var.set(False)  # Uncheck the MP3 checkbox
            self.mp3_checkbox.config(state=tk.DISABLED)  # Disable the MP3 checkbox

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

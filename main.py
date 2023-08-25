import os
import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

class MP4ToMP3Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("MP4 to MP3 Converter")
        self.root.iconbitmap("conv.ico")

        self.upload_button = tk.Button(root, text="Upload MP4 File", command=self.upload_file)
        self.upload_button.pack(pady=10, padx=20, fill=tk.BOTH)

        self.convert_button = tk.Button(root, text="Convert to MP3", command=self.convert_to_mp3)
        self.convert_button.pack(pady=10, padx=20, fill=tk.BOTH)

        self.status_frame = tk.Frame(root)
        self.status_frame.pack(pady=10)

        self.status_label = tk.Label(self.status_frame, text="", fg="green")
        self.status_label.pack()

        window_width = 300
        window_height = 150
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def upload_file(self):
        self.mp4_file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if self.mp4_file_path:
            self.status_label.config(text="Upload Successful", fg="green")

    def convert_to_mp3(self):
        if hasattr(self, 'mp4_file_path'):
            mp3_save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")], initialfile=os.path.splitext(os.path.basename(self.mp4_file_path))[0])
            if mp3_save_path:
                mp3_file_path = os.path.splitext(mp3_save_path)[0] + ".mp3"
                ffmpeg_extract_audio(self.mp4_file_path, mp3_file_path)
                self.status_label.config(text="Convert Successful", fg="green")
                self.root.after(5000, self.hide_status_label)

    def hide_status_label(self):
        self.status_label.config(text="")

    def open_explorer(self, path):
        os.startfile(os.path.dirname(path))

if __name__ == "__main__":
    root = tk.Tk()
    app = MP4ToMP3Converter(root)
    root.mainloop()

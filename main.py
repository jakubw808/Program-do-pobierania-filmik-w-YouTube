import tkinter as tk
from tkinter import filedialog,ttk,messagebox
from pytube import YouTube

audio_ext=[
    "mp3", 'wav'
]
video_ext=[
    "mp4", "wmv"
]


def browse_button_dialog():
    global folder_path
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)
    chosen_folder.config(text=folder_path)

def download_video():
    urls = url_entry.get().split(" ")
    save_path = folder_path.get()
    extension = format_entry.get()
    if  not url_entry.get():
        urls.clear()
        messagebox.showwarning(
            message="Wprowadź adresy i spróbuj ponownie",
            title="Błąd!"
                               )
    else:
        if not folder_path.get():
            messagebox.showwarning(
                message="Wybierz miejsce pobierania i spróbuj ponownie",
                title="Błąd!"
                               )
        else:
            if not format_entry.get():
                messagebox.showwarning(
                message="Wybierz format i spróbuj ponownie",
                title="Błąd!"
                               )
            else:
                for n in urls:
                    video_url = n
                    try:
                        yt = YouTube(video_url)
                        if extension in video_ext:
                            video = yt.streams.filter().get_highest_resolution()
                            video.download(save_path,video.title+"."+extension)
                        if extension in audio_ext:
                            audio = yt.streams.filter(only_audio=True).first()
                            audio.download(save_path,audio.title+"."+extension)
                    except Exception as e:
                        messagebox.showerror(
                            message=e,
                            title="Błąd!"
                        )
                messagebox.showinfo(
                    title="Sukces!",
                    message=f"Pobrano plik/i do {save_path}"
                    )

root = tk.Tk()
root.title("YouTube Downloader")

folder_path= tk.StringVar()

url_label = tk.Label(root, text="Wprowadź URL filmu: \n (Dla pobierania wielu naraz, oddziel linki spacją)")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

format_label = tk.Label(root, text="Wybierz format")
format_label.pack(pady=10)

format_entry = ttk.Combobox(
    state="readonly",
    values=audio_ext+video_ext
)

format_entry.pack(pady=10)

browse_button = tk.Button(root, text="Wybierz folder", command=browse_button_dialog)
browse_button.pack(pady=10)

chosen_folder = tk.Entry(root, state="disabled")
chosen_folder.pack(pady=10)

download_button = tk.Button(root, text="Pobierz film", command=download_video)
download_button.pack(pady=10)

root.mainloop()
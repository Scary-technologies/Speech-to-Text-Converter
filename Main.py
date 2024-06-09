import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import speech_recognition as sr
from pydub import AudioSegment
import threading

def convert_audio_to_text(audio_file_path, output_text_file):
    if not audio_file_path.endswith(".wav"):
        sound = AudioSegment.from_file(audio_file_path)
        audio_file_path = "converted.wav"
        sound.export(audio_file_path, format="wav")

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="fa-IR")
            with open(output_text_file, "w", encoding="utf-8") as file:
                file.write(text)
            messagebox.showinfo("موفقیت", f"متن با موفقیت در {output_text_file} ذخیره شد")
        except sr.UnknownValueError:
            messagebox.showerror("خطا", "صدای ورودی قابل درک نیست")
        except sr.RequestError as e:
            messagebox.showerror("خطا", f"درخواست ناموفق بود؛ {e}")

def select_audio_file():
    audio_file_path = filedialog.askopenfilename(
        title="انتخاب فایل صوتی",
        filetypes=[("فایل‌های صوتی", "*.wav *.mp3 *.flac *.ogg *.m4a")]
    )
    if audio_file_path:
        audio_file_entry.delete(0, tk.END)
        audio_file_entry.insert(0, audio_file_path)

def save_text_file():
    output_text_file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("فایل‌های متنی", "*.txt")]
    )
    if output_text_file:
        text_file_entry.delete(0, tk.END)
        text_file_entry.insert(0, output_text_file)

def start_conversion():
    audio_file_path = audio_file_entry.get()
    output_text_file = text_file_entry.get()
    if not audio_file_path or not output_text_file:
        messagebox.showerror("خطا", "لطفا هر دو فایل صوتی و فایل متنی خروجی را انتخاب کنید")
        return

    threading.Thread(target=convert_audio_to_text, args=(audio_file_path, output_text_file)).start()

# ایجاد رابط کاربری
root = tk.Tk()
root.title("تبدیل گفتار به متن")

frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

audio_file_label = ttk.Label(frame, text="فایل صوتی:")
audio_file_label.grid(row=0, column=0, sticky=tk.W, pady=5)

audio_file_entry = ttk.Entry(frame, width=50)
audio_file_entry.grid(row=0, column=1, pady=5)

audio_file_button = ttk.Button(frame, text="انتخاب...", command=select_audio_file)
audio_file_button.grid(row=0, column=2, padx=5, pady=5)

text_file_label = ttk.Label(frame, text="فایل متنی خروجی:")
text_file_label.grid(row=1, column=0, sticky=tk.W, pady=5)

text_file_entry = ttk.Entry(frame, width=50)
text_file_entry.grid(row=1, column=1, pady=5)

text_file_button = ttk.Button(frame, text="ذخیره به عنوان...", command=save_text_file)
text_file_button.grid(row=1, column=2, padx=5, pady=5)

convert_button = ttk.Button(frame, text="تبدیل", command=start_conversion)
convert_button.grid(row=2, columnspan=3, pady=20)

# تنظیمات بهتر برای اندازه پنجره
root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()

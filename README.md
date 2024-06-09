تبدیل گفتار به متن (Speech to Text Converter) یک برنامه کاربردی است که با استفاده از کتابخانه‌های SpeechRecognition و pydub، فایل‌های صوتی را به متن تبدیل می‌کند. این برنامه با بهره‌گیری از رابط کاربری گرافیکی (GUI) ساخته شده با tkinter و ttk، تجربه کاربری بهتری ارائه می‌دهد. همچنین برای جلوگیری از توقف رابط کاربری هنگام پردازش فایل صوتی، از تکنیک threading استفاده شده است. این برنامه قابلیت انتخاب فایل صوتی و تعیین مسیر ذخیره فایل متنی خروجی را فراهم می‌کند.

ویژگی‌ها
رابط کاربری گرافیکی زیبا و کاربرپسند:

استفاده از tkinter و ttk برای ایجاد یک رابط کاربری مدرن و شیک.
ترجمه تمامی برچسب‌ها و پیام‌ها به فارسی.
تبدیل گفتار به متن:

پشتیبانی از فایل‌های صوتی با فرمت‌های مختلف (wav, mp3, flac, ogg, m4a).
استفاده از کتابخانه SpeechRecognition برای تشخیص گفتار و تبدیل آن به متن.
استفاده از pydub برای تبدیل فایل‌های صوتی به فرمت wav در صورت نیاز.
پردازش همزمان:

استفاده از threading برای اجرای فرآیند تبدیل گفتار به متن در یک رشته جداگانه، به منظور جلوگیری از توقف رابط کاربری هنگام پردازش.
نیازمندی‌ها (Requirements)
برای اجرای این برنامه، نیاز به نصب کتابخانه‌های زیر دارید:

tkinter: کتابخانه استاندارد Python برای ایجاد رابط کاربری گرافیکی.
ttk: کتابخانه‌ای برای ایجاد ویجت‌های مدرن‌تر و زیباتر در tkinter.
speech_recognition: کتابخانه‌ای برای تبدیل گفتار به متن.
pydub: کتابخانه‌ای برای پردازش فایل‌های صوتی.
ffmpeg: ابزار خط فرمان برای تبدیل فایل‌های صوتی به فرمت‌های مختلف.
نصب کتابخانه‌ها
برای نصب کتابخانه‌های SpeechRecognition و pydub، از دستورهای زیر استفاده کنید:

bash
Copy code
pip install SpeechRecognition pydub
نصب و پیکربندی ffmpeg
ویندوز:
به وب‌سایت رسمی ffmpeg بروید و نسخه ویندوز را دانلود کنید.
فایل ZIP را استخراج کنید و پوشه استخراج شده را به مکان مناسبی مانند C:\ffmpeg منتقل کنید.
مسیر bin را به متغیر محیطی PATH اضافه کنید:
بر روی دکمه Start کلیک کنید و "Environment Variables" را جستجو کنید.
گزینه "Edit the system environment variables" را انتخاب کنید.
بر روی دکمه "Environment Variables" کلیک کنید.
در بخش "System variables"، متغیر Path را انتخاب کرده و "Edit" را کلیک کنید.
بر روی "New" کلیک کنید و مسیر C:\ffmpeg\bin را وارد کنید.
تغییرات را ذخیره کنید.
مک یا لینوکس:
برای نصب ffmpeg بر روی مک یا لینوکس، از دستورات زیر استفاده کنید:

مک:

bash
Copy code
brew install ffmpeg
لینوکس (اوبونتو):

bash
Copy code
sudo apt install ffmpeg
نحوه استفاده
برنامه را اجرا کنید.
بر روی دکمه "انتخاب..." کلیک کنید تا فایل صوتی مورد نظر خود را انتخاب کنید.
بر روی دکمه "ذخیره به عنوان..." کلیک کنید تا مسیر فایل متنی خروجی را تعیین کنید.
بر روی دکمه "تبدیل" کلیک کنید تا فرآیند تبدیل گفتار به متن آغاز شود.
پس از اتمام فرآیند، متن به فایل متنی خروجی ذخیره خواهد شد و پیام موفقیت نمایش داده می‌شود.

import os
import sys
import webbrowser
from threading import Timer
from django.core.management import execute_from_command_line

def open_browser():
    """وظيفة لفتح المتصفح تلقائياً"""
    webbrowser.open_new('http://127.0.0.1:8000/')

if __name__ == "__main__":
    # تشغيل المتصفح بعد 2 ثانية من بدء السيرفر
    Timer(2, open_browser).start()

    # ضبط إعدادات المشروع
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    try:
        print("--- تطبيق إنجاز يعمل الآن ---")
        print("يمكنك إغلاق هذه النافذة بعد الانتهاء من العمل.")
        # تشغيل السيرفر بدون خاصية Reload لأنها تسبب مشاكل في الـ EXE
        execute_from_command_line([sys.argv[0], 'runserver', '127.0.0.1:8000', '--noreload'])
    except Exception as e:
        print(f"خطأ في التشغيل: {e}")
        input("اضغط Enter للخروج...")

# ملف تشغيل للوحدة المشفرة file.cpython-312.so
import file

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(file, 'main'):
    file.main()
else:
    print("تم استيراد file بنجاح، ولكن لا توجد دالة main للتشغيل.")

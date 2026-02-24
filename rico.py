
# ملف تشغيل للوحدة المشفرة rico.cpython-312.so
import rico

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(rico, 'main'):
    rico.main()
else:
    print("تم استيراد rico بنجاح، ولكن لا توجد دالة main للتشغيل.")

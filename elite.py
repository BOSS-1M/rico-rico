
# ملف تشغيل للوحدة المشفرة elite.cpython-312.so
import elite

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(elite, 'main'):
    elite.main()
else:
    print("تم استيراد elite بنجاح، ولكن لا توجد دالة main للتشغيل.")

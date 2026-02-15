
# ملف تشغيل للوحدة المشفرة maya.cpython-312.so
import maya

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(maya, 'main'):
    maya.main()
else:
    print("تم استيراد maya بنجاح، ولكن لا توجد دالة main للتشغيل.")

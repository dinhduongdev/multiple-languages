# 🌍 Django Multiple Languages (i18n)

Hướng dẫn từng bước thiết lập và sử dụng đa ngôn ngữ trong Django.

---

## ✅ Yêu cầu

- Python >= 3.6  
- Django >= 3.x  
- `gettext` (dùng để dịch và biên dịch ngôn ngữ)

---

## ⚙️ Bước 1: Cấu hình `settings.py`

```python
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en'
USE_I18N = True

LANGUAGES = [
    ('en', _('English')),
    ('vi', _('Vietnamese')),
    ('fr', _('French')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

```

## 🌐 Bước 2: Dùng trong template & Python

**Trong template:**
```django
{% load i18n %}
<h1>{% trans "Welcome" %}</h1>
```

**🌐 Cách dùng trong Template**
```django
{% load i18n %}
<h1>{% trans "Welcome" %}</h1>
<p>{% blocktrans %}This is a translatable paragraph.{% endblocktrans %}</p>
```
**💬 Cách dùng trong Python code**
```django
from django.utils.translation import gettext as _
def my_view(request):
    message = _("This text will be translated")
    return render(request, "example.html", {"message": message})
```
**📁 Tạo file dịch**
```django
Chạy lệnh sau để tạo file .po:
django-admin makemessages -l vi
```
**📝 Dịch nội dung**
```django
Mở file locale/vi/LC_MESSAGES/django.po, chỉnh sửa như sau:
msgid "Welcome"
msgstr "Chào mừng"
msgid "This text will be translated"
msgstr "Đoạn văn bản này sẽ được dịch"
```
**🔧 Biên dịch file dịch**
```django
Sau khi dịch xong, biên dịch sang file .mo:
django-admin compilemessages

```
**🌐 Thay đổi ngôn ngữ trong session (ví dụ):**
```django
from django.utils import translation
def change_language(request):
    user_language = 'vi'
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return redirect('/')
```
## 📚 Tài liệu thêm
Django i18n: https://docs.djangoproject.com/en/stable/topics/i18n/


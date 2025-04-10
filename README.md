# 🌍 Django Multiple Languages (i18n)

Hướng dẫn thiết lập và sử dụng đa ngôn ngữ trong Django.

## ✅ Yêu cầu

- Python >= 3.6  
- Django >= 3.x  
- `gettext` (để dịch và biên dịch ngôn ngữ)

---

## ⚙️ 1. Cấu hình `settings.py`

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


🌐 2. Dùng trong template và Python
{% load i18n %}
<h1>{% trans "Welcome" %}</h1>


# 📌 Django DRF CRUD API - Fayllar va Kataloglar uchun

## 📖 Loyihani qisqacha tavsif
Bu loyiha **Django Rest Framework (DRF)** asosida CRUD operatsiyalarini amalga oshirish uchun ishlab chiqilgan.
Loyiha orqali foydalanuvchilar fayllar va kataloglar haqidagi ma'lumotlarni kiritish, ko'rish, qidirish, saralash, yangilash va o‘chirish imkoniyatiga ega.

---

## 🚀 O'rnatish va ishga tushirish

### 1️⃣ **Loyihani yuklab oling**

```bash
git clone https://github.com/theNodirjon/oop_takrorlash.git  # Github URL
cd repository  # Loyiha papkasiga o'tish. Agar kerak bo'lsa
```

### 2️⃣ **Virtual muhitni yaratish va faollashtirish**

```bash
python -m venv venv  # Virtual muhit yaratish
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ **Kerakli kutubxonalarni o‘rnatish**

```bash
pip install -r requirements.txt
```

### 4️⃣ **.env faylini sozlash**
Loyiha ildizida **.env** faylini yarating va quyidagi ma'lumotlarni kiriting:

```
SECRET_KEY=istalganSozYokiNarsa
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

### 5️⃣ **Ma'lumotlar bazasini sozlash**

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ **Super foydalanuvchi yaratish (Admin panel uchun)**

```bash
python manage.py createsuperuser
```
Agar kerak bo'lsa.

### 7️⃣ **Serverni ishga tushirish**

```bash
python manage.py runserver
```

Tizimni brauzerda oching: **http://127.0.0.1:8000/**

---

## 📌 API Endpointlari

### 1️⃣ **Ma'lumot qo‘shish (CREATE)** - `POST /files/`
```json
{
    "name": "New File",
    "file_type": "file",
    "absolute_path": "/home/user/new_file.txt",
    "size": 1024
}
```

### 2️⃣ **Barcha fayllarni olish (READ)** - `GET /files/`
```bash
http://127.0.0.1:8000/files/
```

### 3️⃣ **Qidiruv (3 ta kalit so‘z bilan)** - `GET /files/?q=document&q=report&q=pdf`
```bash
http://127.0.0.1:8000/files/?q=document&q=report&q=pdf
```

### 4️⃣ **Saralash**
- **Nomi bo‘yicha:**  `GET /files/?sort=name`
- **Hajmi bo‘yicha kamayish:** `GET /files/?sort=-size`

### 5️⃣ **Ma'lumotni yangilash (UPDATE)** - `PUT /files/{id}/`
```json
{
    "name": "Updated File",
    "file_type": "file",
    "absolute_path": "/home/user/updated_file.txt",
    "size": 2048
}
```

### 6️⃣ **Ma'lumotni o‘chirish (DELETE)** - `DELETE /files/{id}/`
```bash
http://127.0.0.1:8000/files/1/
```

---

## ⚙️ Texnologiyalar
- **Python 3.13.1**
- **Django 5.2**
- **Django Rest Framework (DRF)**
- **SQLite (yoki MySQL, PostgreSQL)**

---

## 📌 Muhim manbalar
- 📚 Django DRF hujjatlari: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
- 🐍 Python rasmiy sayti: [https://www.python.org/](https://www.python.org/)
- 🚀 Django hujjatlari: [https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/)

---

## 🛠 Muallif
👨‍💻 **Nodirjon** - [GitHub Profilim](https://github.com/theNodirjon)

✅ Agar loyiha sizga foydali bo‘lsa ⭐ Yulduz bosing!


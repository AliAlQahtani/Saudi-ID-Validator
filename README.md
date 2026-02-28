# Saudi ID Validator 🇸🇦

## English

### Description

A full-stack application for validating Saudi National ID and Iqama numbers using a modified Luhn algorithm. The system ensures the ID is 10 digits, starts with 1 (Citizen) or 2 (Resident), and passes the required checksum validation.

### Features

- Validates Saudi National ID and Iqama numbers.
- Built with a modern, fast tech stack.
- Auto-converts Eastern Arabic numerals (٠-٩) to Western Arabic numerals (0-9).
- Clean and responsive user interface.
- **100% Offline:** The system runs completely offline once started locally, ensuring total data privacy.

### Tech Stack

- **Frontend:** Svelte + Vite
- **Backend:** Python (FastAPI)

### How to Run Locally

You need two terminal windows to run both frontend and backend.

#### 1. Backend (FastAPI)

Navigate to the `backend` directory and run the application:

```bash
cd backend
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

The FastAPI server will start at `http://localhost:8000`.

#### 2. Frontend (Svelte)

Navigate to the `frontend` directory:

```bash
cd frontend
npm install
npm run dev
```

The Svelte app will be available at `http://localhost:5173`.

---

## العربية (Arabic)

### الوصف

تطبيق متكامل للتحقق من صحة أرقام الهوية الوطنية والإقامة السعودية باستخدام خوارزمية "Luhn" المعدلة. يتأكد النظام من أن الهوية تتكون من 10 أرقام، وتبدأ بـ 1 (للمواطنين) أو 2 (للمقيمين)، بالإضافة إلى التحقق من صحة الأرقام حسابياً.

### المميزات

- التحقق من الهوية الوطنية والإقامة السعودية.
- مبني بتقنيات حديثة وسريعة.
- تحويل الأرقام العربية (٠-٩) تلقائياً إلى أرقام إنجليزية (0-9) لتسهيل الإدخال للحواسيب والهواتف.
- واجهة مستخدم نظيفة ومتجاوبة وحسنة المظهر.
- **يعمل بالكامل أوفلاين (Offline):** بمجرد تشغيل النظام محلياً، فإنه لا يحتاج إلى اتصال بالإنترنت، مما يضمن الخصوصية التامة للبيانات.

### التقنيات المستخدمة

- **الواجهة الأمامية (Frontend):** Svelte + Vite
- **الخلفية (Backend):** Python (FastAPI)

### طريقة التشغيل المحقق (محليًا)

تحتاج إلى نافذتي أوامر (Terminal) لتشغيل الواجهة الأمامية والخلفية.

#### 1. الخلفية (Backend)

انتقل إلى مجلد الخلفية (`backend`) وشغل السيرفر:

```bash
cd backend
python -m venv .venv

# تفعيل البيئة الوهمية (Virtual Environment)
source .venv/bin/activate  # في الويندوز استخدم: .venv\Scripts\activate

# تثبيت الحزم المطلوبة
pip install -r requirements.txt

# تشغيل الخادم
python main.py
```

سيعمل السيرفر على الرابط `http://localhost:8000`.

#### 2. الواجهة الأمامية (Frontend)

انتقل إلى مجلد الواجهة الأمامية (`frontend`):

```bash
cd frontend
npm install
npm run dev
```

ستعمل الواجهة على الرابط `http://localhost:5173`.

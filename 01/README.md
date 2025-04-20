# 📊 Streamlit Project

A simple Streamlit project created as part of my learning journey. This README outlines the steps I followed to build and run the project using [Streamlit](https://streamlit.io/) and [UV](https://github.com/astral-sh/uv) — a fast Python package manager.

---

## 🛠️ How This Project Was Made

I completed this project by following these steps:

1. **Created a folder named** `StreamLit_Project`.

2. **Opened the folder using** [Cursor](https://www.cursor.so/) – an AI-powered code editor.

3. **Inside `StreamLit_Project`, created a subfolder named** `01`.

4. **Installed [UV](https://github.com/astral-sh/uv) instead of pip because it's faster**  
   If UV is not already installed:
   ```bash
   pip install uv
   ```
   To verify UV installation:
   ```bash
   uv --version
   ```

5. **Initialized a Streamlit project:**
   ```bash
   uv init streamlit_01
   ```
   This creates a folder `streamlit_01` and sets up the project environment.

6. **Navigated into the new project folder:**
   ```bash
   cd streamlit_01
   ```

7. **Installed Streamlit using UV:**
   ```bash
   uv add streamlit
   ```

8. **Edited `main.py`**  
   - Opened the file  
   - Removed any existing code  
   - Wrote custom Streamlit code

9. **Ran the Streamlit app:**
   ```bash
   uvx streamlit run main.py
   ```

10. **Accessed the running server at:**  
    [http://localhost:8501](http://localhost:8501)

---

## 📸 Screenshot

Here's a preview of the running project:

![Streamlit Screenshot](StreamLit_01.png)

---

## 🚀 Installation (For pip users)

If you're not using UV, you can install Streamlit using pip:

```bash
pip install streamlit
```

---

## ✅ Features

- Simple Streamlit project setup
- Uses UV for fast package management
- Clean and minimal project structure

---

## 📂 Folder Structure

```
StreamLit_Project/
│
├── 01/
│   └── streamlit_01/
│       ├── main.py
│       ├── StreamLit_01.png
│       └── ...
├── README.md
```

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

# 🎬 Video Manager

This is a command-line Video manager application written in Python. It helps you store, view, update, and delete video records either using a local file or a SQLite database — depending on the version you choose.

---

## 📁 Project Structure

```bash
Video-Manager/
│
├── file_version/        # Version using JSON file storage
│   ├── Video.txt        # Stores video data
│   ├── main.py          # File-based app logic
│   └── README.md        # Instructions for file version
│
├── db_version/          # Version using SQLite database
│   ├── main.py          # Database-backed app logic
│   ├── init_db.py       # (Optional) Script to initialize DB
│   └── README.md        # Instructions for DB version
│
└── README.md            # Root documentation (this file)
```

| Version                          | Description                                                                                    |
| -------------------------------- | ---------------------------------------------------------------------------------------------- |
| [`file_version`](./file_version) | Stores video data in a local `Video.txt` file using JSON. Best for beginners or offline use. |
| [`db_version`](./db_version)     | Uses SQLite database for persistent and structured storage. Recommended for more advanced use. |

# 🎬 Video Manager CLI — SQLite Version

This is the **database version** of the Video Manager app, built using Python and SQLite. It lets you store, view, update, and delete video records in a structured and persistent way using a local `.db` file.

---

## 📦 Features

- 🧾 View all stored videos
- ➕ Add new videos
- ✏️ Edit existing videos
- ❌ Delete videos
- 🗃️ SQLite database used for persistent storage

---

## 🧰 Requirements

- Python 3.x (no external libraries required)

---

## 🚀 How to Run

### 1. Navigate to the `db_version/` directory:

```bash
cd db_version
```

### 2. Run the application:
```bash
python3 video_manager_db.py
```

## 🗄️ Database Details

- Database file: `videos.db`
- Table name: `videos`
- Schema:

| Column | Type    | Description                    |
| ------ | ------- | ------------------------------ |
| id     | INTEGER | Primary key (auto-incremented) |
| name   | TEXT    | Name/title of the video        |
| time   | TEXT    | Duration of the video          |


## 🖥️ Sample Interaction
```text
Video manager app with DB
1. List videos
2. Add videos
3. Update videos
4. Delete videos
5. Exit app

Enter your choice: 1
No videos found in database.
```

## 📁 Folder Structure
<pre lang="markdown">
db_version/
├── .gitignore                  # To exclude the *.db file from version control
├── video_manager_db.py         # Main application code (SQLite-based)
├── videos.db                   # SQLite database file (auto-created at runtime)
└── README.md                   # This documentation file
</pre>
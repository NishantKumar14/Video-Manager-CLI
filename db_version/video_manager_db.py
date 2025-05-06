import sqlite3

conn = sqlite3.connect('videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_all_video():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()

    if not rows:
        print("No video found in database.")
    else: 
        print("\n")
        print("*" * 60)

        for row in rows:
            video_id, name , time = row
            print(f"ID: {video_id}, Name: {name}, Duration: {time}")

        print("*" * 60)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    
    while True:
        print("\n Video Manager app(CLI) with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")

        choice = input("\n Enter your choice: ")

        match choice:
            case '1':
                list_all_video()
                
            case '2':
                name = input("Enter a video name: ")
                time = input("Enter a video time: ")
                add_video(name, time)

            case '3':
                video_id = int(input("Enter a video ID to update: "))
                name = input("Enter a video name to update: ")
                time = input("Enter a video time to update: ")
                update_video(video_id, name, time)

            case '4':
                video_id = int(input("Enter a video ID to delete: "))
                delete_video(video_id)

            case '5':
                break

            case _:
                print("Invalid Choice.")


if __name__ == "__main__":
    main()


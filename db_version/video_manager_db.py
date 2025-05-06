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


def main():
    
    while True:
        print("\n Video Manager app(CLI) with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_video()
                
            case '2':
                name = input("Enter a video name: ")
                time = input("Enter a video time: ")
                add_video(name, time)

            case '3':
                vidoe_id = int(intput("Enter a video ID to update: "))
                name = input("Enter a video name to update: ")
                time = input("Enter a video time to update: ")
                update_video(vidoe_id, name, time)

            case '4':
                vidoe_id = int(input("Enter a video ID to delete: "))
                delete_video(vidoe_id)

            case '5':
                break

            case _:
                print("Invalid Choice.")


if __name__ == "__main__":
    main()


# Video Manager CLI with MongoDB

A command-line interface (CLI) application for managing video records in MongoDB, featuring CRUD operations and simple inventory management.

<!-- ![CLI Screenshot](https://via.placeholder.com/600x400?text=Video+Manager+CLI+Screenshot) 
*(Consider adding actual screenshot later)* -->

## Features

- **CRUD Operations**
  - List all videos with IDs, names, and durations
  - Add new video entries
  - Update existing video details
  - Delete videos from the collection
- **MongoDB Integration**
  - Secure connection using environment variables
  - Real-time database updates
  - Connection verification and error handling
- **User-Friendly Interface**
  - Simple text-based menu system
  - Clear input prompts
  - Error messages with troubleshooting guidance

## Prerequisites

- Python 3.10+
- MongoDB instance (local or [MongoDB Atlas](https://www.mongodb.com/atlas))
- Required Python packages:
  - `pymongo`
  - `python-dotenv`
  - `bson`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NishantKumar14/video-manager-cli.git
cd video-manager-cli
```

2. Install dependencies:
```bash
pip install pymongo
pip install python-dotenv
```

## Configuration

1. Create `.env` file:
```bash
MONGODB_URI=mongodb+srv://<username>:<password>@your-cluster.mongodb.net/
```

2. Replace with your actual MongoDB credentials:

- `<username>`: Your MongoDB username
- `<password>`: Your MongoDB password
- `your-cluster`: Your MongoDB cluster name


## Sample Interaction

```text
Video Manager (MongoDB)
1. List all videos
2. Add a new video
3. Update a video
4. Delete a video
5. Exit

Enter choice: 1
Video name: Python Tutorial
Video duration: 45:30
Inserted video ID: 65f1b2c3869a1d4e12f3a4b7
```

## Project Structure

<pre lang="markdown">
.
├── .env.example              # Environment variable template
├── video_manager.py          # Main application code
├── requirements.txt          # Dependency list
└── README.md                 # This documentation
</pre>


## Database Schema

Collection: `videos`
```javascript
{
  "_id": ObjectId,
  "name": string,
  "time": string
}
```

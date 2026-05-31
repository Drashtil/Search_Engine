# 🔍 Local File Search Engine

A Python-based file search tool that searches for files across your Desktop and all subfolders.

## Features

- Search files by name
- Search through all subfolders using `os.walk()`
- Display full file paths
- Count total matches found
- View file contents
- Simple command-line interface

## Technologies Used

- Python
- os module

## How It Works

1. Enter a search term.
2. The program scans the Desktop and all nested folders.
3. Matching files are displayed with their full paths.
4. Total matches are shown.
5. Users can view the contents of a selected file.

## Example

### Search

```text
Enter your search: python

Found:
python_notes.txt
C:\Users\User\Desktop\Projects\python_notes.txt

Total matches: 1
```

### View File

```text
Enter file name: python_notes.txt

Python is a programming language used for automation,
web development, data science, and more.
```

## Project Structure

```text
search-engine/
│
├── main.py
└── README.md
```

## Future Improvements

- Search inside file contents
- Filter by file type (.txt, .py, .pdf)
- Open files directly from the program
- GUI version using Tkinter
- Search multiple drives

## Author

Drashtil

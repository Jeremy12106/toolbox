# toolbox
Some of my common tools.  
Python version: 3.11  

---
### Directory Tree Generator

This tool generates a tree structure of files and folders in a specified directory.  
It helps visualize the hierarchy of your directory.  

- Input: An absolute file path.
- Example output:
  ```
  toolbox
    ├── .gitignore
    ├── DirectoryTreeGenerator.py
    ├── GradientColorGenerator.py
    ├── MP3
    ├── README.md
    ├── RenameFileAsCreationTime.py
    └── YoutubeMp3Downloader.py
  ```


---
### Gradient Color Generator

This tool generates a series of interpolated colors between a start and end color, based on the number of colors you specify.  
It is useful for creating smooth color gradients for design or visualization.  

- Input:
  - Start color: A color code you want to start with, e.g., "#FCCF31".
  - End color: A color code you want to end with, e.g., "#F55555".
  - Number of colors: The number of colors you want to generate.
- Example output: ['#fccf31', '#fab03a', '#f89243', '#f6734c', '#f55555']
  <img src="assets\pic\color_gradient.png" alt="Color Gradient" width="600" height="140"/>


---
### Rename File As Creation Time

This tool renames all files in a specified folder according to their creation or modification time.  
It ensures each file is named using the format `YYYYMMDD_HHMMSS`, making it easier to manage files based on when they were created or last modified.  

- Input: An absolute file path.
- Output: You need to confirm the execution path to modify the filenames in the path.


---
### Youtube Mp3 Downloader

This tool downloads the audio of a YouTube video as a file. It allows you to specify the YouTube URL and download the audio in the desired format (MP3 or M4A).

- Input: A Youtube URL
- Output: The audio file will be saved in the specified folder, such as `MP3` or `M4A`.


---
### Line Stickers Scraping

A simple Python script to scrape and download stickers from a LINE Stickers Shop URL. 
This script extracts sticker images from the specified URL and saves them in a well-organized folder structure.

- Input: A LINE Stickers Shop URL
- Output: Sticker files (PNG format) saved in the `line_stickers/<pack_name>` folder.
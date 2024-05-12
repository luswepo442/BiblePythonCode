## Bible Verse Lookup Tool

This Python script allows you to look up and display Bible verses from a text file containing the complete Bible. It provides a simple user interface using `tkinter` for inputting the book, chapter, and verse(s) you want to read. The text file `bible-complete.txt` must be present in the same directory as the script and formatted with Bible verses in the following format: `<Book> <Chapter>:<Verse> <Verse Text>`.

### Features

- **Single Verse Lookup**: Enter a specific book, chapter, and verse to display a single Bible verse.
  
- **Verse Range Lookup**: Enter a book, chapter, and a range of verses (e.g., 1-5) to display multiple consecutive verses.

### How to Use

1. **Run the Script**: Execute the Python script `easy gui.py`.
  
2. **Input Book, Chapter, and Verse**:
   - Enter the name of the book of the Bible (e.g., Genesis, Exodus).
   - Specify the chapter number within the book.
   - Input the desired verse number(s), either a single verse or a range (e.g., 1-5 for verses 1 to 5).

3. **View the Bible Verse**: The script will display the requested Bible verse(s) in a pop-up dialog box.

### Usage Examples

**Single Verse Lookup**:
- Book: Genesis
- Chapter: 1
- Verse: 1
  - Displays Genesis 1:1

**Verse Range Lookup**:
- Book: John
- Chapter: 3
- Verse: 16-18
  - Displays John 3:16-18

### Instructions

1. Ensure `bible-complete.txt` is in the same directory as the script.
2. Input the book, chapter, and verse(s) you wish to read.
3. Follow the on-screen prompts and dialog boxes to view the Bible verses.

### Notes

- The script handles errors gracefully and provides meaningful error messages for incorrect inputs or file reading issues.
- To exit the script, input `0` when prompted for the book, chapter, or verse.

#Luswepo Daniel Sinyinza
#ITI-2540-01
#Final Project
# Number of students = 1

# Importing necessary modules
import tkinter as tk
from tkinter import simpledialog, messagebox
import os

# Function to extract reference from a line of the Bible text
def get_reference(in_line):
    ref = in_line.split("\t")
    return ref[0]

# Function to extract verse from a line of the Bible text
def get_verse(in_line):
    ver = in_line.split("\t")
    return ver[1]

# Function to print a single verse
def print_verse(book, chapter, verse):
    try:
        with open("bible-complete.txt", "r") as inputFile:
            for in_line in inputFile:
                reference = get_reference(in_line).lower()
                if reference == f"{book} {chapter}:{verse}":
                    bible_verse = get_verse(in_line)
                    messagebox.showinfo("Bible Verse", bible_verse)
                    return
    except Exception as e:
        messagebox.showerror("Error", f"Error reading Bible: {e}")

# Function to print a range of verses
def print_verses(book, chapter, start_verse, end_verse):
    try:
        with open("bible-complete.txt", "r") as inputFile:
            for in_line in inputFile:
                reference = get_reference(in_line).lower()
                if reference.startswith(f"{book} {chapter}:"):
                    verse_number = int(reference.split(":")[1])
                    if start_verse <= verse_number <= end_verse:
                        bible_verse = get_verse(in_line)
                        messagebox.showinfo("Bible Verse", bible_verse)
                    if verse_number > end_verse:
                        break
    except Exception as e:
        messagebox.showerror("Error", f"Error reading Bible: {e}")

# Function to get the total count of verses in a chapter
def get_chapter_verse_count(book, chapter):
    try:
        with open("bible-complete.txt", "r") as inputFile:
            verse_count = 0
            for in_line in inputFile:
                reference = get_reference(in_line).lower()
                if reference.startswith(f"{book} {chapter}:"):
                    verse_count += 1
            return verse_count
    except Exception as e:
        messagebox.showerror("Error", f"Error reading Bible: {e}")
        return 0

# Main function to interact with the user
def main():
    while True:
        book = simpledialog.askstring("Input", "What Book of the Bible?").lower()

        if book == "0":
            messagebox.showinfo("Goodbye", "Thank you for reading the Bible!")
            return

        # Checking if the book name contains only alphabets
        if not book.isalpha():
            messagebox.showerror("Error", "ERROR: The Book does not exist, start again.")
            continue

        book_exists = False
        try:
            with open("bible-complete.txt", "r") as inputFile:
                for in_line in inputFile:
                    reference = get_reference(in_line).lower()
                    if reference.startswith(f"{book} "):
                        book_exists = True
                        break
            if not book_exists:
                messagebox.showerror("Error", "ERROR: The Book does not exist, start again.")
                continue
        except Exception as e:
            messagebox.showerror("Error", f"Error reading Bible: {e}")
            continue

        while True:
            chapter_input = simpledialog.askstring("Input", f"What Chapter of {book}?")

            if chapter_input == "0":
                messagebox.showinfo("Goodbye", "Thank you for reading the Bible!")
                return

            if chapter_input.isdigit():
                chapter = int(chapter_input)
                if chapter > 0:
                    try:
                        with open("bible-complete.txt", "r") as inputFile:
                            chapter_found = False
                            for in_line in inputFile:
                                reference = get_reference(in_line).lower()
                                if reference.startswith(f"{book} {chapter}:"):
                                    chapter_found = True
                                    break
                            if not chapter_found:
                                messagebox.showerror("Error", "ERROR: Chapter does not exist, start again.")
                                continue
                    except Exception as e:
                        messagebox.showerror("Error", f"Error reading Bible: {e}")
                        continue
                    break
                else:
                    messagebox.showerror("Error", "ERROR: Chapter must be a positive integer, start again.")
            else:
                messagebox.showerror("Error", "ERROR: Chapter must be a positive integer, start again.")

        while True:
            verse_input = simpledialog.askstring("Input", f"What verse of {book} Chapter {chapter}?")

            if verse_input == "0":
                messagebox.showinfo("Goodbye", "Thank you for reading the Bible!")
                return

            verse_range = verse_input.split("-")
            if len(verse_range) == 1:
                if verse_range[0].isdigit():
                    verse = int(verse_range[0])
                    if verse > 0 and verse <= get_chapter_verse_count(book, chapter):
                        print_verse(book, chapter, verse)
                        break
                    else:
                        messagebox.showerror("Error", "ERROR: Verse does not exist, start again.")
                else:
                    messagebox.showerror("Error", "ERROR: Verse must be a positive integer, start again.")
            elif len(verse_range) == 2:
                if verse_range[0].isdigit() and verse_range[1].isdigit():
                    start_verse = int(verse_range[0])
                    end_verse = int(verse_range[1])
                    chapter_verse_count = get_chapter_verse_count(book, chapter)
                    if start_verse > 0 and end_verse > 0 and end_verse >= start_verse and end_verse <= chapter_verse_count:
                        print_verses(book, chapter, start_verse, end_verse)
                        break
                    else:
                        messagebox.showerror("Error", "ERROR: The verse range provided does not exist, start again.")
                else:
                    messagebox.showerror("Error", "ERROR: Verse range must contain positive integers, start again.")
            else:
                messagebox.showerror("Error", "ERROR: Invalid input, start again.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    main()

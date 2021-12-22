**Test Generator**

**Introduction:**

  Test Generator is a desktop-based application made entirely using Python 3.7. It automates the task of manually setting a question paper and also generates an answer key for the same. The user will be able to generate unique set of questions from the same Excel file.

**Libraries used:**

1. **Tkinter:** Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.
- Label: The Label widget is used to provide a single-line caption for other widgets.
- Frame: The Frame widget is used as a container widget to organize other widgets.
- Entry: The Entry widget is used to display a single-line text field for accepting values from a user.
- Button: The Button widget is used to display buttons in your application.
- command: Function or method to be called when the button is clicked.
- tkMessageBox: The tkMessageBox module is used to display message boxes in your applications. This module provides a number of functions that you can use to display an appropriate message.
- tkFileDialog: The tkFileDialog module can be used to get a filename from the user. The module provides two convenience functions, one to get an existing filename so you can open it, and one to get a new filename, to save things into.
- askopenfilename(): The askopenfilename() method returns a string which is the path of the file selected by the user. If the user decides to hit Cancel, an empty string is returned. 
- filetypes: The argument to filetypes is a list of 2-element tuples. In each tuple, the first element is a string which is any description we want to set for each of the file types. The second element is where we state or list the file extensions associated with each file type.
2. **Pandas:** Pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time series data both easy and intuitive.
- read\_excel():** The method read\_excel() reads the data into a Pandas Data Frame, where the first parameter is the filename and the second parameter is the sheet.
- DataFrame: Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labelled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. Pandas DataFrame consists of three principal components, the data, rows, and columns.
- sample(): Returns a random sample of items from an axis of object.
- iterrows(): iterrows() returns the iterator yielding each index value along with a series containing the data in each row.

**Modules used:**

1. **OS:** The OS module in python provides functions for interacting with the operating system. OS, comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality. The “os” and “os.path” modules include many functions to interact with the file system.
- os.startfile(): The os.startfile() method allows us to “start” a file with its associated program. In other words, we can open a file with its associated program, just like when you double-click a .txt and it opens in Notepad.

**Conclusion:**

  The objective to build a Test Generator was successfully achieved. In terms of performance and efficiency, this project has provided a convenient method of generating question paper and their significant answer key. By using Pandas, the data is more organized. This application is also a user-friendly system as data collection, manipulation and presentation is done behind the interface. The question paper and the answer key once generated is stored in “.txt” files and then  automatically opens both the files. 

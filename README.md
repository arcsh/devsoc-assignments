# Project: System Calls & AI Tasks

This repository contains a collection of projects demonstrating skills in both low-level systems programming and high-level artificial intelligence tasks. It is divided into two main parts: `syscall` and `ai-ml`.

There is no documentation required for web-dev because the cloned repo was copied into this repo along with all associated files. Nothing has been changed in structure or form in those files. I have _only_ modified the underlying code to adhere to the instructions mentioned in the readme.

-----

## 📂 Directory Structure

```
.
├── ai-ml
│   ├── task-1
│   │   ├── generate_responses.py
│   │   ├── prompts.txt
│   │   └── responses.json
│   └── task-2
│       └── notebook.ipynb
├── syscall
│   ├── cat
│   ├── cat.c
│   ├── file.txt
│   ├── touch
│   └── touch.c
└── README.md
```

-----

## 🤖 AI/ML Tasks (`ai-ml/`)

This directory contains scripts and notebooks related to Artificial Intelligence and Machine Learning.

### **Task 1: Response Generation**

This task focuses on generating structured responses from a given set of prompts.

  * `prompts.txt`: A plain text file containing input prompts, with each prompt on a new line.
  * `generate_responses.py`: A Python script that reads the prompts from `prompts.txt`, processes them (likely using an API or a local model), and saves the output.
  * `responses.json`: The output file where the generated responses are stored in a structured JSON format.

#### **Usage**

1.  Add your prompts to the `prompts.txt` file.
2.  Install any necessary Python libraries (e.g., `requests`, `openai`). It's recommended to use a `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the script from the `task-1` directory:
    ```bash
    python generate_responses.py
    ```
4.  The results will be saved in `responses.json`.

### **Task 2: Jupyter Notebook**

This task involves data analysis, model experimentation, or visualization.

  * `notebook.ipynb`: A Jupyter Notebook containing the code, visualizations, and markdown explanations for an unspecified ML task.

#### **Usage**

1.  Ensure you have Jupyter Notebook or JupyterLab installed.
    ```bash
    pip install notebook
    ```
2.  Navigate to the `task-2` directory and launch Jupyter:
    ```bash
    jupyter notebook
    ```
3.  Open the `notebook.ipynb` file to view and run the analysis.

-----

## 🛠️ System Call Implementations (`syscall/`)

This directory contains custom implementations of common Unix command-line utilities written in C. This demonstrates an understanding of low-level file I/O and system calls.

  * `cat.c` & `touch.c`: The C source code for the `cat` and `touch` commands.
  * `cat` & `touch`: The compiled executable files.
  * `file.txt`: A sample text file used for testing the custom utilities.

### **How to Compile and Run**

You can compile the C source files using a C compiler like `gcc`.

#### **`cat` Utility**

The `cat` utility reads a file and prints its contents to the standard output.

1.  **Compile the code:**
    ```bash
    gcc cat.c -o cat
    ```
2.  **Run the executable:**
    ```bash
    ./cat file.txt
    ```

#### **`touch` Utility**

The `touch` utility creates a new, empty file if it doesn't exist, or updates the access/modification times of an existing file.

1.  **Compile the code:**
    ```bash
    gcc touch.c -o touch
    ```
2.  **Run the executable:**
    ```bash
    # Create a new file
    ./touch new_file.txt

    # Update timestamp of an existing file
    ./touch file.txt
    ```

# cppOrthodoxCanonicalGenerator


# Class Generator

This Python script is designed to generate C++ class files in the Orthodox Canonical form. It creates the following files for a given class name: `main.cpp`, `ClassName.cpp`, `ClassName.hpp`, and `Makefile`.

## Usage

1. Clone this repository to your local machine or download the script:
   
   ```bash
   git clone https://github.com/yourusername/class-generator.git

2. Navigate to the project directory:
    ```bash
    cd class-generator

3. install for macOS:
    ```bash
    alias genClass="python3 /path/to/scripy.py"
    or
    export="$PATH:/path/to/scripy.py"

## Examples:
        genClass Person
    
- this comand will generate the following files with orthodox-canonial form
    * main.cpp
    * Person.cpp
    * Person.hpp
    * Makefile

You can then edit the generated files to implement your class functionality.


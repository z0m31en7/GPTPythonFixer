<h1 align="center" id="title">GPTPythonFixer</h1><br>

<p id="description">This script leverages OpenAI's ChatGPT to provide assistance in fixing or suggesting solutions for errors in a Python file. It supports two modes of operation: processing the Python code directly or analyzing the output of a Python file via pipe. By interacting with ChatGPT, the script generates suggestions or explanations tailored to the provided Python code or output.</p><br><br>

<p align="center"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&amp;logo=windows&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&amp;logo=linux&amp;logoColor=black" alt="shields"><img src="https://img.shields.io/badge/tmux-1BB91F?style=for-the-badge&amp;logo=tmux&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&amp;logo=windows%20terminal&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/iTerm2-000000?style=for-the-badge&amp;logo=iterm2&amp;logoColor=white" alt="shields"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="shields"></p><br><br>

<h2>💡 Usage:</h2><br>

```
python GPTPythonFixer.py <file_path> [-p | --pipe]

```
Arguments:
* file_path: The path to the Python file to be fixed or analyzed.
* -p, --pipe: Optional argument. If provided, the script will use the output of the Python file via pipe instead of directly processing the file.

<br><h2>🛠️ Functionality:</h2><br>

1. Reads the specified Python file or captures the output of a Python file via pipe.<br>
2. Interacts with ChatGPT to generate suggestions or explanations based on the provided Python code or output.<br>
3. If operating on the file directly:<br>
    - Prints the suggested code or error explanation.<br>
    - Prompts the user to confirm replacing the code in the file.<br>
    - Replaces the code in the file if the user confirms.<br>
4. If using the output via pipe:<br>
    - Prints the suggested output based on the ChatGPT response.<br>

<br><h2>🔮 Examples:</h2>

* Process Python file directly:
   ```python fix_python_file.py path/to/your/python/file.py```

* Process Python file output via pipe:
   ```python error.py | python fix_python_file.py -p```

<br><h2>📜 Note:</h2>
* The script requires the OpenAI Python package (`openai`) to be installed.
* Replace 'YOUR_API_KEY' with your actual OpenAI API key in the script.
* Exercise caution when replacing code in a file and perform adequate testing.
* The script provides a basic example and may not handle all complex code or errors.
* The changes are suggested by ChatGPT and might contain errors.


<br><h2>🛡️ License:</h2><br>
This project is licensed under the <a href="https://github.com/z0m31en7/GPTPythonFixer/blob/main/LICENSE">MIT-LICENSE</a><br><br>

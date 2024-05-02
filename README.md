## Getting Started

Follow the instructions based on your Operating System

## Windows

### Requirements

- *Visual Studio Code*: Download and install from [here](https://code.visualstudio.com/).
- *GitHub Desktop* (optional): Useful for managing Git operations from a GUI.
- *Python*: Install Python from [here](https://www.python.org/downloads/)
- *Djanog*: Install Django using pip.

### Running

1. *Open the Command Prompt* and make sure you have pip installed.
```
pip --version
```

2. *Clone the repository* using Git. If you have GitHub Desktop installed, you can use it to clone the repo. Otherwise, use the following command in the Command Prompt:
```
git clone <your-repository-url>
```

3. *Navigate to your project directory* where **manage.py** is located.
```
cd path\to\your\project
```

4. *Create a virtual environment* (recommended) to isolate your package dependencies locally.
```
python -m venv env
```

5. *Activate the virtual environment*
```
env\Scripts\activate
```

6. *Install dependencies* in the **requirements.txt** file
```
pip install -r requirements.txt
```

7. *Run migrations* to set up your database schemas
```
python manage.py migrate
```

8. *Start the development server*
```
python manage.py runserver
```

After following these steps you are ready to work on the project.
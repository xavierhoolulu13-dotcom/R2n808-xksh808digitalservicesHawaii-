# COPILOT INSTRUCTIONS

## Project Structure Overview
This document provides instructions for building the complete project structure for the project. The required directories include `/src`, `/docs`, `/marketing`, and `/config`. Below are the steps to create each directory and the recommended files with functional starter code.

### 1. Directory Structure
To create the project structure, you should have the following directories:
    - /src  
    - /docs  
    - /marketing  
    - /config  

### 2. Creating Directories
You can use the command line or your preferred IDE to create these directories.

```bash
mkdir src docs marketing config
```

### 3. src Directory
This directory will contain the source code. Create a main file and a sample module:
- **main.py**
- **module.py**

#### main.py
```python
if __name__ == "__main__":
    print('Hello, World!')
```

#### module.py
```python
class SampleModule:
    def __init__(self):
        pass
```

### 4. docs Directory
This directory should contain documentation files. You can start with:
- **README.md**

#### README.md
```markdown
# Project Documentation
This is the documentation for the project.
```

### 5. marketing Directory
This directory should contain marketing-related materials. You may include:
- **marketing_plan.md**

#### marketing_plan.md
```markdown
# Marketing Plan
Outline the marketing strategies here.
```

### 6. config Directory
This directory should contain configuration files. You can create:
- **settings.py**

#### settings.py
```python
# Configuration settings
API_KEY = 'your_api_key'
```

### 7. Final Steps
After creating the directory structure and files, ensure to version control your project using Git:
```bash
git init
```

Now your project structure is complete and ready for further development!
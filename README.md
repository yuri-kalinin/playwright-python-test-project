# Playwright-Python-Test-Project
This repository contains a UI testing project that uses Python, Pytest, Playwright and Page Object Model pattern

# Requirements
* Python 3.12
* pip
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Instalation
1. Download or clone the repository
2. Open terminal
3. Go to the project root directory `\playwright-python-test-project\`
4. Create a virtual environment: `python -m venv .venv`
5. Activate the virtual environment executing the following script: `.\.venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`
7. Download browsers `playwright install`

# Test Execution
1. Edit the file `config.yaml` to configure the tests
2. Open terminal
3. From the project root directory run: `pytest -v --html=results/report.html`

# Configuration
Preferences can be changed in `config.yaml`

# Results
To check the report, open the '/results/report.html' file once the execution has finished

# Showcase
![2024-02-0623-58-25-ezgif com-video-to-gif-converter](https://github.com/yuri-kalinin/playwright-python-test-project/assets/16957236/5adf38d1-d4c1-4f0c-91d3-9d7339a45f18)

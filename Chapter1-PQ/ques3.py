# Ques3:- Install an external Module and use it to perform an operation of your interest.


# Hints: using "pyttsx3 2.98" which helps to convert python text-to-speech.

import pyttsx3
engine = pyttsx3.init()
engine.say("Hey Vandana! How are you? ")
engine.runAndWait()


# Here are some basic and useful external Python modules :-

# 1. requests: For making HTTP requests easily (GET, POST, etc.).
# Installation: pip install requests
# 2. numpy: Essential for numerical computing, handling arrays, and matrix operations.
# Installation: pip install numpy
# 3. pandas: Powerful for data analysis and manipulation, especially with tables and CSV files.
# Installation: pip install pandas
# 4. matplotlib: Plotting and graphing data for visualizations.
# Installation: pip install matplotlib
# 5. flask: Micro-framework for building web applications.
# Installation: pip install flask
# 6. django: Full-fledged web framework for building large-scale web applications.
# Installation: pip install django
# 7. beautifulsoup4: For web scraping, extracting data from HTML/XML documents.
# Installation: pip install beautifulsoup4
# 8. lxml: Library for processing XML and HTML with high performance.
# Installation: pip install lxml
# 9. pytest: Framework for testing Python code easily.
# Installation: pip install pytest
# 10. pyttsx3: Text-to-speech conversion library, useful for speech applications.
# Installation: pip install pyttsx3
# 11. openpyxl: To work with Excel files (both reading and writing).
# Installation: pip install openpyxl
# 12. SQLAlchemy: Object-Relational Mapping (ORM) library for database manipulation.
# Installation: pip install SQLAlchemy
# 13. paramiko: For SSH connections and file transfers over SSH.
# Installation: pip install paramiko
# 14. asyncio: For asynchronous programming (native in Python 3.4+).
# Installation: pip install asyncio
# 15. colorama: Used for coloring output in terminal applications.
# Installation: pip install colorama

import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())  # Show JSON response

# Python Pyppeteer Job Scraper

## Overview
This Python script utilizes Pyppeteer, a Python port of Puppeteer, to scrape job listings from Indeed.com. It automates the process of searching for job listings based on provided criteria like job title and location, extracts relevant information from the listings, and stores it in a text file.

## Installation
To run this project, follow these steps:

1. Clone this repository to your local machine.
2. Create a virtual environment for the project.
3. Activate the virtual environment.
4. Install the necessary dependencies using pip (pyppeteer)

## Usage
- Before running the script, ensure you have Google Chrome installed on your system. 
- Edit the script (job_scraper.py) and provide the path to chrome.exe in the executablePath parameter of the launch() function. This is necessary for Pyppeteer to launch the browser.
- Run the script: **_python job-scraper.py_**
- The script will launch Google Chrome, navigate to Indeed.com, search for job listings based on the provided criteria, extract relevant information, and store it in a text file (jobs.txt).

## Note
This script is designed to scrape job listings from Indeed.com. If you want to scrape from a different website, you may need to modify the script accordingly.

Pyppeteer requires a significant amount of resources, especially memory. Make sure your system meets the requirements to run the script smoothly.

It's recommended to run the script in a virtual environment to avoid conflicts with other Python projects.

Ensure that you have a stable internet connection while running the script to avoid any unexpected behavior.

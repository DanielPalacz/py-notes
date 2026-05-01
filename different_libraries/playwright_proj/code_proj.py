from playwright.sync_api import sync_playwright

import csv

input_file_name = "jobs.csv"

with open(input_file_name, newline='\n') as file_to_read_obj:
    csvfile_reader_obj = csv.reader(file_to_read_obj, delimiter=';')

    counter = 0
    for row in csvfile_reader_obj:
        counter += 1
        jobs_url = row[6]

        try:

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(jobs_url)

                name_ = row[0].replace(' ', '_')
                filename_ = f"screenshoots/{counter}__{name_}__.png"
                page.screenshot(path=filename_, full_page=True)

                browser.close()
                print(filename_)
        except Exception as e:
            print(e)

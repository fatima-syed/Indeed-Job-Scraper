# Importing necessary libraries
import asyncio
from pyppeteer import launch


async def start_scraping():

    # Step 1: Launch the browser
    browser = await launch(executablePath="C:\Program Files\Google\Chrome\Application\chrome.exe", headless=False)
    page = await browser.newPage()

    # Step 2: Go to Indeed.com
    await page.goto('https://www.indeed.com')

    # Step 3: Wait for text inputs to load
    await page.waitForSelector('#text-input-what')
    await page.waitForSelector('#text-input-where')

    # Step 4: Type in fields required
    await page.type('#text-input-what', 'Software Engineer')
    await page.type('#text-input-where', 'Pakistan')

    # Step 5: Submit the form
    await page.click('button[type="submit"]')

    # Step 6: Redirect to Job Listings page
    await page.waitForNavigation()

    # Node list with job listing elements
    job_listings = await page.querySelectorAll('.resultContent')

    # No results case
    if len(job_listings) < 1:
        print("No relevant jobs found.")


    for job in job_listings:
        # Extract the job title
        title_element = await job.querySelector('h2.jobTitle span[title]')
        title = await page.evaluate('(element) => element.textContent', title_element)


        # Extract the company name
        company_element = await job.querySelector('div.company_location [data-testid="company-name"]')
        company = await page.evaluate('(element) => element.textContent', company_element)


        # Extract the location
        location_element = await job.querySelector('div.company_location [data-testid="text-location"]')
        location = await page.evaluate('(element) => element.textContent', location_element)

        # Print info as output
        print({'title': title, 'company': company, 'location': location})

        # Store the info in a file
        with open('jobs.txt', 'a') as file:
            file.write(f"Title: {title}     Company: {company}     Location: {location}\n\n")

    await browser.close()


# Run the coroutine
if __name__ == '__main__':
    asyncio.run(start_scraping())
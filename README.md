![image](https://github.com/MCreasey3/Cars-and-Bids-Testing/assets/24724351/c2cdc3f8-b3ba-4711-a30b-b5dc5a399326)


---Simple test suite for web UI and performance testing on Cars and Bids (carsandbids.com)--- 

This test suite leverages Microsoft's Playwright automation framework, and is built in the Python version running with Pytest. Documentation for Playwright can be found here: https://playwright.dev/python/

This test suite aims to encapsulate basic methods of functional and non-functional testing. On the Web UI side, the search functionality and navigation of the website will be tested. This suite also employs Playwright's performance testing API to measure the website's responsiveness under load. 

You can clone the repository and install the requirements using `pip install -r requirements.txt`.

🟡 IN PROGRESS 🟡

- Performance API testing

🔴 KNOWN ISSUES 🔴

- Issues will be tracked in the Issues tab on the repository as well.
There's a timing problem somewhere when running the search test. Using the command `--slowmo 1000` seems to alleviate this for now. A standard command that works right now is: 

- `python3 -m pytest tests --headed --slowmo 1000`

- This bug also occurs when running tests on parallel threads > 2. I suspect they're related somehow. 

🔵 OPTIMIZATIONS 🔵

- The search test could be parametrized instead of iterating over the keywords passed in from the JSON config file.

- Search test currently checks for results based on a questionable selector - the site only displays results matching the keyword anyway, but for good practice this should be updated to match to the keyword. 



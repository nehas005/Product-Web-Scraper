# Python Product Web Scraper

This Python script is a simple web scraper designed to extract key product information from a given URL. It's built to provide clear output for easy viewing.

## Dependencies:

Before running this script, you need to install the following Python libraries:

* **requests:** For making HTTP requests to fetch the web page content.

* **beautifulsoup4:** For parsing the HTML content and navigating the document tree.

## How It Works

The core of the script is the `product_details` function. This function takes a product URL as input and returns a dictionary containing the scraped data.

1.  **HTTP Request:** It uses the `requests` library with a custom `User-Agent` header to mimic a web browser, fetching the HTML content of the product page. A `try...except` block is used to handle potential connection errors.

2.  **HTML Parsing:** Once the page content is successfully retrieved, `BeautifulSoup` parses it into a traversable object.

3.  **Data Extraction:** The script then searches for specific HTML elements using their ID or class attributes to extract the following information:

    * **Title:** The product name.

    * **Price:** The product's selling price.

    * **Rating:** The average customer rating.

    * **Availability:** Whether the product is in stock.

If any of these elements are not found, the script sets the value to 'not found'.

4.  **Output:** Finally, the script prompts the user for a URL, calls the `product_details` function, and prints the extracted information in a clean, readable format.

## Usage

To use this script, simply save the code to a `.py` file and run it from your terminal.

1.  Open your terminal or command prompt.

2.  Navigate to the directory where you saved the file.

3.  The script will then prompt you to "Enter product URL".

4.  Paste the URL and press Enter.

## Example Output

Here is what a typical output from the script looks like:
--- Product Information ---
Title: Example Product Name
Price: $25.99
Rating: 4.5 out of 5 stars
Availability: In Stock
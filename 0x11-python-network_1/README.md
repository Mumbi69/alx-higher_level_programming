# Python - Network #1
* HOWTO Fetch Internet Resources Using The urllib Package 
> * urllib.request is a Python module for fetching URLs.
* The response from urllib is typically in bytes. To decode it into a string, you can use the .decode() method, specifying the encoding format.  
* The requests library is a popular third-party package for making HTTP requests. It is known for its simplicity and rich features compared to urllib.
* In both urllib and requests, you can make an HTTP GET request using functions like urllib.request.urlopen(url) in urllib and requests.get(url) in requests.
* You can use the requests library to make various types of HTTP requests, like POST, PUT, DELETE, etc.
* To fetch JSON resources, you can make an HTTP GET request and then parse the JSON response.
* Once you have fetched data from an external service (e.g., an API), you can manipulate it using Python's data manipulation libraries like json (for JSON data), pandas (for structured data), and other built-in data processing tools


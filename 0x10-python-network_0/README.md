# Python - Network #0
* URL stands for Uniform Resource Locator. It's a string of characters that provides a way to identify and locate resources on the internet. URLs are used to specify the address of web pages, files, and other resources.
* HTTP stands for Hypertext Transfer Protocol. It is an application protocol used for transmitting hypermedia documents, such as HTML, over the World Wide Web. It is the foundation of data communication on the internet.
* A URL consists of several components, including the scheme, domain name (or IP address), port number, path, query string, and fragment identifier. For example, in the URL "https://www.example.com:8080/path/to/resource?param=value#section", the scheme is "https", the domain name is "www.example.com", the port number is "8080", the path is "/path/to/resource", the query string is "?param=value", and the fragment identifier is "#section".
* The scheme for an HTTP URL is typically "http" for unencrypted connections or "https" for encrypted connections (HTTP Secure).
* A domain name is a human-readable label used to identify a specific location on the internet. It is part of the URL and often corresponds to a website or server. For example, in "www.example.com," "example.com" is the domain name.
* A sub-domain is a domain that is part of a larger domain. It appears before the main domain name and is separated by a period. For example, in "blog.example.com," "blog" is a sub-domain of "example.com."
* A query string is a component of a URL that follows a question mark "?" and contains key-value pairs used to pass data to a web server. It is often used for parameters in web requests. For example, in "https://example.com/search?q=query," the query string is "?q=query."
* An HTTP request is a message sent by a client (e.g., a web browser) to a server requesting a specific action or resource. It typically includes an HTTP method, URL, headers, and sometimes a message body.
* An HTTP response is a message sent by a server to a client in response to an HTTP request. It contains information about the status of the request and may include data or resources requested by the client.
* HTTP headers are metadata associated with an HTTP request or response. They provide information about the message, such as content type, encoding, and authentication credentials. Headers are key-value pairs included in the HTTP message.
* The HTTP message body is the part of an HTTP request or response that contains the actual data being sent or received. It can include HTML content, JSON data, files, or any other information relevant to the request or response.
* An HTTP request method is a verb that specifies the action to be performed on a resource. Common HTTP methods include GET (retrieve data), POST (submit data), PUT (update data), DELETE (remove data), and more.
* An HTTP response status code is a three-digit numeric code returned by a server to indicate the status of an HTTP request. Examples include 200 (OK), 404 (Not Found), and 500 (Internal Server Error).
* An HTTP Cookie is a small piece of data sent from a web server and stored on the user's device by the web browser. Cookies are often used to store user-specific information, such as login credentials or session data, to maintain state between HTTP requests.
* cURL is a command-line tool used to make HTTP requests. You can use it by running a command like:
> * curl -X GET https://example.com
> * This sends an HTTP GET request to "https://example.com."
* When you type "google.com" in your browser and press Enter, the following steps occur at the application level:
> * 17.1. The browser initiates a DNS (Domain Name System) lookup to resolve "google.com" to an IP address.
> * 17.2. Once the IP address is obtained, the browser establishes a TCP connection to the web server associated with that IP address.
> * 17.3. The browser sends an HTTP GET request to the server for the "/" path (the default when no specific path is provided).
> * 17.4. The web server processes the request, generates an HTTP response, and sends it back to the browser.
> * 17.5. The browser receives the HTML content of the Google homepage and begins rendering it.
> * 17.6. The page may include additional resources (such as CSS, JavaScript, and images), which the browser fetches using additional HTTP requests.
> * 17.7. The browser displays the fully rendered Google homepage to the user.

# Response Status Code
* 1xx (Informational): Request received, server is continuing the process.
* 2xx (Success): The request was successfully received, understood, accepted and serviced.
* 3xx (Redirection): Further action must be taken in order to complete the request.
* 4xx (Client Error): The request contains bad syntax or cannot be understood.
* 5xx (Server Error): The server failed to fulfill an apparently valid request.

# Some commonly encountered status codes are:
* 100 Continue: The server received the request and in the process of giving the response.
* 200 OK: The request is fulfilled.
* 301 Move Permanently: The resource requested for has been permanently moved to a new location. The URL of the new location is given in the response header called Location. The client should issue a new request to the new location. Application should update all references to this new location.
* 302 Found & Redirect (or Move Temporarily): Same as 301, but the new location is temporarily in nature. The client should issue a new request, but applications need not update the references.
* 304 Not Modified: In response to the If-Modified-Since conditional GET request, the server notifies that the resource requested has not been modified.
* 400 Bad Request: Server could not interpret or understand the request, probably syntax error in the request message.
* 401 Authentication Required: The requested resource is protected, and require client’s credential (username/password). The client should re-submit the request with his credential (username/password).
* 403 Forbidden: Server refuses to supply the resource, regardless of identity of client.
* 404 Not Found: The requested resource cannot be found in the server.
* 405 Method Not Allowed: The request method used, e.g., POST, PUT, DELETE, is a valid method. However, the server does not allow that method for the resource requested.
* 408 Request Timeout:
* 414 Request URI too Large:
* 500 Internal Server Error: Server is confused, often caused by an error in the server-side program responding to the request.
* 501 Method Not Implemented: The request method used is invalid (could be caused by a typing error, e.g., "GET" misspell as "Get").
* 502 Bad Gateway: Proxy or Gateway indicates that it receives a bad response from the upstream server.
* 503 Service Unavailable: Server cannot response due to overloading or maintenance. The client can try again later.
* 504 Gateway Timeout: Proxy or Gateway indicates that it receives a timeout from an upstream server.

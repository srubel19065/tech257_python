# API's

## What are API's?
**APIs = Application Programming Interface**
- set of rules and protocols that allow communication between different software apps
- APIs define methods and data formats apps use to request/exchange info

**REASONS** for popularity:
- **INTEROPERABILITY** 
  - enable collaboration between software systems, platforms and services
    - devs can integrate different functions from different apps seamlessly
- **FLEXIBILITY and MODULARITY** 
  - allows devs to build modular and flexible software
    - dont need to build from scratch as existing APIs can be used
- **SCALABILITY**
  - scale easily as can offload certain tasks to specialised services/platforms 
    - e.g use of cloud storage

### DATA TRANSFER PROCESS
APIs follow client-server model = clients requests to API endpoint on server and server responds

1. Client sends HTTP request to the server  

2. Server receives HTTP request from client and routes to API endpoint

3. API Endpoint Processing
   - code logic to process request including database query and prepares data to be returned

4. Data Retrieval 
   - server retrive data and generated response

5. HTTP Response
   - server sends one back including status codes and optional messages
6. Client receives the HTTP response with data, client parses and reads data and does necessary actions with data

### REST APIs
REST APIs = Representational State Transfer Application Programming Interface
-  Architectural style(REST) for designing networked apps
- Set of principles defining how resources are: identified, addressed, how interaction between client and server should be

KEY CHARACTERISTICS:
- Stateless
  - each request must contain every detail of info and server does not store client state
- Client-Server Architecture 
- Uniform Interface
  - simple and scalable using set methods like HTTP Methods
- Resource-Based
  - identified by URIs
- State Transfer 

### REST guidelines
- Use nouns to represent URIS eg users
- Use HTTP methods
- Use HTTP status codes
- Use standard media types eg json
- Provide hypermedia links


### HTTP
Hypertext Transfer Protocol
- It's an application-layer protocol used for transmitting hypermedia docs such as HTML files over WWW
- Basically the communication between internet and clients

![](C:\Users\rubel\Downloads\HTTP REQUEST.png)

### HTTP - Request Structure

| VERB | URL | VERSION | 
|------|-----|---------|
|      |     |         |
|      |     |         |
|      |     |         |

1. **REQUEST LINE**
- Verb = method eg GET
- URL = resource identified by client
- Version = HTTP protocol version eg HTTP/1.1
##### EXAMPLE
GET /index.html HTTP/1.1

2. **HEADER LINE**
- Addtional info
  - clients user-agent, accepted content types, cookies etc
    - Host: Specifies the domain name of the server being requested.
    - User-Agent: Identifies the client software making the request.
    - Content-Type: Specifies the type of content included in the message body (for POST and PUT requests).
    - Accept: Indicates the content types that the client is willing to accept in the response.
    - Cookie: Contains any cookies associated with the request.
  ##### EXAMPLE
    - Host: www.example.com
    - User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
      - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

3. **MESSAGE BODY**
- Required when data is transferred

### HTTP - Response Structure

1. STATUS lINE
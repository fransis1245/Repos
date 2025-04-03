# Repos - me
1. Introduction.- In this repository, there is the code to download images of the public repository and store in a individual folder by categories

2. Selected Tools
    os - Python native module for creating folders (os.makedirs) and handling file paths.
    requests - External library (pip install requests) to make HTTP requests to the image API easily.
    Lorem Picsum - Public API, free service providing placeholder images without authentication.

4. Procedure
    a. Initial Setup:
    
    Define image categories ("Category A", "Category B", "Category C", etc.).
    
    Create corresponding folders using os.makedirs.
    
    b. Image Download:
    
    Make GET requests to https://picsum.photos/200 using requests.get().
    
    Verify HTTP status code (200 = success).
    
    c. File Saving:
    
    Use with open(..., "wb") to write the image in binary mode.
    
    Name files using the format [category]/image_[number].jpg.

    d. Error Handling:
    
    If the API fails (status code ≠ 200), display an error message.

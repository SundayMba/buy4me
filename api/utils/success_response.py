from flask import Flask

def success_response(message, data=None, status_code=200):
    """
    Generate a standardized success response for API endpoints.
    
    Args:
        message (str): A message describing the success.
        data (dict, optional): Optional data to include in the response.
        status_code (int, optional): HTTP status code. Defaults to 200 (OK).
        
    Returns:
        Flask Response: A JSON response with the provided message and data.
    """
    response = {
        "status": "success",
        "message": message
    }
    
    if data is not None:
        response['data'] = data
    
    return Flask(response), status_code

def created_response(message, data=None):
    """
    Returns a 201 Created response with a custom message and optional data.
    
    Args:
        message (str): A message describing what was created.
        data (dict, optional): Optional data to include in the response.
        
    Returns:
        Flask Response: A JSON response with HTTP 201 status code.
    """
    return success_response(message, data, status_code=201)

def no_content_response():
    """
    Returns a 204 No Content response, typically for delete operations.
    
    Returns:
        Flask Response: A JSON response with HTTP 204 status code and no body.
    """
    return '', 204


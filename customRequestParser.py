""" Module contains some helper methods used by Server to parse Client Request"""

def customRequestParser(data):
    """ Response based on Request message
        Request length should not exceed 30 characters
        Request first 4 characters should be number        
    """
    if data:
        if(len(data) > 30):
            return "REQUEST EXCEED MAX ALLOWED"

        requestArray = data.split()
        if(len(requestArray[0]) != 4 or not requestArray[0].isdigit()):
            return "BAD REQUEST 4 DIGIT MISSING"
            
        return reverseResponse(data)
    else:
        return "BAD REQUEST"

def reverseResponse(data):
        return ''.join(reversed(data))
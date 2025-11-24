def get_http_error(error_code: int) -> str:
    """
    Returns the HTTP error message corresponding to the given error code.

    Args:
        error_code (int): The HTTP error code.
    
    Returns:
        str: The corresponding error message.
    """

    match error_code:
        case 200:
            result = "OK"
        case 400:
            result = "Bad Request"
        case 404:
            result = "Not Found"
        case _:
            result = "Unknown Error"
    return result

def main():
    error_code = 404
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()
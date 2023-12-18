"""Fetch URL using requests package"""

if __name__ == "__main__":
    from requests import get

    url = 'https://intranet.hbtn.io/status'
    response = get(url)
    bytes_content = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
        type(bytes_content), bytes_content)
    print(string)

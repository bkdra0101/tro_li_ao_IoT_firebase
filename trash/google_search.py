import webbrowser

def search_google(text):
    url="https://www.google.com.vn/search?q="+ text
    webbrowser.open(url)
    
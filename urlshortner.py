import tkinter as tk
import pyperclip
import urllib.parse
import urllib.request
from urllib import parse, request
from PIL import ImageTk, Image

root = tk.Tk()
root.title("URL Shortener by Sravanth")
root.configure(background="black")

# Add a heading with custom font style
heading = tk.Label(root, text="URL Shortener", font=("Times", 50, "bold"), fg="White", bg="black")
heading.pack(pady=20)
heading1 = tk.Label(root, text="~convert your larger URL's into shorter ones", font=("Comic Sans MS2", 20), fg="White", bg="black")
heading1.pack(pady=10)
root.geometry("400x200")

# URL entry
text1 = tk.Label(root, text="Enter your URL below", font=("Arial", 15), fg="White", bg="black")
text1.pack(pady=40)
url_input = tk.Entry(root, width=100)
url_input.pack(pady=10)

def shorten_url():
    url = url_input.get()
    short_url = urllib.parse.quote(url, safe='')
    short_url = "http://tinyurl.com/api-create.php?url=" + short_url
    response = urllib.request.urlopen(short_url)
    short_url = response.read().decode('utf-8')
    pyperclip.copy(short_url)
    result_label.config(text="Short URL: " + short_url,font=("Arial", 20 , "bold"),fg="yellow" )

# Load the image and resize it
img = Image.open("D:/URL_shortner/shorten.png")
img = img.resize((100, 50))

# Create an ImageTk object from the resized image
shorten_image = ImageTk.PhotoImage(img)

# Add the image to the shorten_button
shorten_button = tk.Button(root, image=shorten_image, command=shorten_url)
shorten_button.pack(pady= 20)

result_label = tk.Label(root, text=" ", fg = "yellow", bg = "black")
result_label.pack(pady=10)

root.mainloop()

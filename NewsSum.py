import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    nltk.download('punkt')

    url = utext.get('1.0',"end").strip()
    # url = 'https://www.tomshardware.com/software/windows/microsoft-copilot-pcs-all-we-know'

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    keyword.config(state='normal')
    summary.config(state='normal')
    Sentiment.config(state='normal')

    title.delete('1.0', "end")
    title.insert('1.0', article.title)

    author.delete('1.0', "end")
    author.insert('1.0', article.authors)

    publication.delete('1.0', "end")
    publication.insert('1.0', article.publish_date)

    keyword.delete('1.0', "end")
    keyword.insert('1.0', article.keywords)

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    Sentiment.delete('1.0', "end")
    Sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    keyword.config(state='disabled')
    summary.config(state='disabled')
    Sentiment.config(state='disabled')

    # print(f'Title: {article.title}')
    # print(f'Authors: {article.authors}')
    # print(f'Publication Date: {article.publish_date}')
    # print(f'Summary: {article.summary}')

    # #660066 #FFCC00 #FFAC00

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1280x720')
root.config(bg='#660066')

# Dapatkan ukuran layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Ukuran jendela
window_width = 1280
window_height = 720

# Hitung posisi x dan y untuk menempatkan jendela di tengah layar
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 3) - (window_height // 3)

# Set posisi jendela
root.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')

font_style = ('Helvetica', 12, 'bold')

tlabel = tk.Label(root, text="Judul" , bg='#660066' , fg='#FFCC00', font=font_style)
tlabel.pack(pady=(15 , 0))

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#ddd')
title.pack()

alabel = tk.Label(root, text="Penulis", bg='#660066' , fg='#FFCC00', font=font_style)
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#ddd')
author.pack()

plabel = tk.Label(root, text="Tanggal Publikasi", bg='#660066' , fg='#FFCC00', font=font_style)
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#ddd')
publication.pack()

klabel = tk.Label(root, text="Kata Kunci", bg='#660066' , fg='#FFCC00', font=font_style)
klabel.pack()

keyword = tk.Text(root, height=1, width=140)
keyword.config(state='disabled', bg='#ddd')
keyword.pack()

slabel = tk.Label(root, text="Rangkuman", bg='#660066' , fg='#FFCC00', font=font_style)
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#ddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis", bg='#660066' , fg='#FFCC00', font=font_style)
selabel.pack()

Sentiment = tk.Text(root, height=1, width=140)
Sentiment.config(state='disabled', bg='#ddd')
Sentiment.pack()

ulabel = tk.Label(root, text="URL", bg='#660066' , fg='#FFCC00', font=font_style)
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.config(bg='#FFCC00')
utext.pack()

btn = tk.Button(root, text="Rangkum", command=summarize)
btn.config(bg='#ddd', fg='#660066', font=font_style)
btn.pack(pady=(25,0))



root.mainloop()
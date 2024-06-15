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
    summary.config(state='normal')
    Sentiment.config(state='normal')

    title.delete('1.0', "end")
    title.insert('1.0', article.title)

    author.delete('1.0', "end")
    author.insert('1.0', article.authors)

    publication.delete('1.0', "end")
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    Sentiment.delete('1.0', "end")
    Sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    Sentiment.config(state='disabled')

    # print(f'Title: {article.title}')
    # print(f'Authors: {article.authors}')
    # print(f'Publication Date: {article.publish_date}')
    # print(f'Summary: {article.summary}')

    # #660066 #FFCC00 #FFAC00

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Authors")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

Sentiment = tk.Text(root, height=1, width=140)
Sentiment.config(state='disabled', bg='#dddddd')
Sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()



root.mainloop()
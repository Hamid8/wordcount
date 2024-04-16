# -*- coding: utf-8 -*-
"""word count

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FVp2Sc3X6H4A6odJL_MJn5Prh8y0OhUj
"""

from google.colab import files
uplaoded= files.upload()

import pandas as pd

df = pd.read_csv('Marketing performance comparison ( 2022 vs 2023)_Google ads and Search console _Table.csv')

df

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud



# Create a dictionary with the word frequencies
word_freq = {}
for index, row in df.iterrows():
    word = row['query']
    freq = row['count']
    if not pd.isna(freq):
        word_freq[word] = int(freq)

# Create a word cloud object with custom settings
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=set(),
                      min_font_size=10).generate_from_frequencies(word_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)

# Show the plot
plt.show()


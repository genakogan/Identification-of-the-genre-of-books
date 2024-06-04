# Identification-of-the-genre-of-books

Our dataset was collected from knigogo.net, a Russian-language website that provides fresh news about literature, reviews, and feedback on popular books. It contains a large selection of audiobooks and online books in formats such as fb2, rtf, epub, and txt for iPad, iPhone, Android, and Kindle.
 We name the resulting dataset SONATA for ruSsian bOoks geNre dATAset.

As a result, 11 genres were selected for the dataset: Science Fiction, Detective, Romance, Fantasy, Classic, Action, Non-fiction, Contemporary Literature, Adventure, Novel and Short stories, and Children's books. In non-fiction, we encompassed all genres that do not belong to fiction literature.
The total of 8189 original books were downloaded. However, because some books belong to multiple genres, the total amount of book instances is 10444. 

During the processing, we have applied the following steps: (1) using a custom Python script we re-encoded the files into a UTF-8 format; (2) we parsed the second line of text containing the meta-data and removed the authors' names; (3) finally, we extract books without author names and split  them into small parts (chunks) of 300 words each to allow for LLM processing that has a limit on number of tokens.

The set of complete books and book chunks is available at the following google drive repository (due to its size):

# https://drive.google.com/drive/folders/1rnpMl39yOpsYTaE6ZGzk5nHQRU2dOASB?usp=sharing

Pythons script used for data collection is provided in downloadBooks_knigogo.py

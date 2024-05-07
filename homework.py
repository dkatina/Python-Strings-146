# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as 
# "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.




reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]


#point A : define a function that takes in a list of reviews

#search through list of reviews
#-- for loop, to look at each review individually
#for each review we are looking for key words "good", "excellent", "bad", "poor", and "average"
#--  can use membership check to see if the a kew word word is in my review
#replace the occurance of key words with their capitalized version
#-- once we find a key word in the string we can replace that key word with its uppercase version using .replace(kw, kw.upper())

#point B : print each review with the key words capitalized so the pop


def review_highlight(reviews):
    key_words = ["good", "excellent", "bad", "poor", "average"]
    for review in reviews:
        for kw in key_words:
            review = review.replace(kw, kw.upper())
            review = review.replace(kw.title(), kw.upper())

        print(review)

review_highlight(reviews)
# FraudDetector

Using a dataset I got from kaggle, I created a self-organizing map to detect credit card fraud. The way it does this is by figuring out the features of a normal credit card purchase, and organizing itself around those features. This creates the map.

From there, it maps all of the credit card purchases in the test set. Purchases that are on the outer edges of the map (figuratively speaking, in the actual plot they'll be colored white) thus indicate that those purchases are far from the normal set of features for a credit card purchase, i.e. they are suspicous activity. These can be determined to be credit card fraud.

If you want to run the program yourself, all you have to do is run the main.py, assuming you have the dependencies (they're all very common dependencies, most people will already have them installed). If you don't have them, just use pip to install them.

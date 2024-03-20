from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd

# Load the Enron1 dataset
data = pd.read_csv("enron1.csv")  # Adjust the file path as needed

# Extract features (X) and labels (y) from the dataset
X = data['text']
y = data['label']

# Define the preprocessor function
def preprocessor(text):
    import re
    # Replace non-alphabet characters with a space
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    # Convert the text to lowercase
    text = text.lower()
    return text

# Instantiate a CountVectorizer with the preprocessor
vectorizer = CountVectorizer(preprocessor=preprocessor)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Transform the datasets into a form the model can learn from
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Instantiate and fit the Logistic Regression model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

# Validate the model by generating predictions on the test set
y_pred = model.predict(X_test_vectorized)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print the evaluation metrics
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)

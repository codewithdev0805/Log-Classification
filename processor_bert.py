from sentence_transformers import SentenceTransformer
import joblib
# Load the pretrained Sentence Transformer model
transformer = SentenceTransformer('all-MiniLM-L6-v2')

# Load the saved classifier model
classifier = joblib.load('B:\Machine learning\Classification logs\models\log_clf.joblib')

def classify_with_bert(log_message):
    embedding = transformer.encode(log_message)
    probabilities = classifier.predict_proba([embedding])[0]
    if max(probabilities) < 0.5:
        return "Unclassified"
    predicted_label = classifier.predict([embedding])[0]
    return predicted_label

if __name__ == "__main__":
    logs =[
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
       "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]
    for log in logs:
        label = classify_with_bert(log)
        print(log, "->", label)
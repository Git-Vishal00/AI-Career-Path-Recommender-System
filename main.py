import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

career_descriptions = {
    "Data Scientist": "math, statistics, machine learning, data analysis, Python, R",
    "Software Developer": "coding, algorithms, software engineering, problem solving",
    "AI/ML Engineer": "deep learning, TensorFlow, PyTorch, data, models",
    "Product Manager": "communication, leadership, planning, tech, business",
    "UX Designer": "design, user experience, creativity, empathy"
}

nlp = spacy.load("en_core_web_sm")

def recommend_career(user_input):
    docs = list(career_descriptions.values()) + [user_input]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(docs)
    similarities = cosine_similarity(vectors[-1], vectors[:-1])
    scores = list(similarities[0])

    ranked = sorted(zip(career_descriptions.keys(), scores), key=lambda x: x[1], reverse=True)
    return ranked[:3]

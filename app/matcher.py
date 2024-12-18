from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class Matcher:
    def __init__(self, volunteers, nonprofits):
        self.volunteers = volunteers
        self.nonprofits = nonprofits

    def match(self):
        vectorizer = TfidfVectorizer()
        volunteer_skills = [" ".join(v.skills) for v in self.volunteers]
        nonprofit_skills = [" ".join(n.required_skills) for n in self.nonprofits]

        tfidf_matrix_volunteers = vectorizer.fit_transform(volunteer_skills)
        tfidf_matrix_nonprofits = vectorizer.transform(nonprofit_skills)

        similarity_matrix = cosine_similarity(tfidf_matrix_volunteers, tfidf_matrix_nonprofits)

        matches = {}
        for i, volunteer in enumerate(self.volunteers):
            best_match = similarity_matrix[i].argmax()
            matches[volunteer.name] = self.nonprofits[best_match].name

        return matches

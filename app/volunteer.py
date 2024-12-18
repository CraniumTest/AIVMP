class Volunteer:
    def __init__(self, id, name, skills, interests, availability, location):
        self.id = id
        self.name = name
        self.skills = skills
        self.interests = interests
        self.availability = availability
        self.location = location

    def __repr__(self):
        return f"Volunteer({self.name}, {self.skills}, {self.interests}, {self.location})"

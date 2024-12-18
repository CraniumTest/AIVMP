class NonProfit:
    def __init__(self, id, name, mission, projects, required_skills, location):
        self.id = id
        self.name = name
        self.mission = mission
        self.projects = projects
        self.required_skills = required_skills
        self.location = location

    def __repr__(self):
        return f"NonProfit({self.name}, {self.projects}, {self.required_skills}, {self.location})"

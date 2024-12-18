from app.utils import load_data
from app.volunteer import Volunteer
from app.nonprofit import NonProfit
from app.matcher import Matcher

def main():
    volunteers_data, nonprofits_data = load_data('data/volunteers.csv', 'data/nonprofits.csv')

    volunteers = [
        Volunteer(v.Id, v.Name, v.Skills.split(','), v.Interests.split(','), v.Availability, v.Location)
        for idx, v in volunteers_data.iterrows()
    ]

    nonprofits = [
        NonProfit(n.Id, n.Name, n.Mission, n.Projects.split(','), n.Required_skills.split(','), n.Location)
        for idx, n in nonprofits_data.iterrows()
    ]

    matcher = Matcher(volunteers, nonprofits)
    matches = matcher.match()

    print("Matches:", matches)

if __name__ == "__main__":
    main()

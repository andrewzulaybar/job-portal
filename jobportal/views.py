from django.shortcuts import render

from jobportal.sidebar import Sidebar


def get_context():
    sidebar = Sidebar()
    context = {
        'title': 'Home Page',
        'jobs': [{
            'job1': {
                'id': '1',
                'title': 'Software Developer Co-Op',
                'company': 'Amazon',
                'deadline': '5',
                'applications': '65',
                'salary': '30,000',
                'sector': 'Tech',
                'city': 'Seattle',
                'prov_state': 'WA',
                'type': 'Internship',
                'education': 'High school',
                'skills': ['java', 'c++'],
                'description': """We are looking for Amazon interns to join us for Fall 2019! Amazon interns have the 
                                opportunity to work alongside the industry’s brightest engineers who innovate everyday on 
                                behalf of our customers. Our interns and co-ops write real software and partner with a 
                                select group of experienced software development engineers, who both help and challenge 
                                them as they work on projects that matter..."""
            },
            'job2': {
                'title': 'Data Analyst',
                'company': 'SAP'
            }
        }],
        'sectors': ['Technology', 'Medical', 'Marketing'],
        'skills': ['Java', 'C++', 'Python'],
        'cities': sidebar.cities(),
        'education': ['No Minimum', 'High School', 'Bachelors', 'Masters', 'PhD'],
        'types': ['Part-Time', 'Full-Time', 'Contract', 'Internship']
    }
    return context


def home(request):
    return render(request, 'jobportal/home.html', get_context())


def premium_home(request):
    return render(request, 'jobportal/home-prem.html', get_context())


def company_home(request):
    return render(request, 'jobportal/home-comp.html', get_context())


def details(request):
    return render(request, 'jobportal/details.html', get_context())

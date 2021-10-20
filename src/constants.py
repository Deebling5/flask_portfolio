# Main constants
ssr = False
host = "0.0.0.0"  # Used if ssr (Server Side Rendering) is False
port = "8000"  # Used if ssr (Server Side Rendering) is False

# Configuration
discord_id = "832486961406803981"

me = {
    "name": "Abhijay Maheshwari",
    "email": "9abhijay@gmail.com",
    "location": "Gurgaon, India",
    "College": "DIT University",
    "Work Ex": "2 Years 3 Months",
    "short_bio": "Python Developer.",
    "bio": "2+ years of experience working for a MNC with American Pharma giant in full stack application development, Analytics, Automations, Web Design and an ability to provide an independent view of achievable automations and work-around on limitations to allow client and team work more efficiently. Expertise in using Python libraries for Data Mining, building dashboards, creating API's. Proficient in building Desktop applications and involving multiple python libraries to serve the purpose.",
}

# Custom redirects
# redirections = {
#     "blog": "https://erionline.medium.com/?utm_source=eri.gg",
#     "story": "https://erionline.medium.com/biraz-konusalim-nisan-2021-b8bbc5d9bb08/?utm_source=eri.gg",
# }

# Metadata
main_metadata = {
    "locale": "en_US",
    "author": "eri.gg",
    "title": "Abhijay Maheshwari - Portfolio",
    "desc": "",
    "image": "https://media.discordapp.net/attachments/712969229506183198/831109920103465000/img_caching.png",
    "favicon": "https://images-ext-2.discordapp.net/external/5Hi7Y5E0rvFTKpKPeGg6Uc1p1-itFQPf4AwEsjzcUqo/https/i.imgur.com/tGibRPY.png",
}

social_metadata = {
    "discord": {
        "desc": "Find out my Discord account named to add me as friend!",
        "url": f"https://discord.com/users/{discord_id}",
    },
    "github": {
        "desc": "Discover my work and projects from my GitHub profile.",
        "url": "https://github.com/Deebling5",
    },
    "instagram": {
        "desc": "Take a look to my posts & stories from some parts of my life.",
        "url": "https://www.instagram.com/themonksink",
    },
    "linkedin": {
        "desc": "Check out my LinkedIn profile to know more about my skills & experiences.",
        "url": "https://www.linkedin.com/in/abhijay-maheshwari/",
    },
    "medium": {
        "desc": "Read my diverse Medium stories about my personal life, interests and other topics.",
        "url": "https://medium.com",
    },
    "twitter": {
        "desc": "Follow me on Twitter to stay informed about what I do or feel.",
        "url": "https://twitter.com/AbhijayM",
    },
}

# Main page - Experiences
projects = [
    {
        "name": "Blogger Platform",
        "description": "Complete blogging platform with backend CMS written in Django and frontend in Bootstrap5",
        "link": None,
        "time": "Since September 2021",
        "snip": "https://images.unsplash.com/photo-1593642531955-b62e17bdaa9c?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1469&q=80"
    },
    {
        "name": "Job Portal for Truckers",
        "description": "Job portal for employee and employers with user login, job status, job expiry, employee/employer profiles. Written in Django.",
        "link": None,
        "time": "Since September 2021",
        "snip": "https://images.unsplash.com/photo-1593642531955-b62e17bdaa9c?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1469&q=80"
    },
    {
        "name": "Inventory System",
        "description": "Business inventory management, Vendor purchase/sale, Stock charts, Charts for Business analytics. Written in Django, Pandas, Matplotlib",
        "link": None,
        "time": "Since September 2021",
        "snip": "https://images.unsplash.com/photo-1593642531955-b62e17bdaa9c?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1469&q=80"
    },
    {
        "name": "Paper Trading System",
        "description": "Trade with pseudo money on real stocks. Complete user management with realtime stock data.",
        "link": None,
        "time": "Since September 2021",
        "snip": "https://images.unsplash.com/photo-1593642531955-b62e17bdaa9c?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1469&q=80"
    },
    {
        "name": "Developer Portfolio",
        "description": "Portfolio webapp written in Flask and frontend in Tailwind CSS",
        "link": None,
        "time": "Since September 2021",
        "snip": "https://images.unsplash.com/photo-1593642531955-b62e17bdaa9c?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1469&q=80"
    },
]

# Main page - Education
education = [
        {
        "name": "Accenture",
        "description": "Software Engineer - Analyst",
        "time": "Since August 2019",
        "sno": "1",
        "position": ""
    },
    {
        "name": "DIT UNIVERSITY",
        "description": "Bachelor's of Technology - IT",
        "time": "July 2015 - June 2019",
        "sno": "2",
        "position": "flex-row-reverse"
    },
    {
        "name": "DAV PUBLIC SCHOOL",
        "description": "Formal Schooling of 15 years ",
        "time": "Till 2015",
        "sno": "3",
        "position": ""
    },
]

# Main page - Technologies
technologies = [
    {"name": "Python", "color": "yellow-900", "size": "100%", "logo": "https://www.vectorlogo.zone/logos/python/python-icon.svg"},
    {"name": "Flask", "color": "gray-700", "size": "70%", "logo": "https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg"},
    {"name": "Django", "color": "green-700", "size": "50%", "logo": "https://www.vectorlogo.zone/logos/djangoproject/djangoproject-icon.svg"},
    {"name": "Pandas", "color": "yellow-600", "size": "80%", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/1200px-Pandas_mark.svg.png"},
    {"name": "Numpy", "color": "blue-700", "size": "50%", "logo": "https://www.vectorlogo.zone/logos/numpy/numpy-icon.svg"},
    {"name": "Selenium", "color": "pink-500", "size": "90%", "logo": "https://iconape.com/wp-content/png_logo_vector/selenium-logo.png"},
    {"name": "Ansible", "color": "red-700", "size": "50%", "logo": "https://www.vectorlogo.zone/logos/ansible/ansible-icon.svg"},
    {"name": "MongoDB/Postgre", "color": "blue-900", "size": "60%", "logo": "https://www.vectorlogo.zone/logos/mongodb/mongodb-icon.svg"},
    {"name": "Tailwind CSS", "color": "green-500", "size": "70%", "logo": "https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg"},
    {"name": "Tkinter", "color": "orange-500", "size": "90%", "logo": "https://wingware.com/images/large-feather.png"},
    {"name": "REST API", "color": "purple-500", "size": "50%", "logo": "https://images.squarespace-cdn.com/content/v1/5df3d8c5d2be5962e4f87890/1580626510144-Y6C73XYMHKFRTCY1TW74/apipy-logo.png?format=1000w"},
]

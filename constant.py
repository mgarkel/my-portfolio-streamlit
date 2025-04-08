info = {
    "Pronoun": "him/he",
    "Name": "Manav",
    "Full_Name": "Manav Garkel",
    "Intro": "A Software Engineer with a passion for backend development, data engineering, and ML/AI technologies, driven to build scalable, intelligent systems that solve real-world problems",
    "About": "I’m a backend-focused software engineer with a strong background in building scalable data systems, APIs, and automation pipelines. "
    "I specialize in developing robust backend services that power intelligent applications—from financial forecasting tools to cloud-native data workflows. "
    "My experience spans Python, Node.js, and Java, with expertise in databases like MongoDB, DynamoDB, and SQL-based systems. "
    "I’ve designed and deployed solutions leveraging RESTful APIs, distributed processing, and large language models (LLMs) to turn raw data into actionable insights. "
    "I’m passionate about solving complex problems at the intersection of data engineering, AI, and cloud infrastructure.",
    "City": "Alexandria, Virginia",
    "Photo": """""",
    "Email": "manav.garkel@gmail.com",
}

# TODO: Remove embedd rss and endorsements
embed_rss = {
    "rss": """<div style="overflow-y: scroll; height:500px; background-color:white;"> <div id="retainable-rss-embed" 
        data-rss="https://medium.com/feed/@vicky-note"
        data-maxcols="3" 
        data-layout="grid"
        data-poststyle="inline" 
        data-readmore="Read the rest" 
        data-buttonclass="btn btn-primary" 
        data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""
}

endorsements = {
    "img1": "https://user-images.githubusercontent.com/90204593/238169843-12872392-f2f1-40a6-a353-c06a2fa602c5.png",
    "img2": "https://user-images.githubusercontent.com/90204593/238171251-5f4c5597-84d4-4b4b-803c-afe74e739070.png",
    "img3": "https://user-images.githubusercontent.com/90204593/238171242-53f7ceb3-1a71-4726-a7f5-67721419fef8.png",
}
# TODO
# Refactor Code
# Clean up visuals
work_experience = [
    {
        "id": 1,
        "content": "Sr Software Engineer @ Freddie Mac",
        "start": "2021-05-01",
        "end": "2025-04-01",
        "title": """<ul>
                    <li>Developed a forecasting and analysis tool to reduce manual reporting, improve risk assessment accuracy, and accelerate credit decision-making for Multi-Family loans</li>
                    <li>Collaborated with stakeholders to gather data and reporting requirements for ERCF capital reporting, leading end-to-end development through UAT and production deployment</li>
                    <li>Partnering with stakeholders to gather requirements and lead end-to-end development of capital forecasting reports by integrating financial forecasting results with ERCF spot capital, from initial design to production</li>
                    <li>Maintaining codebase with 100% unit test coverage, developing integration and regression tests, conducting code reviews, and mentoring junior engineers</li>
                    <li>Developed reusable microservices and APIs to provide streamlined access to company data sources, improving developer efficiency and integration workflows</li>
                </ul>""",
        "className": "freddie",
    },
    {
        "id": 2,
        "content": "AI Software Engineer @ Selling.com",
        "start": "2023-03-01",
        "end": "2024-03-01",
        "title": """<ul>
                <li>Built a web-scraping application to automate the collection and classification of 10,000 daily news articles, enabling a new feature in the premium subscription service that provides users with actionable insights on company events</li>
                <li>Applied NER to extract company mentions and leveraged GPT-3.5/4-turbo for multi-label classification of news events (e.g., mergers, layoffs, product launches), driving structured, actionable insights from unstructured text</li>
                <li>Architected a robust, cloud-native data pipeline with AWS DynamoDB, SQS, and S3 to support scalable processing and access to enriched classification data</li>
            </ul>""",
        "className": "selling",
    },
    {
        "id": 3,
        "content": "Software Engineer @ Sync Layer Inc.",
        "start": "2021-02-01",
        "end": "2021-09-01",
        "title": """<ul>
                <li>Created a RESTful service that the main application consumes to send automated text messages to users</li>
                <li>Implemented frontend and backend functionality to provide a new phone-number lookup feature</li>
                <li>Designed and implemented a new algorithm to efficiently display data windows based on screen resolution and size</li>
            </ul>""",
        "className": "synclayer",
    },
    {
        "id": 4,
        "content": "Graduate Teaching Asst @ GMU",
        "start": "2020-08-01",
        "end": "2021-05-01",
        "title": """<ul>
                <li>Instructing lab coding sessions and holding weekly office hours for undergraduate courses teaching OOP in Python</li>
            </ul>""",
        "className": "gmu",
    },
    {
        "id": 5,
        "content": "Data Science & ML Intern @ Selling.com",
        "start": "2020-05-01",
        "end": "2020-08-01",
        "title": """<ul>
                <li>Built TF-IDF + SVM-based classification models with 90%+ accuracy to categorize 13M job titles by level and department</li>
                <li>Developed NER-based scripts to extract CEO information for 1.2M companies via web mining</li>
            </ul>""",
        "className": "selling",
    },
    {
        "id": 6,
        "content": "QA Specialist II @ Dexcom, Inc.",
        "start": "2017-02-01",
        "end": "2019-07-01",
        "title": """<ul>
                <li>Transitioned 95% of complaint code (including product and data investigations review) volume over to the Manila, Philippines office during a four-month assignment abroad</li>
                <li>Successfully trained 100+ employees and new hires for the Quality Assurance team in Manila, Philippines</li>
                <li>Led a process improvement project to identify sources of errors within product and data investigations, driving down error percentage from 12% to 5% in a duration of 10 months in conjunction with Field Failure Analysis Lab</li>
                <li>Identified a bug in the sensor algorithm in conjunction with R&D engineering team and implemented a fix to reduce sensor malfunctions by 1% (5000 sensors) each month</li>
                <li>Department liaison between Quality Assurance dept. and Field Failure Analysis Lab – worked with engineers in the lab to draft SOP’s and PI’s for failed product investigations and root cause analysis</li>
            </ul>""",
        "className": "dexcom",
    },
    {
        "id": 7,
        "content": "Research Associate @ UC San Diego",
        "start": "2016-11-01",
        "end": "2017-06-01",
        "title": """<ul>
                <li>Developed C++ code for lattice Monte Carlo simulation software to study the coarse-grained dynamics of nanoparticle diffusion and self-assembly in a polymer thin film, critical for predicting and engineering electromechanical properties of advanced nanocomposite materials</li>
                <li>Designed and executed experiments to characterize higher-order structures formed by nanoparticle diffusion and self-assembly</li>
                <li>Implemented MATLAB scripts to visualize the morphology of the structures formed</li>
                <li>Automated the simulation process with Python to generate varied initialization parameters and efficiently run and organize multiple simulations</li>
            </ul>""",
        "className": "ucsd",
    },
    {
        "id": 8,
        "content": "Student Fundraiser @ UC San Diego",
        "start": "2014-06-01",
        "end": "2015-04-01",
        "title": """<ul>
                <li>Reached out to alumni and friends of the University to raise funds for various scholarships and departments at UCSD</li>
                <li>Raised $18,000 during an 11-month span at the Telephone Outreach Program</li>
                <li>Achieved a participation (pledge) rate of 70%</li>
                <li>Awarded Top 5 Caller of the Month 8 out of 11 months in the program</li>
            </ul>""",
        "className": "ucsd",
    },
    {
        "id": 9,
        "content": "Internship @ Nielsen Company",
        "start": "2013-06-01",
        "end": "2013-08-01",
        "title": """<ul>
                <li>Successfully built Polygon 1.0, a database and reporting system, by collaborating data for 5000+ North American contractors</li>
                <li>Enabled efficient data analysis by consolidating data from various platforms including OLAP Cubes, SharePoint lists and Excel files into a single data repository in Microsoft Excel</li>
            </ul>""",
        "className": "nielsen",
    },
    {
        "id": 10,
        "content": "Management Trainee @ Nielsen Company",
        "start": "2011-07-01",
        "end": "2012-03-01",
        "title": """<ul>
                <li>Prepared monthly deliverables and invoices to be sent out to clients</li>
                <li>Assisted manager in client meetings</li>
                <li>Researched and acquired prospective clients to expand client base</li>
            </ul>""",
        "className": "nielsen",
    },
]

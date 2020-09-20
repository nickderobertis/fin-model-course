from lectures.model import LectureNotes, Lecture


def get_about_me_lecture() -> Lecture:
    title = 'About Me'
    youtube_id = 'xL0Wo14Hqbk'
    week_covered = 1
    notes = LectureNotes([
        'I am currently a Finance Ph.D. student at UF focusing on market intervention, alternative assets, '
        'and behavioral finance',
        'This is my third time teaching Financial Modeling and I taught Debt and Money Markets twice previously',
        "Undergraduate and master's degrees in Finance from Virginia Commonwealth University (VCU)",
        r'Worked as the only commercial loan portfolio analyst at a small bank (about \$1B in assets, 15 branches). '
        r'During my time there, saved the bank \$4.5 million dollars',
        'Represented VCU in the Chartered Financial Analyst (CFA) Equity Research Challenge, '
        'our team got in the top 12 out of ~800 university teams from around the world',
        'I am a strong supporter of open-source software. I develop packages as part of my research and '
        'also as part of this class.'
    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)


def get_syllabus_lecture() -> Lecture:
    title = 'Syllabus'
    youtube_id = 'k5KxoG-Oi-A'
    week_covered = 1
    notes = LectureNotes([
        "Get the textbook if you're someone who learns well from reading, and doesn't have a "
        "lot of Excel experience. Otherwise it probably won't be very helpful",
        "Mac and Windows are both fine, though I don't have much experience on Mac so I won't be as "
        "helpful with OS-specific issues",
        "This class is hard. Those who don't have good technical skills already should prepare to "
        "put a lot of work in or consider another course.",
        "We focus on the modeling process and skills, not as much on the finance, so you need to "
        "have a good knowledge of finance first.",
        "If you don't have any of the required Excel skills, take a look at the resources provided on "
        "the syllabus and ask me any questions",
        "The lab sessions are perhaps the most valuable part of the course because you can get "
        "lots of hands on feedback",
        "I have consistently heard that these are the hardest (and most rewarding) projects in the "
        "finance program at UF. Start early and ask questions.",
        "I would highly encourage those who don't have Python experience to work through some of the "
        "resources in the syllabus. This will greatly enhance your learning and allow you to focus on the "
        "models rather than struggling with programming basics.",
        "Please review the syllabus document for the grading structure",
    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)


def get_what_is_financial_modeling_lecture() -> Lecture:
    title = 'What is a Financial Model?'
    youtube_id = 'oF5M2JjF1ZQ'
    week_covered = 1
    notes = LectureNotes([
        'A model is simply a repeatable process which converts inputs to outputs',
        'The process might be as simple as a single calculation or as complicated as trying to value a '
        'large multinational company',
        'There can be one or many inputs and outputs',
        'A model is a logical and mathematical construct, it has nothing to do with Excel or Python. These '
        'are just tools we can use to implement the model',
    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)


def get_tools_and_skills_lecture() -> Lecture:
    title = 'Tools and Skills'
    youtube_id = 'D-G7DekFIvg'
    week_covered = 1
    notes = LectureNotes([
        'We will implement models in both Excel and Python in this class',
        'It is necessary to learn programming to build real-world custom models',
        'Out of programming languages, people love Python for its short(er) learning curve, readability, '
        'power, and flexibility. ',
        'Learning programming and Python has many applications outside financial modeling and proves '
        'technical competency on a resume',
        'Python, like (nearly) any other programming language, is text-based and lives in a terminal',
        "While it does get much easier to learn more languages after your first, if you're going to pick "
        "just one, it should definitely be Python over VBA",
        "Excel is not going anywhere. It has its problems, some of which are major, but it is so widespread "
        "and people are used to dealing with these problems"

    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)


def get_install_python_lecture() -> Lecture:
    title = 'Installing Python'
    youtube_id = 'Y3xQrT0oSO0'
    week_covered = 1
    notes = LectureNotes([
        'Watch this process to learn how to install Python',
        'You will only need to complete this once on a given computer',
        'The "Add Anaconda to my PATH environment variable" is very important, it will warn you '
        "that it could cause issues but it won't for our purposes, and if you leave it unchecked you "
        "may have to reinstall Python later in the course",
        'Be sure to test your installation is working',
    ], title=title)
    return Lecture(title, week_covered, notes, youtube_id=youtube_id)

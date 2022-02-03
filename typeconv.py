def typeconvo(newdf):
    # print("hlo")
    newdf.gender = newdf.gender.apply(gender)
    newdf.relevent_experience = newdf.relevent_experience.apply(relevent_experience)
    newdf.enrolled_university = newdf.enrolled_university.apply(enrolled_university)
    newdf.education_level = newdf.education_level.apply(education_level)
    newdf.major_discipline = newdf.major_discipline.apply(major_discipline)
    newdf.experience = newdf.experience.apply(experience)
    newdf.company_size = newdf.company_size.apply(company_size)
    newdf.company_type = newdf.company_type.apply(company_type)
    newdf.last_new_job = newdf.last_new_job.apply(last_new_job)
    return newdf

def gender(value):
    if value == 'Female':
        return 0
    elif value =='Male':
        return 1
    elif value == 'Other':
        return 2

def relevent_experience(value):
    if value == 'Has relevent experience':
        return 0
    elif value == 'No relevent experience':
        return 1

def enrolled_university(value):
    if value == 'Full time course':
        return 0
    elif value == 'no_enrollment':
        return 1
    else:
        return 2

def education_level(value):
    if value == 'Graduate':
        return 0
    elif value == 'High School':
        return 1
    elif value == 'Masters':
        return 2
    elif value == 'Phd':
        return 3
    elif value == 'Primary School':
        return 4

def experience(value):
    no_experience = ['0', '<1']
    beginner = ['1, 2, 3']
    intermidiate = ['4', '5', '6', '7', '8', '9']
    advanced = ['10', '11', '12', '13', '14', '15']
    if value in no_experience:
        return 0
    elif value in beginner:
        return 1
    elif value in intermidiate:
        return 2
    elif value in advanced:
        return 3
    else:
        return 4

def major_discipline(value):
    if value == 'Arts':
        return 0
    elif value == 'Business Degree':
        return 1
    elif value == 'Humanities':
        return 2
    elif value == 'No Major':
        return 3
    elif value == 'Other':
        return 4
    elif value == 'STEM':
        return 5

def company_size(value):
    if value == '01-10-1949':
        return 0
    elif value == '<10':
        return 1
    elif value == '50-99':
        return 2
    elif value == '100-500':
        return 3
    elif value == '500-999':
        return 4
    elif value == '1000-4999':
        return 5
    elif value == '5000-9999':
        return 6
    else:
        return 7

def company_type(value):
    if value == 'Early Stage Startup':
        return 0
    elif value == 'Funded Startup':
        return 1
    elif value == 'NGO':
        return 2
    elif value == 'Other':
        return 3
    elif value == 'Public Sector':
        return 4
    elif value == 'Pvt Ltd':
        return 5

def last_new_job(value):
    if value == '1':
        return 0
    elif value == '2':
        return 1
    elif value == '3':
        return 2
    elif value == '4':
        return 3
    elif value == '>4':
        return 4
    else:
        return 5
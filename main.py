from pyscript import display, document





#grades pyscript code


def getting_allat(e):
    first_name = document.getElementById('input1').value
    last_name = document.getElementById('input2').value
    va_nox_grade = float(document.getElementById('va-noxgr').value)
    pe_grade = float(document.getElementById('pegr').value)
    ict_grade = float(document.getElementById('ictgr').value)
    sci_grade = float(document.getElementById('scigr').value)
    mth_grade = float(document.getElementById('mthgr').value)
    eng_grade = float(document.getElementById('enggr').value)

    units = [5, 5, 5, 3, 1, 2]
    subjects = [sci_grade, mth_grade, eng_grade, va_nox_grade, pe_grade, ict_grade]

    total_units = sum(units)
    total_points = sum(g * u for g, u in zip(subjects, units))  
    gwa = total_points / total_units

    html = f'''
    student name: {first_name} {last_name}<br>
    <strong>grades:</strong><br>
    Science: {sci_grade}<br>
    Mathematics: {mth_grade}<br>
    English: {eng_grade}<br>
    Va-nox: {va_nox_grade}<br>
    PE: {pe_grade}<br>
    ICT: {ict_grade}<br>
    <strong>GWA:</strong> {gwa:.2f}
    ''' 

    document.getElementById('outputgrades').innerHTML = html


#club pyscript code

baseball = {
    'name of club' : 'baseball team',
    'description' : 'baseball team of the school',
    'meeting times' : 'every monday 3:00-5:00 pm',
    'location' : 'university field',
    'club moderator' : 'Ekko',
    'number of members' : 30 
}     #dictionary for the baseball club
debate = {
    'name of club' : 'debate team',
    'description' : 'a club to train the top piltovan debaters',
    'meeting times' : 'every tuesday 2:30-5:00 pm',
    'location' : 'debate hall',
    'club moderator' : 'Caitlyn Kiramman',
    'number of members' : 25 
}    #dictionary for debate club
science = {
    'name of club' : 'science club',
    'description' : 'the pinnacle of piltovers scientific minds',
    'meeting times' : 'every friday 2:00-6:00 pm',
    'location' : 'da lab',
    'club moderator' : 'Heimerdinger',
    'number of members' : 50
}    #dictionary for science club  

def display_club_info1(e):
    club_info = baseball
    bball_output = f"Club Name: {club_info['name of club']}\nDescription: {club_info['description']}\nMeeting Times: {club_info['meeting times']}\nLocation: {club_info['location']}\nClub Moderator: {club_info['club moderator']}\nNumber of Members: {club_info['number of members']}"
    document.getElementById("outputclub").innerText = bball_output

def display_club_info2(e):
    club_info = debate
    debate_output = f"Club Name: {club_info['name of club']}\nDescription: {club_info['description']}\nMeeting Times: {club_info['meeting times']}\nLocation: {club_info['location']}\nClub Moderator: {club_info['club moderator']}\nNumber of Members: {club_info['number of members']}"
    document.getElementById("outputclub").innerText = debate_output

def display_club_info3(e):
    club_info = science
    science_output = f"Club Name: {club_info['name of club']}\nDescription: {club_info['description']}\nMeeting Times: {club_info['meeting times']}\nLocation: {club_info['location']}\nClub Moderator: {club_info['club moderator']}\nNumber of Members: {club_info['number of members']}"
    document.getElementById("outputclub").innerText = science_output

def clear_club_info(e):
    document.getElementById("outputclub").innerText = ""
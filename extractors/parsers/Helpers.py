from bs4 import BeautifulSoup


def get_name(soup):
    '''
    Parse and return the name of the course
    '''
    name = soup.find(id='u19').find('span')
    return ' '.join(name.getText().split(' ')[1:]) if name else None


def get_division(soup):
    '''
    Parse and return the division of the course
    '''
    divison = soup.find('span', id='u23')
    return divison.getText().strip() if divison else None


def get_department(soup):
    '''
    Parse and return the department by which course in provided
    '''
    department = soup.find('span', id='u41')
    return department.getText().strip() if department else None


def get_prerequisites(soup):
    '''
    Parse and return the pre-requisites of the course
    '''
    prerequisites = soup.find('span', id='u50')
    return prerequisites.getText().strip().split(',') if prerequisites else None


def get_exclusion(soup):
    '''
    Parse and return the exclusions of the course
    '''
    exclusion = soup.find('span', id='u68')
    return exclusion.getText().strip().split(',') if exclusion else None


def get_courselevel(soup):
    '''
    Parse and return the level of the course
    '''
    courselevel = soup.find('span', id='u86')
    return courselevel.getText().strip() if courselevel else None


def get_campus(soup):
    '''
    Parse and return the campusat which course is provided
    '''
    campus = soup.find('span', id='u149')

    if campus:
        campus = campus.getText().strip()
        if campus == 'Scarborough':
            return 'UTSC'

        elif campus == 'St. George':
            return 'UTSG'

        elif campus == 'Mississauga':
            return 'UTM'

    return None


def get_breadth(soup):
    '''
    Parse and return the breadth requirements this course fulfills
    '''
    campus = get_campus(soup)
    if campus == 'UTSG':
        breadth = soup.find('span', id='u122')
        return ([br.strip() for br in breadth.getText().strip().split('+')]
                if breadth else None)
    elif campus == 'UTSC':
        breadth = soup.find('span', id='u104')
        return ([br.strip() for br in breadth.getText().strip().split('+')]
                if breadth else None)
    else:
        return None


def get_term(soup):
    '''
    Parse and return the term in which course is provided
    '''
    term = soup.find('span', id='u158')
    return term.getText().strip() if term else None


def get_sections(soup):
    '''
    Parse and return the information regarding each section of the course
    '''
    row_labels = ['Activity', 'Day and Time',
                  'Instructor', 'Location', 'Class Size']
    sections_info = []
    sections_table = soup.find('table', id='u172')

    tr_list = None
    if sections_table:
        tr_list = sections_table.find_all('tr')

    if tr_list:
        for tr in tr_list:
            td_list = tr.find_all('td')

            if td_list:
                section = {}
                for i in range(5):
                    data = td_list[i].find('span').getText().strip()
                    section[row_labels[i]] = data
                sections_info.append(section)

    return sections_info if sections_info else None


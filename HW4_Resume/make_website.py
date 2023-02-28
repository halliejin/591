def read_the_file(file):
    '''
    This function reads the file line by line and store the lines in a list

    This function returns the list
    '''
    # create an empty list to store the lines read
    list1 = []
    # open the file and read lines
    with open(file) as file1:
        # read the first line and strip it for further use
        line = file1.readline().strip()
        list1.append(line)

        # read lines from the file
        for line in file1:
            # skip the empty lines
            if line.isspace():
                continue
            # add the first line to the list
            list1.append(line)
    return list1


def detecting_the_name(list1):
    '''
    This function reads the first element of the resume list

    This function returns either a name or 'Invalid Name'
    '''
    # read the name from the resume list
    # strip it once again to make sure that all whitespace and leading/trailing are removed
    name = list1[0].strip()
    # check if the first letter of the name is uppercase
    if name[0] != name[0].upper():
        return 'Invalid Name'
    else:
        return name


def detecting_the_email(list1):
    '''
    This function is used to detect the email address in the resume

    This function returns either a valid email address or None
    '''
    # use a new object to store the email
    email = ''
    # read through the list to find the email address
    for i in list1:
        if '@' in i:
            email = i
    # strip once again
    email = email.strip()

    # check if the email is valid
    # check if the email contains digits
    for character in email:
        if character.isnumeric():
            return None

    len_email = len(email) - 1
    email = email.strip()
    for i in range(len_email + 1):
        # check if the email has an invalid uppercase letter after '@'
        if email[i] == '@':
            if email[i + 1] == email[i + 1].upper():
                return None

    # check if the last 3 letters are 'edu' or 'com'
    if email[-3:] == 'edu' or email[-3:] == 'com':
        return email
    else:
        return None


def detecting_the_course(list1):
    '''
    This function detects the courses listed in the resume list

    This function returns a list of cleaned courses
    '''
    # find the course item in the list
    for i in list1:
        if 'Course' in i:
            course = i
    # split the course by ',' for further handling
    course_list = course.split(',')
    # clean the whitespace
    course_list = [i.strip() for i in course_list]

    # clean the first item which include 'Course'
    first_course = course_list[0].split(':-')
    first_course = [i.strip() for i in first_course]

    # handle the random punctuation between Course and the first actual course
    l1 = first_course[1].split(' ')
    l1 = [i.strip() for i in l1]

    l2 = []
    # append the punctuations into a list
    for character in l1[0]:
        if not character.isalpha():
            l2.append(character)
    # combine the elements in the list and get the prefix that needs to be deleted
    prefix = ''.join(l2)
    prefix_len = len(prefix)
    l1[0] = l1[0][prefix_len:].strip()
    # remove the prefix
    # l1[0] = l1[0].removeprefix(prefix).strip()
    # combine the first course without prefix
    l3 = ' '.join(l1)
    course_list[0] = l3

    return course_list


def detecting_the_project(list1):
    '''
    This is a function that detects the projects in the list

    This function returns the list with cleaned project items
    '''
    start = 0
    end = 0
    for i in range(len(list1) - 1):
        # get the start of the project line
        if 'Projects' in list1[i]:
            start = i + 1
        # get the end of the project line
        if '-'*10 in list1[i]:
            end = i

    project_list = []
    # get the projects in the list
    for i in range(start, end):
        project_list.append(list1[i].strip())

    return project_list


def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.

    This function returns the html sentence of the given tag and text
    """
    # create the front tag and the back tag
    front_tag = "<" + tag + ">"
    back_tag = "</" + tag + ">\n"
    # create the text that indicates the html sentence
    texts = front_tag + text + back_tag

    # return the string with tags attached.
    return texts


def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """
    # check if the passing email address is valid
    if email_address is not None:
        address_to_split = email_address
        # replace the '@' with '[aT]' if the email address is valid
        email_list = address_to_split.split('@')
        email_address_new = '[aT]'.join(email_list)
        # generate the html sentence
        html_email = "<a href=\"mailto:" + email_address + "\">" + email_address_new + "</a>"

        return html_email
    else:
        return None


def write_name_section(list1):
    '''
    This function writes the information of the name and email

    This function returns a html sentence with basic information section
    '''
    # call the detecting and create method
    email = create_email_link(detecting_the_email(list1))
    if email is None:
        email = ""
    surrounded_email = surround_block("p", "Email: " + email)
    header_with_name = surround_block("h1", detecting_the_name(list1))
    # put it all together within "div" now.
    name_written = surround_block("div", "\n" + header_with_name + surrounded_email)

    return name_written


def write_project_section(list1):
    '''
    This function writes the information of projects

    This function returns a html sentence with projects information
    '''
    # call the detecting method to receive the project item list
    project = detecting_the_project(list1)
    # generate <h2> by calling surround_block() function
    surrounded_project = surround_block("h2", "Projects")

    projects_surrounded = []

    # loop through the projects
    for pj in project:
        # get the content of <li> blocks
        projects_surrounded.append(surround_block("li", pj))
    # combine the two elements
    projects_surrounded = "".join(projects_surrounded)

    # nest the items in the project list together and form a <ul> block
    nested_projects_surrounded = surround_block("ul", "\n" + projects_surrounded)
    # the final return sentence with tag <div>
    projects_written = surround_block("div", "\n" + surrounded_project + nested_projects_surrounded)

    return projects_written


def write_courses_section(list1):
    '''
    This function writes the information of course information, which is similar to the previous two write_ functions

    This function returns a html sentence with course information
    '''
    course = detecting_the_course(list1)
    surrounded_course = surround_block("h3", "Courses")
    course_str = ', '.join(course)
    surrounded_span = surround_block("span", course_str)
    course_written = surround_block("div", "\n" + surrounded_course + surrounded_span)

    return course_written


def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    """
    list1 = read_the_file(txt_input_file)
    list2 = ['</body>', '</html>']
    # write in
    with open("resume_template.html") as template:
        # open the template html file and write it into the new file
        with open (html_output_file, 'w') as resume_html:
            lines = template.readlines()
            lines = lines[:-2]
            resume_html.writelines(lines)

            # start to write in contents related to resume.txt
            # write in the two lines in instruction step 1
            # when </body> in line, start to write in contents to the file
            resume_html.writelines('<div id="page-wrap">\n')

            # write in name information
            resume_html.write(write_name_section(list1))
            # write in projects information
            resume_html.write(write_project_section(list1))
            # write in course information
            resume_html.write(write_courses_section(list1))

            # write in the last three lines
            resume_html.writelines('</div>\n')
            resume_html.writelines('</body>\n')
            resume_html.writelines('</html>\n')

            resume_html.close()


def main():

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    # generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    # generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    # generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    # generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    # generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    # generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    # generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()

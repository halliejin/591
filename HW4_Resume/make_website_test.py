import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_surround_block(self):
        # test text with surrounding h1 tags
        self.assertEqual("<h1>Eagles</h1>\n", surround_block('h1', 'Eagles'))

        # test text with surrounding h2 tags
        self.assertEqual("<h2>Red Sox</h2>\n", surround_block('h2', 'Red Sox'))

        # test text with surrounding p tags
        self.assertEqual('<p>Lorem ipsum dolor sit amet, consectetur ' +
                         'adipiscing elit. Sed ac felis sit amet ante porta ' +
                         'hendrerit at at urna.</p>\n',
                         surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna.'))

    def test_create_email_link(self):

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',
            create_email_link('lbrandon@wharton.upenn.edu')
        )

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',
            create_email_link('krakowsky@outlook.com')
        )

        # test email without @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',
            create_email_link('lbrandon.at.seas.upenn.edu')
        )

    def test_detecting_the_name(self):
        # test name with the first letter of lower case
        self.assertEqual('Invalid Name', detecting_the_name(['bRandon']))

        # test name with the first letter of upper case
        self.assertEqual('BRandon', detecting_the_name(['BRandon']))

        # test name with whitespaces with the first letter of upper case
        self.assertEqual('BRandon', detecting_the_name(['   BRandon   ']))

        # test name with whitespaces with the first letter of lower case
        self.assertEqual('Invalid Name', detecting_the_name(['   bRandon   ']))

    def test_detecting_the_email(self):
        # test email with whitespaces
        self.assertEqual('brandon@upenn.edu', detecting_the_email(['course', '   brandon@upenn.edu  ', '234']))

        # test email with invalid uppercase
        self.assertEqual(None, detecting_the_email(['course', 'brandon@Upenn.edu', '234']))

        # test email with invalid digits
        self.assertEqual(None, detecting_the_email(['course', 'brandon4@Upenn.edu', '234']))

        # test email ends with strings other than 'edu' or 'com'
        self.assertEqual(None, detecting_the_email(['course', 'brandon@Upenn.org', '234']))

    def test_detecting_the_course(self):
        # test courses with whitespaces
        self.assertListEqual(['Programing and Computing', 'Lottery'],
                         detecting_the_course(['Course :-     Programing and Computing ,  Lottery   ', 'Projects', 'Math', 'English', '-' * 10, '112233']))
        # test courses with random punctuations
        self.assertListEqual(['Programing and Computing', 'Lottery'],
                         detecting_the_course(
                             ['Course :-+*/-+*()+-*/+Programing and Computing ,  Lottery   ', 'Projects', 'Math', 'English',
                              '-' * 10, '112233']))

    def test_detecting_the_project(self):
        # test whether the function returns the correct project list
        self.assertListEqual(['Math', 'English'],
                         detecting_the_project(['course', 'Projects', 'Math', 'English', '-' * 10, '112233']))

        # test projects with whitespaces
        self.assertListEqual(['Math', 'English'],
                         detecting_the_project(['course', 'Projects', '  Math  ', '  English  ', '-' * 10, '112233']))

    def test_write_name_section(self):
        # test the name with a lowercase letter as the first letter
        self.assertEqual('<div>\n<h1>Invalid Name</h1>\n<p>Email: <a href="mailto:tonyl@seas.upenn.edu">tonyl['
                         'aT]seas.upenn.edu</a></p>\n</div>\n',
                         write_name_section(['bRanton', 'Course', 'tonyl@seas.upenn.edu']))

        # test the nme with an uppercase letter as the first letter
        self.assertEqual('<div>\n<h1>Brandon Bran</h1>\n<p>Email: <a href="mailto:tonyl@seas.upenn.edu">tonyl['
                         'aT]seas.upenn.edu</a></p>\n</div>\n',
                         write_name_section(['Brandon Bran', 'Course', 'tonyl@seas.upenn.edu']))

    def test_write_project_section(self):
        # test if the project returns the correct html sentences
        # the test of project input without whitespaces is done by test_detecting_the_course(self) function
        self.assertEqual('<div>\n<h2>Projects</h2>\n<ul>\n<li>Math</li>\n<li>English</li>\n</ul>\n</div>\n',
                         write_project_section(['I.M. Student', 'Courses :- Programming Languages and Techniques, '
                                                                'Biomedical image analysis, Software Engineering\n',
                                                'Projects\n', 'Math\n', 'English\n',
                                                '------------------------------\n', 'tonyl@seas.upenn.edu\n']))

    def test_write_courses_section(self):
        # test if the course returns the correct html sentences
        # the test of course input without whitespaces and punctuations is done by test_detecting_the_course(self) function
        self.assertEqual('<div>\n<h3>Courses</h3>\n<span>Math, English</span>\n</div>\n',
                         write_courses_section(['Courses :- Math, English', 'Projects']))

if __name__ == '__main__':
    unittest.main()

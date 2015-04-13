from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # John's fucking stupid, and can't remember anything.
    # He goes online to find a to-do app.
    self.browser.get('http://localhost:8000')

    # He looks for "To-Do" in the title, otherwise how would he know what the site is?
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')

    # The site tells him to enter a thing, he does.

    # He types "Learn to read" into the prompt

    # The page updates, and he sees some text he doesn't know how to read.

    # He sees a box for more typing. He enters "Learn Math"

    # Suddenly, there are TWO texts he can't read.

    # He wonders how on earth he'll remember that, when he finds out the site
    # made a URL just for him. SOMEONE loves John.

    # He goes to that URL and finds the pretty letters.

    # He cries himself to sleep.

if __name__ == "__main__":
  # If executed from command line
  unittest.main(warnings='ignore')

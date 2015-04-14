from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # John"s a little stupid, and can"t remember anything.
    # He goes online to find a to-do app.
    self.browser.get("http://localhost:8000")

    # He looks for "To-Do" in the title and header, otherwise how would he know what the site is?
    self.assertIn("To-Do", self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    # The site tells him to enter a thing, he does.
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
    )

    # He types "Learn to read" into the prompt
    inputbox.send_keys('Learn to read')
    inputbox.send_keys(Keys.ENTER)

    # The page updates, and he sees some text he doesn't know how to read.
    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_element_by_tag_name('tr')
    self.assertTrue(
      any(row.text == '1: Learn to read' for row in rows)
    )

    # He sees a box for more typing. He enters "Learn Math"
    self.fail('Finish the test!')

    # Suddenly, there are TWO texts he can't read.

    # He wonders how on earth he'll remember that, when he finds out the site
    # made a URL just for him. SOMEONE loves John.

    # He goes to that URL and finds the pretty letters.

    # He cries himself to sleep.

if __name__ == "__main__":
  # If executed from command line
  unittest.main(warnings="ignore")

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "7f73c02d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select\n",
      "White\n",
      "Black\n",
      "African American\n",
      "American Indian\n",
      "Alaska Naitive\n",
      "Asian\n",
      "Hispanic\n",
      "Native Hawaiian\n",
      "Other Pacific Islander\n",
      "Other/Unspecified\n",
      "True\n",
      "True\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "object of type 'WebElement' has no len()",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-41-d4f0c52ffb7d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     99\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    100\u001b[0m \u001b[0mboxes\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCLASS_NAME\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m'form-group'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 101\u001b[0;31m \u001b[0mNUMBER\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mboxes\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    102\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    103\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: object of type 'WebElement' has no len()"
     ]
    }
   ],
   "source": [
    "#Automation of carespan.io\n",
    "\n",
    "import selenium\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support.ui import Select\n",
    "\n",
    "import time\n",
    "\n",
    "driver=webdriver.Chrome(executable_path = \"/home/trainee/Desktop/chromedriver\")\n",
    "driver.get(\"https://carespan.io\")\n",
    "\n",
    "driver.maximize_window()\n",
    "\n",
    "# login into account\n",
    "login=driver.find_element_by_xpath(\"//*[@id='collapsibleNavbar']/ul[2]/li[1]/a\").click()\n",
    "driver.find_element_by_id(\"email\").send_keys(\"doctor@gmail.com\")\n",
    "driver.find_element_by_id(\"typepass\").send_keys(\"admin@123\")\n",
    "driver.find_element_by_xpath(\"//*[@id='form-']/div[4]/button\").click()\n",
    "time.sleep(5)\n",
    "driver.execute_script(\"window.scrollBy(0,500)\",\"\")\n",
    "element=driver.find_element_by_xpath(\"//*[@id='collapsibleNavbar']/ul[2]/li[2]/a\").click()\n",
    "time.sleep(3)\n",
    "driver.find_element_by_xpath(\"//*[@id='collapsibleNavbar']/ul[2]/li[2]/div/a[2]\").click()\n",
    "\n",
    "time.sleep(5)\n",
    "\n",
    "# Clicking on Patient button and adding a new patient\n",
    "\n",
    "patients = driver.find_element_by_xpath(\"//*[@id='ga-asidebar']/div/div/div/div[2]/nav/ul/li[2]/a\").click()\n",
    "time.sleep(4)\n",
    "add_new = driver.find_element_by_xpath(\"/html/body/div[1]/section/div/div/div[2]/div/div[1]/h2/span/a\").click()\n",
    "\n",
    "# Filling the patient form\n",
    "\n",
    "name = driver.find_element_by_id(\"name\").send_keys(\"John\")\n",
    "Email = driver.find_element_by_id(\"email\").send_keys(\"John@gmail.com\")\n",
    "Mobile = driver.find_element_by_id(\"phone\").send_keys(\"6278455865\")\n",
    "phone = driver.find_element_by_id(\"hphone\").send_keys(\"Not Applicable\")\n",
    "Dob = driver.find_element_by_id(\"datefield\").send_keys(\"11/02/1977\")\n",
    "zipfield = driver.find_element_by_id(\"zip\")\n",
    "# page scrolling\n",
    "scroll_page = driver.execute_script(\"window.scrollBy(0,750)\",\"\")\n",
    "\n",
    "# dropdown\n",
    "\n",
    "element = driver.find_element_by_id(\"race\")\n",
    "\n",
    "drp = Select(element)\n",
    "\n",
    "drp.select_by_visible_text(\"Asian\")\n",
    "\n",
    "# capture all dropdown options\n",
    "\n",
    "all_options = drp.options\n",
    "for option in all_options:\n",
    "    print(option.text)\n",
    "\n",
    "# FILLING DESCRIPTION\n",
    "\n",
    "driver.find_element_by_id(\"icd10\").send_keys(\"The patient is having mild fever\")\n",
    "\n",
    "# dropdown\n",
    "\n",
    "element_two = driver.find_element_by_id(\"gender\")\n",
    "drp = Select(element_two)\n",
    "drp.select_by_index(1)\n",
    "\n",
    "driver.find_element_by_xpath(\"//*[@id='address']\").send_keys(\"H.no 10 Sector 45 \")\n",
    "driver.find_element_by_id(\"city\").send_keys(\"Chandigarh\")\n",
    "\n",
    "driver.find_element_by_id(\"state\").send_keys(\"Chandigarh\")\n",
    "\n",
    "# Assign wing dropdown\n",
    "element_three = driver.find_element_by_id(\"wing\")\n",
    "drp = Select(element_three)\n",
    "drp.select_by_index(1)\n",
    "\n",
    "# Submit the form\n",
    "driver.execute_script(\"window.scrollBy(0,500)\",\"\")\n",
    "\n",
    "driver.find_element_by_xpath(\"/html/body/div[1]/section/div/div/div[2]/div/div[3]/button\").click()\n",
    "\n",
    "time.sleep(3)\n",
    "\n",
    "\n",
    "# upload a file using pathname\n",
    "\n",
    "driver.find_element_by_xpath(\"//*[@id='ga-asidebar']/div/div/div/div[2]/form/div/div/input\").send_keys(\"/home/trainee/Desktop/zomato tests.xlsx\")\n",
    "#driver.find_element_by_xpath(\"//*[@id='ga-asidebar']/div/div/div/div[2]/form/div/div/div/button\").click()\n",
    "\n",
    "#assert if dashboard button is enabled\n",
    "\n",
    "dashboard = driver.find_element_by_xpath(\"//*[@id='ga-asidebar']/div/div/div/div[2]/nav/ul/li[1]/a/span\")\n",
    "\n",
    "print(dashboard.is_enabled())\n",
    "print(dashboard.is_displayed())\n",
    "\n",
    "# Checking how many input boxes\n",
    "\n",
    "boxes = driver.find_element(By.CLASS_NAME,'form-group')\n",
    "NUMBER = print(len(boxes))\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# # #working with links\n",
    "# links = driver.find_elements(By.TAG_NAME,\"a\")\n",
    "# print(len(links))\n",
    "\n",
    "# # for link in links:\n",
    "#     print(link.text)\n",
    "\n",
    "# # driver.find_element(By.LINK_TEXT,\"Signed Records\").click()\n",
    "# # time.sleep(5)\n",
    "# # print(driver.current_window_handle)\n",
    "# # print(driver.window_handles)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dcb15df6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# skipping tests\n",
    "\n",
    "Class Mobile(unittest.TestCase):\n",
    "@unittest.Skip(\"I am skipping this test\")\n",
    "def apptesting(self):\n",
    "    print(\"this is a skip test\")    \n",
    "    \n",
    "def hello(self):\n",
    "    prinnt(\" Print hello\")\n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    unittest.main"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75dc998a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# asssertions\n",
    "\n",
    "def name(self):\n",
    "    driver = webdriver.Chrome(executable_path = \"    \")\n",
    "    url = driver.get(\"https\")\n",
    "    title = driver.title\n",
    "    self.assertTrue(title = \" \")\n",
    "    \n",
    "# asserIn and assertNotIn\n",
    "\n",
    "Class Mobile_testing(unittest.TestCase):\n",
    "    def test(self):\n",
    "        list = [\"hello\",\"bye\",\"jelo\"]\n",
    "        self.assertIn(\"bye\",list)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

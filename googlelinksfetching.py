{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc1b71e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Code to fetch google url using selenium\n",
    "\n",
    "import selenium\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "import time\n",
    "from selenium.webdriver.common.by import By\n",
    "\n",
    "driver = webdriver.Chrome(executable_path = \"/home/trainee/Desktop/chromedriver\")\n",
    "driver.maximize_window()\n",
    "\n",
    "driver.get(\"https://www.google.com\")\n",
    "searchbox = driver.find_element_by_xpath(\"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input\").send_keys(\"Top car making companies in the world\")\n",
    "Enter = driver.find_element_by_xpath(\"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]\").click()\n",
    "\n",
    "# weblinks = driver.find_elements(By.CLASS_NAME,'LC20lb DKV0Md')\n",
    "\n",
    "for element in driver.find_elements_by_xpath('//div[@class=\"tF2Cxc\"]'):\n",
    "    link = element.find_element_by_xpath('.//div[@class=\"yuRUbf\"]/a')\n",
    "    link.get_attribute(\"href\")\n",
    "    print(link.get_attribute(\"href\"))"
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

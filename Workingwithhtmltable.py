{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fadc17fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "235\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'list' object has no attribute 'text'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-de8c3459f847>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     26\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mr\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     27\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mc\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 28\u001b[0;31m         \u001b[0mvalue\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_elements_by_xpath\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"//*[@id='example2']/tbody/tr[\"\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m\"]/td[\"\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;34m\"]\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     29\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mend\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0;34m'    '\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     30\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'list' object has no attribute 'text'"
     ]
    }
   ],
   "source": [
    "#code to fetch contents of a table\n",
    "\n",
    "import selenium\n",
    "from selenium import webdriver\n",
    "import time\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.support.ui import Select\n",
    "from selenium.webdriver import ActionChains\n",
    "\n",
    "driver = webdriver.Chrome(executable_path = \"/home/trainee/Desktop/chromedriver\")\n",
    "driver.maximize_window()\n",
    "\n",
    "url= driver.get(\"https://www.worldometers.info/world-population/population-by-country/\")\n",
    "\n",
    "# driver.implicitly_wait(6)\n",
    "time.sleep(5)\n",
    "\n",
    "rows = driver.find_elements_by_xpath(\"//*[@id='example2']/tbody/tr\")\n",
    "cols = driver.find_elements_by_xpath(\"//*[@id='example2']/thead/tr/th\")\n",
    "time.sleep(5)\n",
    "print(len(cols))\n",
    "print(len(rows))\n",
    "time.sleep(3)\n",
    "\n",
    "for r in range(1,10):\n",
    "    for c in range(1,10):\n",
    "        value = driver.find_elements_by_xpath(\"//*[@id='example2']/tbody/tr[\"+str(r)+\"]/td[\"+str(c)+\"]\").text\n",
    "        print(value,end= '    ')\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c42f052f",
   "metadata": {},
   "outputs": [],
   "source": []
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

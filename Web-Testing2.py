import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import matplotlib.pyplot as plt
import numpy as np
import time
import requests
import os
import subprocess
import time
from pathlib import Path

WEB_BROWSER_TYPE = 'FF'

VERSIONS_LIST_1=['firefox-61.0','firefox-60.0.2','firefox-60.0.1','firefox-60.0','firefox-59.0.3','firefox-59.0.2','firefox-59.0.1','firefox-59.0', 'firefox-58.0.2','firefox-58.0.1','firefox-58.0','firefox-57.0.3','firefox-57.0.2','firefox-57.0.1']	
VERSIONS_LIST_2 = ['firefox-56.0.2' ,'firefox-56.0.1','firefox-56.0','firefox-55.0.2' ,'firefox-55.0.1','firefox-55.0','firefox-54.0.1','firefox-54.0']
VERSIONS_LIST_3 = ['firefox-50.0.2','firefox-50.0.1','firefox-50.0','firefox-48.0.2',
'firefox-48.0.1','firefox-48.0','firefox-47.2','firefox-47.1','firefox-47.0','firefox-46.0.1','firefox-46.0','firefox-45.0.2','firefox-45.0.1','firefox-45.0']	
#,'firefox-49.0','firefox-49.0.2''firefox-49.0.1'
def run_giphy_reactions_test(version_folder_path):
	binary = FirefoxBinary(f'/home/user1/Desktop/Firefox/{version_folder_path}/firefox-bin')
	browser = webdriver.Firefox(firefox_binary=binary)
	#print('Im in run_giphy_reactions_test')
	start_time=time.time()
		#Open the link #giphy.com/reactions and open in new tap
	browser.execute_script("window.open('https://giphy.com/reactions');")
		#sleep(5)
	#elem1=browser.find_element_by_link_text('Sports')
	#elem1.click()
	end_time = time.time()	
	diff_time = end_time - start_time
	#time.sleep(2)
	browser.quit()
	return diff_time

def run_generic_web_test_with_cache(version_folder_path, url):
	binary = FirefoxBinary(f'/home/user1/Desktop/Firefox/{version_folder_path}/firefox-bin')
	browser = webdriver.Firefox(firefox_binary=binary)
	print('Im in run_generic_web_test')

	print('Opening url uncached...')
	browser.execute_script( f"window.open('{url}');")
	#time.sleep(5)	
	
	print('Opening url cached...')
	start_time = time.time()
	#browser.execute_script( f"window.open('{url}');")
	browser.get( f"{url}")
	end_time = time.time()	
	
	diff_time = end_time - start_time
	browser.quit()

	return diff_time
	

def run_generic_web_test(version_folder_path, url):
	binary = FirefoxBinary(f'/home/user1/Desktop/Firefox/{version_folder_path}/firefox-bin')
	browser = webdriver.Firefox(firefox_binary=binary)
	print('Im in run_generic_web_test')
	start_time = time.time()
	browser.execute_script( f"window.open('{url}');")
	end_time = time.time()	
	diff_time = end_time - start_time
	browser.quit()

	return diff_time


def make_output_file_name(url):
	return url.replace('/', '').replace('https:', '').replace('http:','').replace('.com', '')

#Static 
def run_all_tests(test_function, args = ()):
	test_count = 0
	run_times = []
	print('run_all_tests')
	# run group 1 tests
	for version in VERSIONS_LIST_1:
		test_count = test_count + 1
		print(f'Running test {test_count}...')
		subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
		subprocess.call( "tar -xf /home/user1/Desktop/Firefox/21/21.tar.gz --directory /home/user1/Desktop/Firefox/21/",shell=True)
		subprocess.call( "sudo mv /home/user1/Desktop/Firefox/21/geckodriver  /usr/bin/",shell=True)
		if len(args) > 0:
			run_times.append(test_function(version, args))
		else:
			run_times.append(test_function(version))

	# run group 2 tests
	for version in VERSIONS_LIST_2:
		test_count = test_count + 1
		print(f'Running test {test_count}...')
		subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
		subprocess.call( "tar -xf /home/user1/Desktop/Firefox/19/19.tar.gz --directory /home/user1/Desktop/Firefox/19/",shell=True)
		subprocess.call( "sudo mv /home/user1/Desktop/Firefox/19/geckodriver  /usr/bin/",shell=True)
		if len(args) > 0:
			run_times.append(test_function(version, args))
		else:
			run_times.append(test_function(version))
	
	# run group 3 tests
	for version in VERSIONS_LIST_3:
		test_count = test_count + 1
		print(f'Running test {test_count}...')
		
		subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
		subprocess.call( "tar -xf /home/user1/Desktop/Firefox/15/15.tar.gz --directory /home/user1/Desktop/Firefox/15/",shell=True)
		subprocess.call( "sudo mv /home/user1/Desktop/Firefox/15/geckodriver  /usr/bin/",shell=True)
		if len(args) > 0:
			run_times.append(test_function(version, args))
		else:
			run_times.append(test_function(version))

	return run_times

def create_csv(output_filename, run_times):
	
	if os.path.exists(output_filename + '.csv'):
		os.remove(output_filename + '.csv')
	with open(output_filename + '.csv', 'a') as csvfile:
		writer = csv.writer(csvfile,lineterminator= '\n')
		writer.writerow(VERSIONS_LIST_1 + VERSIONS_LIST_2 + VERSIONS_LIST_3)	
		writer.writerow(run_times)

#Static 
def create_plot_from_csv(csv_filename, output_filename, title, row = 1):
	y_axis_list = []
	with open(csv_filename + '.csv', 'r') as csvfile:
		reader = csv.reader(csvfile,lineterminator= '\n')
		y_axis_list = list(reader)[row]

	y_axis_list = list(map(float, y_axis_list))
	create_plot(output_filename, title, y_axis_list)
			
	
def create_plot(output_filename, title, run_times):
	plot_x_ticks = ['61\n.0','60\n.0','60\n0.1','60\n.0.2','59\n0','59\n0.1','59\n0.2','59\n0.3','58\n0','58\n0.1','58\n0.2','57\n0.1','57\n0.2','57\n0.3','56\n0','56\n0.1','56\n0.2','55\n0','55\n0.1','55\n0.2','54\n0','54\n0.1','50\n0','50\n0.1','50\n0.2','49\n0','49\n0.1','49\n0.2','48\n0','48\n0.1','48\n0.2','47\n0','47\n1','47\n2','46\n0','46\n0.1','45\n0','45\n0.1','45\n0.2'] 	
	run_times = [round(i, 4) for i in run_times]
	

	plt.figure(figsize=(15,10))
	plt.title(title)
	plt.xticks(list(range(0, len(plot_x_ticks))), plot_x_ticks, fontsize=10, rotation=20)
	plt.plot(list(range(0, len(plot_x_ticks))), run_times)

	if WEB_BROWSER_TYPE == 'FF':
		plt.xlabel('Firefox Version')

	plt.ylabel('Time (s)')
	#plt.show()
	plt.savefig(output_filename + '.png')

def main():
	'''
	# Example: running generic page load tests. No extra clicking, typing, interactions involved
	run_times_fox_news = run_all_tests(run_generic_web_test, 'http://www.foxnews.com/')
	
	# Example:  specific test
	run_times_giphy = run_all_tests(run_giphy_reactions_test)
	
	 Example: creating csvs
	create_csv('foxnewstest', run_times_fox_news)
	create_csv('giphytest', run_times_giphy)	
	
	# Example: creating plot from run_time data
	create_plot(output_filename='foxnewstest', title='title', run_times=run_times_fox_news)

	# Example: creating plot from csv
	create_plot_from_csv(csv_filename='giphytest', output_filename'giphytest', title='Title')
	'''

	#run_times_fox_news = run_all_tests(run_generic_web_test, 'https://www.sling.com/')

	#create_csv('foxnewstest', run_times_fox_news)
	#create_plot_from_csv(csv_filename='foxnewstest', output_filename='foxnewstest', title='NSF')
	'''
	create_csv('slingtest', run_times_fox_news)
	create_plot(output_filename='slingtest', title='sling', run_times=run_times_fox_news)
	'''
	''''
	run_times_giphy = run_all_tests(run_giphy_reactions_test)
	create_plot(output_filename='giphy_test2', title='iphy', run_times=run_times_giphy)
	create_csv('giphytest2', run_times_giphy)
	'''
	#FoxNews
	'''
	run_times_fox_news = run_all_tests(run_generic_web_test, 'http://www.foxnews.com/')
	create_csv('foxnewstest4', run_times_fox_news)
	create_plot(output_filename='foxnewstest5', title='Fox News', run_times=run_times_fox_news)
	'''
	#Cisco
	'''
	run_times_fox_news = run_all_tests(run_generic_web_test, 'https://www.cisco.com/')
	create_csv('Ciscotest2', run_times_fox_news)
	create_plot(output_filename='Ciscotest5', title='Cisco', run_times=run_times_fox_news)
	'''
	#theguardian
	'''
	run_times_fox_news = run_all_tests(run_generic_web_test, 'https://www.theguardian.com/uk-news')
	create_csv('theguardian2', run_times_fox_news)
	create_plot(output_filename='Theguardian2', title='The Guardian', run_times=run_times_fox_news)
	'''
	#Sling
	'''
	run_times_fox_news = run_all_tests(run_generic_web_test, 'https://www.sling.com/')
	create_csv('slingTest2', run_times_fox_news)
	create_plot(output_filename='slingTest2', title='Sling', run_times=run_times_fox_news)
	'''
	#NSF
	#run_times_fox_news = run_all_tests(run_generic_web_test, 'https://nsf.gov/awardsearch/showAward?AWD_ID=1118043&HistoricalAwards=false')
	#create_csv('NSFTest3', run_times_fox_news)
	#create_plot(output_filename='NSFTest4', title='NSF', run_times=run_times_fox_news)
	
	'''
	run_times_fox_news = run_all_tests(run_generic_web_test, 'https://www.theguardian.com/uk-news')
	create_csv('theguardian4', run_times_fox_news)
	create_plot(output_filename='Theguardian4', title='The Guardian', run_times=run_times_fox_news)	
	'''

	# NSF with Cache
	run_times_fox_news = run_all_tests(run_generic_web_test_with_cache, 'https://www.theguardian.com/uk-news')
	create_csv('Theguardian_cached', run_times_fox_news)
	create_plot(output_filename='Theguardian_cached', title='The Guardian (Cached)', run_times=run_times_fox_news)	
	
		
main()
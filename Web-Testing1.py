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
import time
import requests
import os
import subprocess

list=[]

def firefox(Foldername):
      
	
	print(Foldername)
	binary = FirefoxBinary(f'/home/user1/Desktop/Firefox/{Foldername}/firefox-bin')
	print(f'/home/user1/Desktop/Firefox/{Foldername}/firefox-bin')
	cap = DesiredCapabilities().FIREFOX
	cap["marionette"] =False
	browser = webdriver.Firefox(firefox_binary=binary)


	#browser.maximize_window()

			
	
	#find the link that has the below text and click in search

	start_time=time.time()
	browser.get('https://giphy.com/explore/the-best')
	 	# Save the window opener (current window, do not mistaken with tab... not the same)
	main_window = browser.current_window_handle
	T1=time.time()-start_time
		#writer.writerow([repr(T1)])
	print("Tab1 =====  %s seconds  ===== click the link from search result "%(T1))
	
	start_time=time.time()
		#Open the link #giphy.com/reactions and open in new tap
	browser.execute_script("window.open('https://giphy.com/reactions');")
		#sleep(5)
	elem1=browser.find_element_by_link_text('Sports')
	elem1.click()
	T2=time.time()-start_time
	       
		#writer.writerow([repr(time.time()-start_time)])
	print("Tab3 ===== %s seconds  ===== go to Reactions & click sports "%(time.time()-start_time))

	start_time=time.time()
	browser.execute_script("window.open('https://nsf.gov/awardsearch/showAward?AWD_ID=1118043&HistoricalAwards=false');")
	T3=time.time()-start_time
	print("Tab4 ===== %s seconds  =====NSF "%(time.time()-start_time) )
	browser.switch_to_window(browser.window_handles[1])
	#writer.writerow(repr(time.time()-start_time)	
	
		
    #T=("%.4f"%T1)+
	list.append("%.4f"%T1)
	list.append("%.4f"%T2)
	list.append("%.4f"%T3)
		
	
	for x in range (10):
		    
		    #time.sleep(3)
		    start_time=time.time()
		    browser.execute_script("window.open('https://www.youtube.com/watch?v=JZUX3n2yAzY');")
		    #Var[x]=time.time()-start_time
		    #writer.writerow(repr(time.time()-start_time))
		    list.append("%.4f" %(time.time()-start_time)) 		
		    print("=====%s seconds  =====Tab"+repr(x+5)+ "  "+repr((time.time()-start_time)))
		    #time.sleep(3)


	#print (list)

	with open('foxloop2.cvs', 'a') as csvfile:
		writer = csv.writer(csvfile,lineterminator= '\n')	

		writer.writerow(Foldername)
		writer.writerow([list])

	browser.quit()




#firefox-57.0' has issuee#   and 'firefox-55.0.3
# ff 54 dose not work with browser.maximize_window()


def group0():	
	list1=['firefox-61.0','firefox-60.0.2','firefox-60.0.1','firefox-60.0','firefox-59.0.3','firefox-59.0.2','firefox-59.0.1','firefox-59.0', 'firefox-58.0.2','firefox-58.0.1','firefox-58.0','firefox-57.0.1','firefox-57.0.2','firefox-57.0.3']
	                                                                       
	for i in range(len(list1)): 
		firefox(list1[i])


	

def group1():
#change to Driver Version 19 for the foloowing FF versions
	#subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
	#subprocess.call( "sudo mv /home/user1/Desktop/Firefox/19/geckodriver  /usr/bin/ ", shell=True)

	list2=['firefox-56.0.2' ,'firefox-56.0.1','firefox-56.0','firefox-55.0.2' ,'firefox-55.0.1','firefox-55.0','firefox-54.0.1','firefox-54.0']
	for i in range(len(list2)): 
		firefox(list2[i])


#change to Driver Version 18 for the foloowing FF versions
def group2():
	list3=	['firefox-50.0.2','firefox-50.0.1','firefox-50.0','firefox-49.0.2','firefox-49.0.1','firefox-49.0','firefox-48.0.2','firefox-48.0.1','firefox-48.0','firefox-47.2','firefox-47.1','firefox-47.0','firefox-46.0.1','firefox-46.0','firefox-45.0.2','firefox-45.0.1','firefox-45.0']
	
	subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
	subprocess.call( "sudo mv /home/user1/Desktop/Firefox/18/geckodriver  /usr/bin/ ", shell=True)

	for i in range(len(list3)): 
			firefox(list3[i])



def  group3():
	list4=['firefox-44.0','firefox-44.0.1','firefox-44.0.2']
	#subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
	#subprocess.call( "sudo mv /home/user1/Desktop/Firefox/14/geckodriver  /usr/bin/ ", shell=True)

	#selenium.common.exceptions.WebDriverException: Message: Unsupported Marionette protocol version 2, required 3
	#With Driver Version 14 and capabilities

	for i in range(len(list4)): 
		firefox(list4[i])



def main():
	
	for i in range(4): 
		#if (i==0):
			#subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
			#subprocess.call( "sudo mv /home/user1/Desktop/Firefox/21/geckodriver  /usr/bin/",shell=True)
			#group0()

		#if (i==1):
			#subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
			#subprocess.call( "sudo mv /home/user1/Desktop/Firefox/19/geckodriver  /usr/bin/",shell=True)
			#group1()


		if (i==2):
			subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
			subprocess.call( "sudo mv /home/user1/Desktop/Firefox/14/geckodriver  /usr/bin/",shell=True)
			group3()	
		



main()

#subprocess.Popen(['rm', '-rf', ' /usr/bin/geckodriver'])
#subprocess.call( "sudo mv /home/user1/Desktop/Firefox/21/geckodriver  /usr/bin/ ", shell=True)
#group1()










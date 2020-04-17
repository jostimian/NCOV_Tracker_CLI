print("much better if you maximize your terminal")
import COVID19Py
import time
import pandas as pd
import sys
def loop():
	covid19 = COVID19Py.COVID19(data_source="jhu")
	def fight_corona(conf_list):
	    d = pd.DataFrame.from_dict(conf_list)
	    d = pd.concat([d, d['coordinates'].apply(pd.Series),d['latest'].apply(pd.Series)], axis=1)
	    d.drop(columns= ['coordinates', 'latest'], inplace= True)
	    return d
	def confirmedCases():
		print("Please wait while we extract data in JHU's database")
		locations = covid19.getLocations(rank_by='confirmed')
		df = fight_corona(locations)
		df.to_excel("ConfirmedCases.xlsx")
		print("It is saved in ConfirmedCases.xlsx")
		loop()
	def findByCountryCode():
		countryCode = input("Add a country code eg.(PH, CN, US, PK)")
		find = covid19.getLocationByCountryCode(countryCode)
		df = fight_corona(find)
		df.to_excel(countryCode + ".xlsx")
		print("saved in " + countryCode + ".xlsx")
		loop()

	print("""
		                                                                                                                                                                                                        
	                                                                                                                                                                                                        
	            #@@&*           %@@%                                                                                  *&@&*                                #@@&*                                            
	       ,@@@@(  .(@@     &@@@/  %@@@#   @@@.         &@@   (@@@@@@@@@@@#    @@@@@@@@@@@@       ,@@@@@@/        .@@@    *@@@                        ,@@@@(  .(@@     ,@@/             @@@@@@@@@@@@        
	      @@@.             @@@        @@@   @@@        #@@.        &@@         @@#       (@@#    #%   /@@/       .@@(       @@@                      @@@.              ,@@/                 .@@#            
	     #@@.             @@@         *@@/   @@@      /@@.         &@@         @@#        &@@         /@@/       ,@@(       ,@@*                    #@@.               ,@@/                 .@@#            
	     @@@              @@&         .@@#   .@@&    ,@@*          &@@         @@#        *@@*        /@@/        /@@@#  .&@@@@/                    &@@                ,@@/                 .@@#            
	     &@@.             @@@         ,@@/    .@@#   @@#           &@@         @@#        #@@.        /@@/                  /@@                     &@@.               ,@@/                 .@@#            
	     .@@@             (@@(        @@@      /@@* @@@            &@@         @@#       (@@(         /@@(                 /@@,                     .@@@               ,@@/                 .@@#            
	       @@@@.     ,@    ,@@@*    @@@%        %@@&@@             &@@         @@#   ,&@@@@           *@@/            .#@@@@&                         @@@@,     .@     ,@@/                 .@@#            
	          %@@@@@@(        (@@@@@%            @@@@         (@@@@@@@@@@@#    @@@@@&#.          %@@@@@@@@@@@@    ,@@@%*                                 %@@@@@@#      ,@@@@@@@@@@@.    @@@@@@@@@@@@        
	                                                                                                                                                                                                        
	                                                                                                                             &@@@@@@@@@@@@@@@@@                                                         
	         Made By Timothy Ganoza ╰(*°▽°*)╯                                                                                                                                                                                               
	                                                                                                                                                                                                        

		""")

	print("""
		1. Confirmed case and deaths world wide
		2. Confirmed case and deaths in your country eg.(PH)
		3. Quit
		""")
	userInput = input("Please Pick Using The Number Before The Operation")
	if userInput == "1":
		confirmedCases()
	elif userInput == "3":
		sys.exit()
	elif userInput == "2":
		findByCountryCode()


loop()
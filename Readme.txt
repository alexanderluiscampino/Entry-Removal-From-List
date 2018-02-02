:: This routine will create the files to send DMs and Gifts to users. ::
::  Version 1 :: 
::  Created by ALexandre Campino :: 
::  Date Created 12/11/2017 :: 
::  Date Reviewed 12/13/2017 :: 

_________________________________________________________________________________________________________________

The current directory will be set to:

C:\Users\name\Desktop\Cabalidays

-----------------------------------------------------------------------------------------------------------------
Run the routine with:

C:\Users\name\Desktop\Cabalidays\run.bat

*This is a standalone .bat file. It should run the whole routine, as long as the file & folder structure is 
kept the same. Once it is clicked a CMD window will pop-up. Ignore warning that says:

- The system cannot find the patch specified.

The system is now running. It will take around 1 minute to process all information, successful messages will
be output to the console each time a file is created successfully. The following message will appear:

- Press any key to continue . . .

Once a key is pressed, the console prompt window will disappear. The output files have been created.

_________________________________________________________________________________________________________________

Input files to be placed in:

C:\Users\name\Desktop\Cabalidays\cabalidays dm

----------------------------------------------------------------------------------------------------------------
The inputs are:

- On the \cabalidays dm\email folder:
	- br.txt, eu.txt, na.txt (email, username, link, link)

- On the \cabalidays dm\usernum_list folder:
	- username_list.xlsx (3 Sheets with the following fields:	
					NA: NA Usernum(PB)	email	id
					NA: Global Usernum	BR Usernum(PB)	id	usernum	email
					BR: Global Usernum	BR Usernum(PB)	id	usernum	email
				)


- On the \cabalidays dm folder:
	- domainsRemove.txt (Domains to remove from main files)
	- toRemove.txt	(emails to remove from main file)
----------------------------------------------------------------------------------------------------------------
The outputs are:

- On the \cabalidays dm\output folder:

	- DMBR.txt, DMEU.txt, DMNA.txt (email, username, link, link)

	- GiftBR.txt, GiftEU.txt, GiftNA.txt (PB UserNum)
_________________________________________________________________________________________________________________

NOTES: The domainsRemove.txt file has a certain structure to be kept. It is:
		
		service1:
		domain1
		domain2
		domain3
		   .
		   .
		   .
		domain#

		service2:
		domain1
		domain2
		domain3
		   .
		   .
		   .
		domain#

		service3:
		domain1
		domain2
		domain3
		   .
		   .
		   .
		domain#

This structure must remain the same. If new domains are to be added, those must be introduced at the bottom 
of the respective service.

----------------------------------------------------------------------------------------------------------------

Notes: The xlsx file that comes as default must have its name changed to: username_list.xlsx






	
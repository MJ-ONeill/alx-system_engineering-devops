# 0x19 postmortem

## Project  Description
	In this project I am going to write a incident report (More commonly known as a postmortem'
	The incident I wrote about was a Wordpress page that was returning a 500 status code.


## Description
	A postmortem (or post-mortem) is a process intended to help you learn from past incidents. It typically involves an analysis or discussion soon after an event has taken place.
	
	Postmortems typically involve blame-free analysis and discussion soon after an incident or event has taken place. An artifact is produced that includes a detailed description of exactly what went wrong in order to cause the incident, along with a list of steps to take in order to prevent a similar incident from occurring again in the future. An analysis of how your incident response process itself worked during the incident should also be included in the discussion. The value of postmortems comes from helping institutionalize a culture of continuous improvement. This way, teams are better prepared when another incident inevitably occurs with mission- or business-critical systems.

	As your systems scale and become more complex, failure is inevitable, assessment and remediation is more involved and time-consuming, and it becomes increasingly painful to repeat recurring mistakes. Not having data when you need it is expensive.

	Streamlining the postmortem process is key to helping your team get the most from their postmortem time investment: spending less time conducting the postmortem, while extracting more effective learnings, is a faster path to increased operational maturity. In fact, the true value of postmortems comes from helping institutionalize a positive culture around frequent and iterative improvement.
				-----------------------------------------------------------
  #0x19. Postmortem

#Issue Summary:
---------------
	Start time: 10/01/19 9:00 AM (GMT+02:00), 
	End time: 10/01/19 10:00 AM (GMT+02:00).
	The wordpress page was returning a 500 status code, so the page was down for 100% of the users.
	Root cause: typo in a wordpress settings document.

#Timeline:
-----------
	10/01/19 9:05 AM (GMT+02:00) - The issue was detected by several users, who contacted the customer service department.
	10/01/19 9:10 AM (GMT+02:00) - The issue was escalated to the System Engineering team, and the SRE.
	10/01/19 9:15 AM (GMT+02:00) - They looked at the running processes on the server using ‘ps auxf’ to see if any unwanted child process was running in the 	background, and keeping the server from responding.
	10/01/19 9:20 AM (GMT+02:00) - After seeing the processes looked fine, the team used ‘strace’ on some process ids including the ones of apache2 (the web 	server hosting the wordpress page).
	10/01/19 9:30 AM (GMT+02:00) - strace on one of the apache2 processes was showing an infinite loop of system calls, so they looked at the second apache2 	process, that was calling the system call accept4() and hanging.
	10/01/19 9:35 AM (GMT+02:00) - When using curl on the page’s IP while running strace on that second apache2 process, the team realised strace was 		displaying a lot of errors. One of them said that the file index.html didn’t exist, but it was a misleading clue because adding that file in the wordpress 	folders didn’t seem to make it work.
	10/01/19 9:40 AM (GMT+02:00) - After reading carefully all the errors returned by strace, the team saw that one of them mentioned that a file didn’t exist: 	the file that apache2 was trying to access seemed to be terminating in ‘.php’, which is not a common extension for a file.
	10/01/19 9:45 AM (GMT+02:00) - When looking at the wordpress settings file, /var/www/html/wp-settings.php, line 137 was trying to require that faulty file. 	From then, the team just removed the extra ‘p’ at the end of the extension.
	10/01/19 9:50 AM (GMT+02:00) - The team only had to restart apache2 using ‘service apache2 restart’. The page was back up like normal.

#Root cause and resolution:
---------------------------
	One typo in the wordpress settings file was found, causing apache2 to not work properly.
	The issue was saved by removing that typo and restarting apache2.

#Corrective and preventative measures:
-------------------------------------
	Setting files should not have write permissions for anyone other than the SRE, in order to avoid injection of small typos like the one that was experienced 	in this incident.

#TODO
-----
	Change permissions on /var/www/html/wp-settings.php to read-only for the team.
	Read carefully all setting files to look for other typos of that type.




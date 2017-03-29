C:\Python27\python table-notification.py windows 

IF %errorlevel%==1 (
	start mailto:dan.brennan@softchoice.com?subject=MSRP%%20Table%%20Updated^&body=There%%20is%%20a%%20new%%20MSRP%%20table%%20for%%20windows.
) 

C:\Python27\python table-notification.py linux

IF %errorlevel%==1 (
	start mailto:dan.brennan@softchoice.com?subject=MSRP%%20Table%%20Updated^&body=There%%20is%%20a%%20new%%20table%%20for%%20linux.
) 
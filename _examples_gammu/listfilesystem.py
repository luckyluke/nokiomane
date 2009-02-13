#!/usr/bin/env	python
#
# Example for usage of GetNextFileFolder, which is oriented at
#
# gammu --getfilesystem
# 
# Without argument you get a hierarchical list, provide flat as
# argument and get somethink like (not exactly!)
#
# gammu --getfilesystem -flatall
#
# Matthias Blaesing <matthias.blaesing@rwth-aachen.de>

import gammu
import locale
import sys

# Init gammu module
sm = gammu.StateMachine();
sm.ReadConfig()
sm.Init()

# Get wished listing from commandline (if provided - else asume level)
# On commandline level or flat can be provided as parameters
mode = "level"

if len(sys.argv) > 2:
	print 'Only one parameter is allowed here: flat or level'
	sys.exit(1)
elif len(sys.argv) == 2:
	if(sys.argv[1] == "flat" or sys.argv[1] == "level"):
		mode = sys.argv[1]
	else:
		print 'Only one parameter is allowed here: flat or level'
		sys.exit(1)

# Set locale to default locale (here relevant for printing of date)
locale.setlocale(locale.LC_ALL, '')

# Wrapper around GetNextFileFolder, catching gammu.ERR_EMPTY
# for me, which should be after the last entry and returning "None"
#
# GetNextFileFolder gives us a dict with:
# 'Name' => Symbolic Name of the file (String)
# 'ID_FullName' => unique ID of the file (String)
# 'Used' => space used in bytes (integer)
# 'Modified' => Date of last change (datetime)
# 'Type' => Filetype as reported by phone (String)
# 'Folder' => Entry is a Folder (Bool)
# 'Level' => On which level of FS (Integer)
# 'Buffer' => ?? (String)
# File Attributes (Bool): 
# 'Protected'
# 'ReadOnly'
# 'Hidden'
# 'System'
def NextFile (start = 0):
	file = None;
	try:
		file = sm.GetNextFileFolder(start);
	except gammu.ERR_EMPTY:
		pass
	return file

# Format File Attributes as String as a shorted Version
def FileToAttributeString(file, filled = 1):
	protected = readonly = hidden = system = ""
	if filled:
		protected = readonly = hidden = system = u" "
	if file["Protected"]:
		protected = u"P"
	if file["ReadOnly"]:
		readonly = u"R"
	if file["Hidden"]:
		hidden = u"H"
	if file["System"]:
		system = u"S"
	return protected + readonly + hidden + system

# Make sure we reset the pointer of the current entry to the first
file = NextFile(1);

# Iterate over Files and print the Info
while(file):
	if mode=="flat" :
		# Output:
		# <ID>;<NAME>;<TYPE>;<MODDATE>;<SIZE>;<ATTRIBUTES>
		# We have to catch the situations, where no Modification Time is provided
		try:
			time = file["Modified"].strftime("%x %X") + ";"
		except AttributeError:
			time = ";"
		
		print file["ID_FullName"] + ";" \
			+ file["Name"] + ";" \
			+ file["Type"] + ";" \
			+ time \
			+ str(file["Used"]) + ";" \
			+ FileToAttributeString(file, 0)
	elif mode=="level":
		attrib = FileToAttributeString(file,1)
		level = file["Level"]
		spacer = ""
		
		for i in range(1, (level-1)):
			spacer = spacer + " |   "
		if(level > 1):
			spacer = spacer + " |-- "

		title = '"' + file["Name"] + '"'
		if file["Folder"]:
			title = "Folder " + title
		print attrib + spacer + title;
	file = NextFile()

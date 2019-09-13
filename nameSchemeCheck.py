import os, re
from tqdm import tqdm
__name__ = "__main__"

def scanFolders(inputDirectory):
	foldersFound=[]
	for folder in os.listdir(inputDirectory):
		if os.path.isdir(os.path.join(inputDirectory,folder)):
			foldersFound.append(folder)

	# checks if you're pointing it to a folder with subfolders in:
	fullPaths=[]
	print("Checking for subfolders in top level directory:\n",flush=True)
	for folder in tqdm(foldersFound):
		fullpath=inputDirectory+'\\'+folder
		if os.path.isdir(fullpath):
			fullPaths.append(fullpath)

	if fullPaths:
		# compile regexs outside of loops
		folderPatternOne=re.compile("(^\d{7}_\d{4}$)",re.MULTILINE)
		folderPatternTwo=re.compile("(^\d{7}_\d{4}_[a-zA-Z]{3}_[a-zA-Z]{3}$)",re.MULTILINE)

		print("\nChecking folder name compliance:\n",flush=True)
		with open ('nonCompliantFolders.txt','a+') as badFolders:
			for folder in tqdm(foldersFound):
				matchOne=folderPatternOne.match(folder)
				matchTwo=folderPatternTwo.match(folder)
				if matchOne is None:
					if matchTwo is None:
						badFolders.write(folder+'\n')

		return fullPaths
	else:
		print("No subfolders found within this directory!",flush=True)
		return 0
	
def scanFiles(pedantic,fullPaths):
		print("\nChecking filename compliance:\n",flush=True)
		with open('nonCompliantFiles.txt','a+') as badFileNames:
			for directoryPath in tqdm(fullPaths):
				filenames=os.listdir(directoryPath)
				filePattern=(os.path.basename(directoryPath))+r'(_\d{4}.tif)'
				if pedantic is True:
					regexPattern=re.compile(filePattern)
				else:
					regexPattern=re.compile(filePattern,re.IGNORECASE)
				for tifFile in filenames:
					match=regexPattern.match(tifFile)
					if match is None:
						outstring=directoryPath+'\\'+tifFile
						badFileNames.write(outstring+'\n')

def setup():
	pedantic=False
	mode=input("Type Y to run in case-sensitive filename checking mode, or enter to continue in case-insensitive mode:\n")
	if mode is "Y":
		pedantic=True
	else:
		pedantic=False
	if pedantic is True:
		print("Running in case-sensitive mode\n")
	else:
		print("Running in case-insensitive mode\n")

	
	inputDirectory=r"\\P12B-NAS1\scandata2\HMD\RAW SCANS\Dave\FMP\Still to deliver to FMP"
	inDir=input("Scan current folder? Y/N:\n")
	if (inDir=="Y" or inDir=="y" or inDir=="Yes" or inDir=="yes"):
		inputDirectoryUser=os.getcwd()
	elif (inDir=="N" or inDir=="n" or inDir=="No" or inDir=="no"):
		inputDirectoryUser=input("Enter full path of folder to scan:\n")
		if inputDirectoryUser=="":
			print("No path entered, using default filepath: {}\n".format(inputDirectory),flush=True)
			inputDirectoryUser=inputDirectory
	else:
		inputDirectoryUser=inputDirectory
		print("Input not recognised, using default filepath: {}\n".format(inputDirectory))	
	print("Checking if directory exists...\n",flush=True)	
	
	
	
	if os.path.isdir(inputDirectoryUser):
		print("Input directory: {}\ exists!\n".format(inputDirectoryUser))
		inputDirectory = inputDirectoryUser
	else:
		print("File path not a valid directory, using default path {}\n".format(inputDirectory))

	return pedantic,inputDirectory

def main():

	isPedantic,inputDir=setup()
	filePaths=scanFolders(inputDir)
	scanFiles(isPedantic,filePaths)


	input("Complete! Press enter to exit")


if __name__=="__main__":
	main()

import subprocess

def return_list(directory):
	sp = subprocess.Popen(['ls', '-l', directory],shell=True,stdout=subprocess.PIPE)
	stdout,stderr= sp.communicate()


	directory_list=[x.split(' ')[-1] for x in stdout.decode().split('\n')[1:-1]]
	# num=directory_list.index('..\r')
	# directory_list=directory_list[num+1:-3]
	# directory_list=[i.replace('\r','')for i in directory_list]
	
	return directory_list
	
	

directory=input("Enter the directory :")
directory_list=return_list(directory)

print(directory_list)



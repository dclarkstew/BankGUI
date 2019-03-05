from tkinter import *
from tkinter import filedialog
import os

# Cat 1 - Rent
# Cat 2 - Utilities
# Cat 3 - Groceries
# Cat 4 - Eating Out
# Cat 5 - Alcohol
# Cat 6 - Car/Gas/Transportation
# Cat 7 - Projects
# Cat 8 - Clothes/Personal
# Cat 9 - Gifts
# Cat 10 - Home Goods
# Cat 11 - Misc
# Cat 12 - Income
catNames = ['Rent\t\t', 'Utilities\t','Groceries\t','Eating Out\t','Alcohol\t\t','Car/Gas\t\t','Projects\t','Clothes/Personal','Gifts\t\t','Home Goods\t','Misc\t\t','Income']
dataStarts = 2
numCats = 13
numCols = 6
cats = []
for k in range(numCats):
	cats.append(0)

class GUI:
	def __init__(self,master):
		self.master = master
		master.title('Transaction Sorter')

		self.label_index = 0
		
		#Date
		self.date = StringVar()
		self.date.set('Date: \t\t')
		Label(master, textvariable= self.date).grid(row=0, column=0, columnspan=2, sticky=W)
		#Debit or Credit
		self.DorC = StringVar()
		self.DorC.set('Debit/Credit: \t')
		Label(master, textvariable= self.DorC).grid(row=1, columnspan=3, sticky=W)
		#Amount
		self.amount = StringVar()
		self.amount.set('Amount: \t')
		Label(master, textvariable= self.amount).grid(row=2, columnspan=3, sticky=W)
		#Description
		self.info = StringVar()
		self.info.set('Date: \t\t')
		Label(master, textvariable= self.info).grid(row=3, columnspan=3, sticky=W)
		#Select File
		Button(master, text='Select File', command=self.browse_button, background='gray70').grid(row=0, column=1, columnspan=2, sticky=W+E)
		self.name = StringVar()
		self.name.set('')
		Label(master, textvariable=self.name, background='gray80').grid(row=1, column=1, columnspan=2)

		# Number of Transactions Left
		self.remain = StringVar()
		self.remain.set('-'*8+'Number of Transactions Left: '+'-'*84)
		Label(master, textvariable = self.remain).grid(row=4, columnspan=3)

		# Category 1 Value Set
		self.cat1Val = StringVar()
		self.cat1Val.set('Rent: $'+str(cats[0]))
		self.label_cat1Val = Label(master, textvariable = self.cat1Val, background='gray70').grid(row=5, column=0, sticky=W+E)
		# Category 2 Value Set
		self.cat2Val = StringVar()
		self.cat2Val.set('Utilities: $'+str(cats[1]))
		self.label_cat2Val = Label(master, textvariable = self.cat2Val, background='gray65').grid(row=5, column=1, sticky=W+E)
		# Category 3 Value Set
		self.cat3Val = StringVar()
		self.cat3Val.set('Groceries: $'+str(cats[2]))
		self.label_cat3Val = Label(master, textvariable = self.cat3Val, background='gray70').grid(row=5, column=2, sticky=W+E)
		# Category 4 Value Set
		self.cat4Val = StringVar()
		self.cat4Val.set('Eating Out: $'+str(cats[3]))
		self.label_ca41Val = Label(master, textvariable = self.cat4Val, background='gray80').grid(row=6, column=0, sticky=W+E)
		# Category 5 Value Set
		self.cat5Val = StringVar()
		self.cat5Val.set('Alcohol: $'+str(cats[4]))
		self.label_cat5Val = Label(master, textvariable = self.cat5Val, background='gray75').grid(row=6, column=1, sticky=W+E)
		# Category 6 Value Set
		self.cat6Val = StringVar()
		self.cat6Val.set('Car/Gas: $'+str(cats[5]))
		self.label_cat6Val = Label(master, textvariable = self.cat6Val, background='gray80').grid(row=6, column=2, sticky=W+E)
		# Category 7 Value Set
		self.cat7Val = StringVar()
		self.cat7Val.set('Projects: $'+str(cats[6]))
		self.label_cat7Val = Label(master, textvariable = self.cat7Val, background='gray70').grid(row=7, column=0, sticky=W+E)
		# Category 8 Value Set
		self.cat8Val = StringVar()
		self.cat8Val.set('Clothes/Personal: $'+str(cats[7]))
		self.label_cat8Val = Label(master, textvariable = self.cat8Val, background='gray65').grid(row=7, column=1, sticky=W+E)
		# Category 9 Value Set
		self.cat9Val = StringVar()
		self.cat9Val.set('Gifts: $'+str(cats[8]))
		self.label_cat9Val = Label(master, textvariable = self.cat9Val, background='gray70').grid(row=7, column=2, sticky=W+E)
		# Category 10 Value Set
		self.cat10Val = StringVar()
		self.cat10Val.set('Home Goods: $'+str(cats[9]))
		self.label_cat10Val = Label(master, textvariable = self.cat10Val, background='gray80').grid(row=8, column=0, sticky=W+E)
		# Category 11 Value Set
		self.cat11Val = StringVar()
		self.cat11Val.set('Misc: $'+str(cats[10]))
		self.label_cat11Val = Label(master, textvariable = self.cat11Val, background='gray75').grid(row=8, column=1, sticky=W+E)
		# Category 12 Value Set
		self.cat12Val = StringVar()
		self.cat12Val.set('Income: $'+str(cats[11]))
		self.label_cat12Val = Label(master, textvariable = self.cat12Val, background='gray80').grid(row=8, column=2, sticky=W+E)
		# Category 13 Value Set
		self.cat13Val = StringVar()
		self.cat13Val.set('Savings: $'+str(cats[12]))
		self.label_cat13Val = Label(master, textvariable = self.cat13Val, background='gray70').grid(row=9, column=0, sticky=W+E)

		# Buttons
		self.cat1 = Button(master, text='\nRent\n', command=lambda:self.update(1), background='gray70').grid(row=11, column=0 , sticky=W+E)
		self.cat2 = Button(master, text='\nUtilities\n', command=lambda:self.update(2), background='gray70').grid(row=11, column=1 , sticky=W+E)
		self.cat3 = Button(master, text='\nGroceries\n', command=lambda:self.update(3), background='gray70').grid(row=11, column=2 , sticky=W+E)
		self.cat4 = Button(master, text='\nEating Out\n', command=lambda:self.update(4), background='gray70').grid(row=12, column=0 , sticky=W+E)
		self.cat5 = Button(master, text='\nAlcohol\n', command=lambda:self.update(5), background='gray70').grid(row=12, column=1 , sticky=W+E)
		self.cat6 = Button(master, text='\nCar/Gas\n', command=lambda:self.update(6), background='gray70').grid(row=12, column=2 , sticky=W+E)
		self.cat7 = Button(master, text='\nProjects\n', command=lambda:self.update(7), background='gray70').grid(row=13, column=0 , sticky=W+E)
		self.cat8 = Button(master, text='\nClothes/Personal\n', command=lambda:self.update(8), background='gray70').grid(row=13, column=1 , sticky=W+E)
		self.cat9 = Button(master, text='\nGifts\n', command=lambda:self.update(9), background='gray70').grid(row=13, column=2 , sticky=W+E)
		self.cat10 = Button(master, text='\nHome Goods\n', command=lambda:self.update(10), background='gray70').grid(row=14, column=0 , sticky=W+E)
		self.cat11 = Button(master, text='\nMisc\n', command=lambda:self.update(11), background='gray70').grid(row=14, column=1 , sticky=W+E)
		self.cat12 = Button(master, text='\nIncome\n', command=lambda:self.update(12), background='gray70').grid(row=14, column=2 , sticky=W+E)
		self.cat13 = Button(master, text='\nSavings\n', command=lambda:self.update(13), background='gray70').grid(row=15, column=0 , sticky=W+E)
		self.cat14 = Button(master, text='\nDelete\n', command=lambda:self.update(14), background='gray70').grid(row=15, column=1 , sticky=W+E)

		Label(master,text='-'*125).grid(row=16, columnspan=3)
		Button(master, text='Print Output File', command=lambda:self.printCSV('yes'), background='green3').grid(row=17, column=0, columnspan=3, sticky=W+E)

	def browse_button(self):
		global numPoints
		global table
		global fileName
		global inputFile
		self.label_index = 0

		# Import/Open File
		filepath=filedialog.askopenfilename()
		path, fileName = os.path.split(filepath)
		inputFile = open(fileName,'r')

		# Read File
		inputLines=[0]
		i=0
		for line in inputFile.readlines():
			inputLines[i]=line.split(',')
			inputLines.append(0)
			i+=1
		numPoints = len(inputLines)-dataStarts-1
		catVals = ([0]*numPoints)

		#ReOrganize Data
		table=[]
		for i in range(numCols):
			table.append([0]*(numPoints+1))

		for lines in range(numPoints):
			table[0][lines] = inputLines[lines+1][0]
			table[1][lines] = inputLines[lines+1][1]
			table[2][lines] = inputLines[lines+1][2]
			table[3][lines] = inputLines[lines+1][3]
			table[4][lines] = float(inputLines[lines+1][4].strip('[()$]\n'))
		print(str(numPoints)+ ' Data Points Loaded.\n')
		print('*'*19+'\n'+'Begin Entering Type\n')

		self.date.set('Date: \t\t'+str(table[0][self.label_index]))
		self.DorC.set('Debit/Credit: \t'+str(table[1][self.label_index]))
		self.amount.set('Amount: \t'+str(table[4][self.label_index]))
		self.info.set('Description: \t'+str(table[3][self.label_index]))
		self.remain.set('-'*8+'Number of Transactions Left: '+str(numPoints-self.label_index)+'-'*84)
		self.name.set(fileName)

	def update(self, method):
		if self.label_index < numPoints:
			val = float(table[4][self.label_index])
			for j in range(numCats):
				if method == j+1:
					cats[j] += val
			self.label_index += 1
			self.date.set('Date: \t\t'+str(table[0][self.label_index]))
			self.DorC.set('Debit/Credit: \t'+str(table[1][self.label_index]))
			self.amount.set('Amount: \t'+str(table[4][self.label_index]))
			self.info.set('Description: \t'+str(table[3][self.label_index]))
			self.remain.set('-'*8+'Number of Transactions Left: '+str(numPoints-self.label_index)+'-'*84)
		else:
			self.date.set('Date: \t\t Transactions Complete')
			self.DorC.set('Debit/Credit: \t X')
			self.amount.set('Amount: \t X')
			self.info.set('Desctription: \t X')

		self.cat1Val.set('Rent: $'+str(cats[0]))
		self.cat2Val.set('Utilites: $'+str(cats[1]))
		self.cat3Val.set('Groceries: $'+str(cats[2]))
		self.cat4Val.set('Eating Out: $'+str(cats[3]))
		self.cat5Val.set('Alcohol: $'+str(cats[4]))
		self.cat6Val.set('Car/Gas: $'+str(cats[5]))
		self.cat7Val.set('Projects: $'+str(cats[6]))
		self.cat8Val.set('Clothes/Personal: $'+str(cats[7]))
		self.cat9Val.set('Gifts: $'+str(cats[8]))
		self.cat10Val.set('Home Goods: $'+str(cats[9]))
		self.cat11Val.set('Misc: $'+str(cats[10]))
		self.cat12Val.set('Income: $'+str(cats[11]))
		self.cat13Val.set('Savings: $'+str(cats[12]))

	def printCSV(self, request):
		if request == 'yes':
			name = os.path.splitext(fileName)[0]
			outputFile = open(name+'.txt','w+')
			outputFile.write(fileName+'\n\n')
			for lines in range(numPoints):
				date = table[0][lines]
				amount = str(table[4][lines])
				desc = str(table[3][lines])
				cat = str(table[5][lines])
				outputFile.write(date+'\t'+amount+'\t'+cat+'\t'+desc+'\n')
			outputFile.write('\n')
			outputFile.write('Income: $'+str(int(cats[11]))+'\n')
			for lines in range(numCats-2):
				outputFile.write(catNames[lines]+'\t$'+str(int(cats[lines]))+'\t'+str(int(cats[lines]*100/(sum(cats)-cats[11]-cats[12])))+'%\n')
			outputFile.write('\n Savings: $' + str(cats[12]))
			outputFile.write('\n Total Spending: $'+str(int(sum(cats)-cats[12]-cats[11])))
			if cats[11] > 0:
                                outputFile.write('\n Excess Savings: $'+str(int(cats[11] - (sum(cats)-cats[12]-cats[11])))+'\t'+str(int(cats[11]-(sum(cats)-cats[12]-cats[11]))*100/cats[11])+'%')
			outputFile.close()
			print('\nWrite Successful\n')
		inputFile.close()
root = Tk()
my_gui = GUI(root)
root.mainloop()
			





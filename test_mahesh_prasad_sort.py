import unittest
from mahesh_prasad_sort import MP_Sort

class Test_MP_Sort(unittest.TestCase):
	
	mpSort 		= 0	
	hedearseq 	= []
	csvFile     = ''
	
	def setUp(self):
		# read a CSV file and do the sort functionality		
		self.hedearseq = ['Year','Month','Company A','Company B','Company C','Company N']
		self.csvFile = 'prices.csv'
		
	def test_readCSV(self):
		self.mpSort = MP_Sort()
		# Read share prices CSV file
		self.mpSort.readCSV(self.csvFile,',')
		# check if file read object availabe
		self.assertTrue(self.mpSort.dt)
		
	def test_readHD(self):
		self.mpSort = MP_Sort()
		# Read share prices CSV file
		self.mpSort.readCSV(self.csvFile,',')		
		self.headerRow = self.mpSort.readHD()
		for header_element in self.headerRow:
			self.assertIn(header_element,self.hedearseq)
			
	def test_sortData(self):
		self.mpSort = MP_Sort()
		self.mpSort.readCSV(self.csvFile,',')		
		self.headerRow = self.mpSort.readHD()		
		pdt = self.mpSort.dt;			
		# List for each Company year and month in which the share price was highest
		# As CSV have 2 columns year and month so next column start with price data
		# So 0 and 1 means years and months and from 2 means prices data
		'''
		for n in range(2, self.mpSort.dl):
			print "Highest price of " + self.headerRow[n]
			pdt = self.mpSort.sortData(pdt,n)	
			if pdt!=[]:
				print pdt[0][0] + ' ' + pdt[0][1] + ' - ' + pdt[0][n]
		'''		
		#Highest price of Company A		2013 Sep - 50
		#Highest price of Company B		1990 Jan - 15
		#Highest price of Company C		1990 Jan - 20
		#Highest price of Company N		2013 Sep - 500				
		self.assertTrue("ok")
		# Highest price of Company A
		# 2013 Sep - 50		
		pdt = self.mpSort.sortData(pdt,2)
		self.assertEqual(pdt[0][0], '2013', msg="Highest price of Company A		2013 Sep - 50")
		self.assertEqual(pdt[0][1], 'Sep', msg="Highest price of Company A		2013 Sep - 50")
		self.assertEqual(pdt[0][2], '50', msg="Highest price of Company A		2013 Sep - 50")
		# Highest price of Company B
		# 1990 Jan - 15		
		pdt = self.mpSort.sortData(pdt,3)
		self.assertEqual(pdt[0][0], '1990', msg="Highest price of Company B		1990 Jan - 15")		
		self.assertEqual(pdt[0][1], 'Jan', msg="Highest price of Company B		1990 Jan - 15")		
		self.assertEqual(pdt[0][3], '15', msg="Highest price of Company B		1990 Jan - 15")	
		# Highest price of Company C		
		# 1990 Jan - 20
		pdt = self.mpSort.sortData(pdt,4)
		self.assertEqual(pdt[0][0], '1990', msg="Highest price of Company C		1990 Jan - 20")
		self.assertEqual(pdt[0][1], 'Jan', msg="Highest price of Company C		1990 Jan - 20")
		self.assertEqual(pdt[0][4], '20', msg="Highest price of Company C		1990 Jan - 20")
		# Highest price of Company N		
		# 2013 Sep - 500
		pdt = self.mpSort.sortData(pdt,5)
		self.assertEqual(pdt[0][0], '2013', msg="Highest price of Company N		2013 Sep - 500")
		self.assertEqual(pdt[0][1], 'Sep', msg="Highest price of Company N		2013 Sep - 500")
		self.assertEqual(pdt[0][5], '500', msg="Highest price of Company N		2013 Sep - 500")
		
# end of Test_MP_Sort class
'''
if __name__ == '__main__':
    unittest.main()
#'''
suite = unittest.TestLoader().loadTestsFromTestCase(Test_MP_Sort)
unittest.TextTestRunner(verbosity=2).run(suite)
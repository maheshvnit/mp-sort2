import sys,csv
import operator

class MP_Sort:

	dl 		= 0
	
	dt 		= []
	
	def __init__(self):
		self.dt = []	

	def readCSV(self,file,de_limiter):
		try:
			self.dt = csv.reader(open(file),delimiter=de_limiter)
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
			raise
		except ValueError:
			print "Could not convert data to an integer."
			raise
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise	
			
	def readHD(self):
		headerRow = self.dt.next()
		self.dl = len(headerRow)
		return headerRow
		
	def sortData(self,dt,by_index):
		sdt=[]
		try:
			sdt = sorted(dt, key=operator.itemgetter(by_index), reverse=True)	
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
			raise
		except ValueError:
			print "Could not convert data to an integer."
			raise
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise	
		return sdt
		
# end of MP_Sort class
		

import AppClass_sm

class AppClass:

	k = 0
	_func = ""

	def __init__(self):
		self._fsm = AppClass_sm.AppClass_sm(self)
		self._is_acceptable = False

		# Uncomment to see debug output.
		#self._fsm.setDebugFlag(True)

	def CheckString(self, string):
		self._fsm.enterStartState()
		t = 0
		for c in string:
			if c.isdigit():
				self._fsm.D()
				if t == 1:
					self._func = self._func+c
			elif c.isalpha():
				self._fsm.L()
				if t == 1:
					self._func = self._func+c
			elif c == ' ':
				self._fsm.Sp()
				if self._func != "":
					t = 0
			elif c == '(':
				self._fsm.LBr()
				t = 0
			elif c == ')':
				self._fsm.RBr()
			elif c == '=':
				self._fsm.Eq()
				t = 1
			elif c == ',':
				self._fsm.Com()
			elif c == ';':
				self._fsm.Sem()
			elif c == '\n':
				self._fsm.EOS()
			else:
				self._fsm.Unknown()
		return self._is_acceptable

	def setk(self):
		self.k = 0

	def addk(self):
		self.k = self.k + 1

	def getk(self):
		return self.k

	def Acceptable(self):
		self._is_acceptable = True

	def Unacceptable(self):
		self._is_acceptable = False
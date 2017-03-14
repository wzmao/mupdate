# -*- coding: utf-8 -*-


class Logger():

	def __init__(self, filename, filemode='w', *arg, **kwargs):
		from multiprocessing import Lock
		from datetime import datetime
		self.filename = filename
		self.datetime = datetime
		self.on = True
		self.screenon = False
		self.lock = Lock()
		self.lock.acquire(True)
		f = open(self.filename, filemode)
		f.close()
		self.lock.release()
		self.write('Start logging.')

	def write(self, content):
		self.lock.acquire(True)
		if self.on:
			f = open(self.filename, 'a')
			if isinstance(content, str):
				f.write(self.datetime.now().strftime(
						'%Y-%m-%d %H:%M:%S  ') + content.strip() + '\n')
				if self.screenon:
					print(self.datetime.now().strftime(
						'%Y-%m-%d %H:%M:%S  ') + content.strip()).decode('utf-8')
			else:
				for i in content:
					f.write(self.datetime.now().strftime(
							'%Y-%m-%d %H:%M:%S  ') + i.strip() + '\n')
					if self.screenon:
						print(self.datetime.now().strftime(
							'%Y-%m-%d %H:%M:%S  ') + i.strip()).decode('utf-8')
			f.close()
		self.lock.release()


class _fakeLogger():

	def __init__(self, *arg, **kwargs):
		pass

	def write(self, *arg, **kwargs):
		pass

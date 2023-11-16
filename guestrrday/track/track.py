import re
import os.path
import unidecode
from guestrrday import utils

class track:
	def __init__(self, title):
		self.filename_path = None
		if os.path.exists(title) and os.path.isfile(title) and utils.has_music_ext(title):
			base = os.path.basename(title)
			self.filename_path = title
			title = base[ : base.rfind('.')]
		self.title = title
		self.track = None
		self.artist = None
		self.year = None
		self.label = None
		self.qualifier = None
		self.song_title = None
		self.id = id
		self.new_title = None
		self.extract_artist_title()
		
	
	# MyFolder\MyAlbum\02. Prince - Musicology (Timelife Mix).mp3
	def get_filename_path(self):
		return self.filename_path

	# 002. Prince - Musicology (Timelife Mix)
	def get_full_title(self):
		tit = self.title
		if self.track is not None:
			tr = str(self.track).zfill(3)
			tit = f'{tr}. {tit}'
		return tit
		
	# Prince - Musicology (Timelife Mix)
	def get_title(self):
		return self.title
	
	# Prince
	def get_artist(self):
		return self.artist
	
	# Musicology
	def get_song_title(self):
		return self.song_title

	# 2
	def get_track(self):
		return self.track
	
	# Timelife Mix
	def get_qualifier(self):
		return self.qualifier	
	
	def get_year(self):
		return self.year
	
	def get_label(self):
		return self.label
		
	def get_id(self):
		return self.id
	
	def is_track(self):
		return self.artist != None and self.song_title != None
	
	def get_new_name(self):
		return self.new_title
		
	def set_new_name(self, new):
		self.new_title = new
		if self.filename_path is not None:
			path = os.path.dirname(self.filename_path)
			base = os.path.basename(self.filename_path)
			ext = base[ base.rfind('.') + 1 : ]
			self.new_title = os.path.join(path, f'{self.new_title}.{ext}')			
	
	def __str__(self):
		if self.filename_path != None:
			return self.filename_path
		else:
			return self.get_full_title()
	
		
	def extract_artist_title(self):	
		self.title = cleanup_title(self.title)
		pat_str = r'^\s*(\d*)\s*[\W_]?\s*(.+)(?:(\s[\-\_~\：]|[\-\_~\：]\s|\s[\-\_~\：]\s))(.*)$'
		pat = re.compile(pat_str)
		match = re.findall(pat, self.title)
		if match != []:
			match = match[0]
			if match[0] != '':
				self.track = int(match[0].strip())
			self.artist = match[1].strip()
			if len(match) == 5 and match[4] != '':
				self.year = match[4]
			sng_tit = match[3].strip()
			pat_2 = re.compile(r'^\s*(.+)\s*(?:\((.[\w\s\W]+)\))\s*$')
			match_2 = re.findall(pat_2, sng_tit)
			if match_2 != []:
				match_2 = match_2[0]
				sng_tit = match_2[0].strip()
				self.qualifier = match_2[1].strip()
			self.song_title = sng_tit
			self.title = self.artist + ' - ' + self.song_title
			if self.qualifier != None:
				self.title += ' (' + self.qualifier + ')'
			#if self.year != None:
			#	self.title += ' (' + self.year + ')'
		else:
			pat2= r'^\s*(\d*)\s*[\W_]?\s*(.+)$'
			pat2 = re.compile(pat2)
			match2 = re.findall(pat2, self.title)
			if match2 != [] and match2[0][0].strip() != '':
				self.track = int(match2[0][0].strip())
				self.title = match2[0][1].strip()
				#print("Couldn't match: " + self.title)
			self.artist = self.title
			self.song_title = self.title
		

def cleanup_title(title):
	#title = title.lower()
	title = title.replace('[','(')
	title = title.replace(']',')')
	title = title.replace('{','(')
	title = title.replace('}',')')
	title = title.replace('–','-')
	title = title.replace("’","'")
	title = title.replace("´","'")
	title = title.replace('＂','"')
	title = title.replace(' and ', ' & ')
	title = title.replace(' feat.', ' & ')
	title = title.replace(' feat ', ' & ')
	title = title.replace(' ft. ', ' & ')		
	title = title.replace(' ft ', ' & ')
	title = title.replace(' featuring ', ' & ')
	title = unidecode.unidecode(title)
	title = title.replace('*', '')
	title = title.replace("''", '"')
	if title.rfind('"') > title.find('"') and title.find('"') > -1 and title.find(" - ") == -1:
		title = re.sub(' ?\" ?(.+) ?\"', ' - \\1', title)
	if title.find(' - ') == -1:
		if title.find('   ') > -1:
			title = title.replace('   ',' - ', 1)
		elif title.find('  ') > -1:
			title = title.replace('  ',' - ', 1)
		elif title.find('-') > -1:
			title = title.replace('-',' - ', 1)
	title = title.replace('"', '')
	return title.strip()
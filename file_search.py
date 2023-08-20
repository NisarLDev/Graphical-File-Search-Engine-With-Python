import os
import pickle

class SearchEngine:
  def __init__(self):
      self.file_index = []
      self.results = []
      self.matches = 0
      self.records = 0

  def create_new_index(self, root_path):
      ''' create a new index and save to file '''
      self.file.index = [(root, files) for root, dirs, files in os.walk(root_path) if files]
      # save to file
      with open('file_index.pkl','wb')
    
  def load_existing_index(self):
      ''' load existing index '''

  def search(self, term, search_type = 'contains'):
      ''' search for term based on search type '''
      pass
  

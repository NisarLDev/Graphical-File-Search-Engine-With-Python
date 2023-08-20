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
      with open('file_index.pkl','wb') as f:
          pickle.dump(self.file_index, f)
        
  def load_existing_index(self):
      ''' load existing index '''
      try:
          with open('file_index.pkl','rb') as f:
              self.file_index = pickle.load(f)
      except:
          self.file_index = []
        
  def search(self, term, search_type = 'contains'):
      ''' search for term based on search type '''


      # reset variables
      self.results.clear()
      self.matches = 0
      self.records = 0
      # perform search
      for path, files in self.file_index
      # save search results

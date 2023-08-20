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
    

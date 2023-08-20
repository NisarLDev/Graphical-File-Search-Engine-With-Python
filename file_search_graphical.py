import os
import pickle

class Gui:
    def __init__(self):
        self.layout = [sg.Text('Search Term'), sg.Input()]
        self.window = sg.Windows('File Search Engine').Layout(self.layout)
      
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
      for path, files in self.file_index:
          for file in files:
              self.records +=1
              if (search_type == 'contains' and term.lower() in file.lower() or 
                  search_type == 'startswith' and file.lower().startswith(term.lower()) or
                  search_type == 'endwith' andfile.lower().endwith(term.lower())):
                  # For Windows systems
                  result = path.replace('\\','/') + '/' + file
                  self.results.append(result)
                  self.matches +=1
              else:
                continue
                
      # save search results
      with open('search_results.txt','w') as f:
          for row in self.results:
              f.write(row + '\n')


def test1():
    s = SearchEngine()
    s.create_new_index('C:/')
    s.search('gecko')

    print()
    print('>> There were {:,d} matces out of {:,d} records searched.'.format(s.matches))
    print('>> This query produced the following atches: \n')
    for match in s.results:
        print(match)



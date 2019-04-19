# a possible solution
def scrape_directory_tree(starting_dir, file_ending):
    assert os.path.isdir(starting_dir) # do not pass a filename
    matching_files = []
    for current_dir, directories, files in os.walk(starting_dir, topdown=True):
       for filename in files:
           if filename.endswith(file_ending):
               matching_files.append(os.path.join(current_dir, filename))
    return matching_files

def list_files_by_size(filepathlist, decreasing=True):
    sorted_files = sorted(filepathlist, key=os.path.getsize, reverse=decreasing)
    return sorted_files

# test it
start = 'first_exercise.md' # fails when given a file instead of dir?
name_ending = '.cat'
print(scrape_directory_tree(start, name_ending))

start = 'exciting_data'
name_ending = '.cat' # find the cat file
print(scrape_directory_tree(start, name_ending))

name_ending = '.doc' # find and rank the docs
print(scrape_directory_tree(start, name_ending))

name_ending = '.dat'
filelist = scrape_directory_tree(start, name_ending)
filelist_by_size = list_files_by_size(filelist)
for filepath in filelist_by_size:
    print(filepath, os.path.getsize(filepath))
# passed the tests.

# how about more general patterns?
import re
pattern = re.compile(".*\.dat$")
def scrape_directory_tree(starting_dir, file_pattern):
    assert os.path.isdir(starting_dir) # do not pass a filename
    matching_files = []
    for current_dir, directories, files in os.walk(starting_dir, topdown=True):
       for filename in files:
           if file_pattern.match(filename):
               matching_files.append(os.path.join(current_dir, filename))
    return matching_files

name_ending = '.dat'
filelist = scrape_directory_tree(start, name_ending)
filelist_by_size = list_files_by_size(filelist)
for filepath in filelist_by_size:
    print(filepath, os.path.getsize(filepath))

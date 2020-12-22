#!/usr/bin/python

import sys
import re

def extract_names(filename):
  """
  Given a file name for baby<year>.html,
  returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  If this seems too daunting, return
  ['2006', (male_name,rank), (female_name,rank), ....]
  The names and ranks are pairs rather than strings and they
  do not have to be sorted. For example the list might begin
  ['2006', ('Jacob','1'), ('Emma','1'), ...]
  
  """
  # +++your code here+++
  names = []
  f = open(filename, 'r')
  text = f.read()
  year_match = re.search(r'(Popularity\sin\s)(\d\d\d\d)', text)
  year = year_match.group(2)
  names.append(year)
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
  rank_name =  {}
  for rank_tuple in tuples:
    (rank, boyname, girlname) = rank_tuple 
    if boyname not in rank_name:
      rank_name[boyname] = rank
    if girlname not in rank_name:
      rank_name[girlname] = rank
  sorted_names = sorted(rank_name.keys())
  for name in sorted_names:
    names.append(name + " " + rank_name[name])
  return names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.

  if len(sys.argv) == 2:
    arg = sys.argv[1]
  else:
    print("usage: ", sys.argv[0], "filename")
    sys.exit(1)

  # +++your code here+++
  # For each filename, get the names, then print the text output
  names = extract_names(arg)
  text = '\n'.join(names) + '\n'
  print (text)

  print('Yes, you are running the script correctly!')

if __name__ == '__main__':
  main()

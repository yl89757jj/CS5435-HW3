from abc import ABCMeta, abstractmethod
import unittest
import functools as ft
import re
from collections import defaultdict
from password_database import load_rockyou_dataset


class WordSnippet:
  __metaclass__ = ABCMeta
  data = ""

  def __init__(self, _data):
    self.data = _data

  @property
  @abstractmethod
  def regexpr(self):
    pass

  @property
  @abstractmethod
  def keyword(self):
    pass

  def key_string(self):
    return "%s%d" % (self.keyword, len(self.data))


class Letters(WordSnippet):
  regexpr = re.compile("[a-zA-Z]+")
  keyword = "L"


class Numbers(WordSnippet):
  regexpr = re.compile("\d+")
  keyword = "N"


class Symbols(WordSnippet):
  regexpr = re.compile("([^\w])+")
  keyword = "S"


class Password:
  """From a password(string) parse to list of categories based on regex matches(letters, numbers or letters)."""
  password = ""
  snip_list = []

  def __init__(self, _password):
    # assert _password != self.password

    self.password = _password
    for snippet_type in [Letters, Numbers, Symbols]:
      match_idxs = [m.span() for m in snippet_type.regexpr.finditer(self.password)]
      self.snip_list = self.snip_list + list(
        map(lambda match_idx: (match_idx[0], snippet_type(self.password[match_idx[0]:match_idx[1]])), match_idxs))

    self.snip_list.sort(key=lambda tup: tup[0])

  def key_strings(self):
    """Return a string that describes the structure of the password. For example:
        - `%^*hello(*&1348` produces "S*3 L*5 S*3 N*4`
        - `chargers21` produces `L*8 N*2`
        - `chamillionaire` produces `L*14`
    """
    return ft.reduce(lambda kstr, sn1: "%s%s" % (kstr, sn1[1].key_string()), self.snip_list, "")[1:]


class TestPasswordSnippet(unittest.TestCase):
  def test_letters_symbols(self):
    self.assertEqual(Password("%^*hello(*&1348").key_strings(), "S3L5S3N4")

  def test_chargers21(self):
    self.assertEqual(Password("chargers21").key_strings(), "L8N2")

  def test_chamillionaire(self):
    self.assertEqual(Password("chamillionaire").key_strings(), "L14")


def categorize(password_strings):
  categories = defaultdict(list)
  for password_string in password_strings:
    p0 = Password(password_string)
    categories[p0.key_strings()].append(password_string)

  return categories


def main():
  """Read 70,000 of the rockyou dataset, parse them, then output a count per parse-description"""
  passwords = []
  i = 0

  with open('rockyou-withcount.txt', encoding='raw_unicode_escape') as passwords_file:
    for password_line in passwords_file:
      passwords.append(password_line[8:].strip())
      i += 1
      if i >= 70000:
        break

  categories = categorize(passwords)

  file = open("passwords_parsed_70k.txt", "w")
  for category_key in categories:
    category = categories[category_key]
    file.write("%d6\t%s\n" % (len(category), category_key))
  file.close()


if __name__ == '__main__':
  main()

from abc import ABCMeta, abstractmethod
import unittest
import functools as ft
import re


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
    return "%s*%d" % (self.keyword, len(self.data))


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
    assert _password != self.password

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
    return ft.reduce(lambda kstr, sn1: "%s %s" % (kstr, sn1[1].key_string()), self.snip_list, "")[1:]


class TestPasswordSnippet(unittest.TestCase):
  def test_letters_symbols(self):
    self.assertEqual(Password("%^*hello(*&1348").key_strings(), "S*3 L*5 S*3 N*4")

  def test_chargers21(self):
    self.assertEqual(Password("chargers21").key_strings(), "L*8 N*2")

  def test_chamillionaire(self):
    self.assertEqual(Password("chamillionaire").key_strings(), "L*14")


if __name__ == '__main__':
  unittest.main()

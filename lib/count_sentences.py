#!/usr/bin/env python3
import re 

class MyString:
  def __init__(self, value=""):
    self._value = value  

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      raise ValueError("The value must be a string.")
    self._value = new_value

  def is_sentence(self):
    if self.value and self.value.endswith('.'):
      return True
    return False

  def is_question(self):
    if self.value and self.value.endswith('?'):
      return True
    return False

  def is_exclamation(self):
    if self.value and self.value.endswith('!'):
      return True
    return False

  def count_sentences(self):
    sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s.strip()]
    return len(sentences)
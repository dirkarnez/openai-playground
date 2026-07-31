# -*- coding: utf-8 -*-
from typing import Any, List
import os
from openai import OpenAI
import numpy as np

def main():
  client = OpenAI(
      # This is the default and can be omitted
      api_key = os.environ.get("OPENAI_API_KEY"),
  )
  
  response = client.responses.create(
      model = "gpt-5.5",
      instructions = "You are a coding assistant that talks like a pirate.",
      input = "How do I check if a Python object is an instance of a class?",
  )
  
  print(response.output_text)

if __name__ == "__main__":
  main()

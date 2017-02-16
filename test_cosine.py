import re, math
from collections import Counter

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     print 'intersection  = ', intersection
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     print 'numerator = ', numerator
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     print 'sum1 = ', sum1
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     print 'sum2 = ', sum2
     denominator = math.sqrt(sum1) * math.sqrt(sum2)
     print 'denominator = ', denominator
     if not denominator:
          return 0.0
     else:
          return float(numerator) / denominator

def main(text1, text2):
     WORD = re.compile(r'\w+')
     print WORD.findall(text1)
     print WORD.findall(text2)
     print '\n'
     word_vector1 = Counter(WORD.findall(text1))
     word_vector2 = Counter(WORD.findall(text2))
     # word_vector1 = Counter(text1.strip())
     # word_vector2 = Counter(text2.strip())     
     print word_vector1
     print word_vector2
     cosine = get_cosine(word_vector1, word_vector2)
     return cosine

"""
Experiment Starts Here.
"""
oporater = dict(_pos = "+",
                             _neg = "-",
                             _eql="=",
                             _grt=">",
                             _lsr="<")
def get_cosine_similarity(std_eqn, stu_eqn):
     """
     Purpose:
         Compare two equations & return float value
     Arrguments:
         std_eqn = standard equation
         stu_eqn = student equation
     Description:
         Convert both to vector structure,
         calculate the no * in word,
         get common word, Apply cosine similarity
         formula, Now add both value to get final result
     Return:
         cosine value(float) in between 0 ~ 1
     """
     word_pattern = re.compile(r'(\w+|\*)')
     _special_symbol = float(std_eqn.count("*"))
     cos_result = 0
     symbol_percentage = 0
     try:
          std_vector = Counter(word_pattern.findall(std_eqn))
          print 'std_vector = ', std_vector
          stu_vector = Counter(word_pattern.findall(stu_eqn))
          print 'stu_vector  = ', stu_vector
          print '\n'
          _words = sum([x for x in std_vector.values()])
          if stu_vector.has_key("*"):
               _special_symbol -= stu_vector["*"]
          print '_special_symbol = ', _special_symbol
          print '_words @ last = ', _words
          try:
               symbol_percentage = _special_symbol / _words
          except ZeroDivisionError:
               symbol_percentage = 0.0
     except Exception as exp:
          print "Exception at converting equation to vector"
          import traceback
          traceback.print_exc()
     else:
          intersection = set(std_vector.keys()) & set(stu_vector.keys())
          numerator = sum([std_vector[x] * stu_vector[x] for x in intersection])
          _sum1 = sum([std_vector[x]**2 for x in std_vector.keys()])
          _sum2 = sum([stu_vector[x]**2 for x in stu_vector.keys()])
          denominator = math.sqrt(_sum1) * math.sqrt(_sum2)
          if not denominator:
              cos_result = 0
          else:
              cos_result = float(numerator) / denominator
     print 'float(symbol_percentage) = ', float(symbol_percentage)
     print 'cos_result = ', cos_result
     final_value = float(symbol_percentage) + cos_result
     print final_value
"""
Experiment Ends Here.
"""



"""
Test only cosine for live implimentation in equationcompare
"""
def get_cosine_from_live(c_std_eqn, c_stu_eqn):
     std_vector = Counter(get_word(c_std_eqn))
     print 'std_vector = ', std_vector
     stu_vector = Counter(get_word(c_stu_eqn))
     print 'stu_vector = ', stu_vector
     _special_symbol = 0
     non_intersection_value = list()
     # Storing number of * & the value contains *
     for _val in std_vector.keys():
          if _val.__contains__("*"):
               _special_symbol += std_vector[_val]
               non_intersection_value.append(_val)
     if stu_vector.has_key("*"):
         _special_symbol -= stu_vector["*"]
     intersection = set(std_vector.keys()) & set(stu_vector.keys())
     print 'intersection = ', intersection
     numerator = sum([std_vector[x] * stu_vector[x]
                      for x in intersection])
     non_intersection_sum = 0
     # storing no of non_matched value
     for _val in stu_vector.keys():
         if _val not in intersection:
             non_intersection_sum += stu_vector[_val]
             non_intersection_value.append(_val)
     # If both non intersect value are not same
     # Empty the list
     if _special_symbol != non_intersection_sum:
         non_intersection_value = list()
     # Cosine similarity formula
     _sum1 = sum([std_vector[x]**2
                  for x in std_vector.keys()
                  if x not in non_intersection_value])
     _sum2 = sum([stu_vector[x]**2
                  for x in stu_vector.keys()
                  if x not in non_intersection_value])
     denominator = math.sqrt(_sum1) * math.sqrt(_sum2)
     print 'numerator = ', numerator
     print 'denominator = ', denominator
     if not denominator:
          return 0
     else:
          return (float(numerator) / denominator) \
                 if (float(numerator) / denominator) <= 1.0 \
                 else 1
def get_word(eqn):
     print eqn
     temp = ""
     # pattern to get word or * in each character
     temp_word_pett = re.compile(r'^(\w+\*+|\*+\w+|\w+|\*+)')
     # pattern for next word or * in string
     next_word_pett = re.compile(r'(\w+|\*+)')
     word_list = list()
     while eqn:
          match = temp_word_pett.search(eqn)
          print match
          if not match:
               if temp:
                    word_list.append(temp)
               print 'temp = ', temp
               temp = ""
               next_match = next_word_pett.search(eqn)
               if not next_match:
                    print 'eqn @ break = ', eqn
                    break
               eqn = eqn[next_match.start():]
               print 'eqn @ new = ', eqn
               continue
          temp += match.group(0)
          eqn = eqn[match.end(0) : ]
          if not eqn and temp:
               word_list.append(temp)
          print 'eqn @ b4 while', eqn
     print 'word_list = ', word_list
     return word_list


if __name__ == "__main__" or __name__=='django.core.management.commands.shell':
     """
     1. Check number of operator("+","-",".", etc) are same or not.
     2. Make a logic for * i.e. where variable can be differ.
     The logic may be like bellow:
     ----------------------------------------------------
         Count the no of * in teacher answer.(3)
         Count the no of words in formula.(10)
         Store the percentage of * in words(33.33333). 
         Check the cosine similarity value. If both are same except * area, the similarity should be 0.666666. Multiply with 100 to get 66.6666
         Now add 66.666666666666+33.3333333333=100 or can be 99 percentage.
         So the equation are same.
     ----------------------------------------------------
     3. The run 'get_cosine' function to get percentage in bet 0 to 1. 1 for all correct.
     
     """
     t1 = 'This is a foo bar sentence .'
     t2 = 'This sentence is similar to a foo bar sentence .'
     # anstext=  "\\frac{1221}{2323}."
     anstext = "(x+y)^2 = x^2 + y^2"
     # stdtext=  "\\frac{1221}{23231}."
     stdtext = "(y+x1)^2=(y)^2+(x)^2"
     
     t3 = "K =\\frac{n(1 \cap 2)}{\sqrt{n(2) \\times n(1)}}"
     t4 = "K =\\frac{n(1 \cap 1)}{\sqrt{n(1) \\times n(2)}}"
     
     t5 = '\sum x+*+\ast'
     t6 = '\sum x+*+\ast'
     t7 = 'x+*+3'
     t8 = 'x+*+2'
     
     t9 = "4ab+(a+b)^2"
     t10 = "(a+b)^2+4ab"

     t11="\[a,b,c,d\]"
     t12="\[b,a,d,c\]"
     
     t13 = "\frac{q}{6}"
     t14 = "\frac{q}{9}"
     
     # cosine = main(t5, t6)
     # print cosine
     # get_cosine_similarity(t7, t8)
     
     wo = get_word(t10)
     result = get_cosine_from_live(t13, t14)
     print result
     
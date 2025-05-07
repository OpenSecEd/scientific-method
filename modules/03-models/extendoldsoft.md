---
title: Exercise: Extending old software
authors:
  - Arve Gengelbach
---
The goal of this exercise is to harden an old network-connected banking 
software that is checked to be working correctly on input that is well-formed, 
however on any other input anything could happen from simple shutdown 
(availability) to leak of confidential data. Programmers that could program in 
the system's programming language are not around anymore.

To increase the assurance level the idea of this exercise is to discussing 
formal-methods based hardening in this particular scenario.

The approach to harden the system is in two steps, first by adding a filtering 
software that drops any malformed network traffic before this traffic could 
even enter the possibly partially broken banking software, and second by 
checking that the filter works correctly. Well-formed input can be specified by 
a regular expression for this program.

Tasks:

1. Formulate a security property that could be verified for each of the two:

  a. the interface between (the output of) the filter and (the input of) the 
  old banking application

  b. the application that does the filtering

2. Discuss how to verify the security property: Which formal method should be 
   used for which scenario? What are the reasons? State any assumptions on 
   input/output.

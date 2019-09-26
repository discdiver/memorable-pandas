---
title: 'Chapter 1: Getting started with Pandas'
description:
  'This chapter will help you get familiar with the course environment. 
  You will import Pandas and make your first DataFrame!'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Introduction" type="slides">

<slides source="chapter1_01_introduction">
</slides>

</exercise>

<exercise id="2" title="Your first quiz">

This is a quiz. 😀
Select your choice and click the *Submit* button. 
When you are ready to move on, click the *Mark as completed button* 
and then click the *Next* button.


What's black and white and red all over? 

<choice>
<opt text="A panda with a sunburn." correct='true'>

This is the right answer, clearly. ☀️🐼 Mark as completed and click *Next*.

</opt>

<opt text="Any other answer.">

Wrong! Clearly a panda with a sunburn! Come on. 😁

</opt>

</choice>

</exercise>

<exercise id="3" title="Import pandas">

We always import the pandas module by its a abbreviation, *pd*. 

Print the version of pandas you're running with `pd.__version__`. 

Note that those are double underscores and there's no space between *pd* and the double underscore.

<codeblock id="01_03">

Have you included a double underscore on either side of *version*?

</codeblock>

</exercise>

<exercise id="4" title="Create a DataFrame">

DataFrames are like super spread sheets. 
There are a several ways to create one. 
The simplest way is to call *pd.DataFrame()* with a dictionary as an argument.
The dictionary keys become the column names and the dictionary values become the DataFrame values. 

<codeblock id="01_04">

Pass in sample_dict.

</codeblock>

</exercise>
import os
from textwrap import dedent
from crewai import Agent
from langchain_groq import ChatGroq


class GameAgents():

	def __init__(self):
		self.llm = ChatGroq(
			api_key=os.getenv('GROQ_API_KEY'),
			model='llama-3.1-70b-versatile',
		)
	def senior_engineer_agent(self):
		print('in senior engineer agent...')
		return Agent(
			role='Senior Software Engineer',
			goal='Create software as needed',
			backstory=dedent("""\
				You are a Senior Software Engineer at a leading tech think tank.
				Your expertise in programming in python. and do your best to
				produce perfect code"""),
			allow_delegation=False,
			llm = self.llm,
			verbose=True
		)

	def qa_engineer_agent(self):
		print('in qa engineer agent')
		return Agent(
			role='Software Quality Control Engineer',
  		goal='create prefect code, by analizing the code that is given for errors',
  		backstory=dedent("""\
				You are a software engineer that specializes in checking code
  			for errors. You have an eye for detail and a knack for finding
				hidden bugs.
  			You check for missing imports, variable declarations, mismatched
				brackets and syntax errors.
  			You also check for security vulnerabilities, and logic errors"""),
			allow_delegation=False,
			llm = self.llm,
			verbose=True
		)

	def chief_qa_engineer_agent(self):
		print('in chief engineer agent')
		return Agent(
			role='Chief Software Quality Control Engineer',
  		goal='Ensure that the code does the job that it is supposed to do',
  		backstory=dedent("""\
				You feel that programmers always do only half the job, so you are
				super dedicate to make high quality code."""),
			allow_delegation=True,
			llm = self.llm,
			verbose=True
		)
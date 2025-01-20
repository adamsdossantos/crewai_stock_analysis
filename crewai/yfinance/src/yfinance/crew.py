from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool
from tools.stock_analysis_tool import YFinanceStockAnalysisTool
import os
import pandas as pd

file_read_tool = FileReadTool(file_path='principles.txt')
file_write_tool = FileWriterTool(function= lambda ticker: f'analysis/{ticker}_stock_analysis.md')
tickers = pd.read_csv('C:\\Users\\adams\\Desktop\\machine_learning\\porfolio_crewai\\ai_stock_analyst\\crewai\\yfinance\\src\\yfinance\\ticker.csv', header=None)


@CrewBase
class Yfinance():
	"""Yfinance crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def stock_research_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['stock_research_manager'],
			tools=[],
			memory = True,
			verbose=True
		)

	@agent
	def senior_stock_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['senior_stock_analyst'],
			tools=[file_read_tool, YFinanceStockAnalysisTool(), FileWriterTool()],
			memory = True,
			verbose=True
		)

	@task
	def get_stock_analysis_ticker_task(self) -> Task:
		return Task(
			config=self.tasks_config['get_stock_analysis_ticker_task'],
			tools=[YFinanceStockAnalysisTool()]
			
		)
	@task
	def analyse_ticker_task(self) -> Task:
		os.makedirs('analysis', exist_ok=True)
		return Task(
			config=self.tasks_config['analyse_ticker_task'],
			tools=[file_read_tool, file_write_tool],
    )

	@crew
	def crew(self) -> Crew:
		"""Creates the Yfinance crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

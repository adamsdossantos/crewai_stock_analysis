# Crewai - Stock Analysis Based on Warren Buffett's Principles  

## Overview  
This project leverages the **CrewAI** framework and the **yfinance** Python module to automate stock analysis based on Warren Buffett's investment principles. It streamlines fetching, evaluating, and reporting stock performance, emphasizing fundamental analysis inspired by Buffett's philosophy.  

## Features  
- **Data Fetching with yfinance**: Automatically retrieves stock data for evaluation.  
- **Buffett-Inspired Analysis**: Applies principles such as earnings growth, economic moats, and intrinsic value.  
- **Agent-Based Workflows**: Organizes tasks through CrewAI's agent and crew structure.  
- **Report Generation**: Produces Markdown reports for individual stock tickers.  

## File Structure  

The project follows the default directory structure created when initializing a CrewAI project:  

```
    ├───analysis
    │       amzn_stock_analysis.md
    │       msft_stock_analysis.md
    │       nflx_stock_analysis.md
    │       tsla_stock_analysis.md
    │
    └───yfinance
        │   .env
        │   .gitignore
        │   pyproject.toml
        │   README.md
        │
        ├───knowledge
        │       user_preference.txt
        │
        ├───src
        │   └───yfinance
        │       │   crew.py
        │       │   main.py
        │       │   principles.txt
        │       │   ticker.csv
        │       │   __init__.py
        │       │
        │       ├───config
        │       │       agents.yaml
        │       │       tasks.yaml
        │       │
        │       ├───tools
        │       │   │   custom_tool.py
        │       │   │   stock_analysis_tool.py
        │       │   │   __init__.py
        │       │   │
        │       │   └───__pycache__
        │       │           stock_analysis_tool.cpython-312.pyc
        │       │           __init__.cpython-312.pyc
        │       │
        │       └───__pycache__
        │               crew.cpython-312.pyc
        │               main.cpython-312.pyc
        │
        └───tests
                teste.ipynb
```

## Installation  

### Prerequisites  
1. **Python 3.10 - 3.12**  
2. Required libraries:  
   - `CrewAI`  
   - `Pandas`  
   - `yfinance`  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/adamsdossantos/crewai_stock_analysis  
   cd yfinance  

2. Install dependencies:
    ```bash
    pip install -r requirements.txt  

3. Verify configuration files:

    Ensure the config/ directory contains the appropriate YAML files for agents, tasks, and the crew.

## Usage

### Input

The project uses a ticker.csv file located in the data/ directory, which contains a list of stock tickers for analysis.

### Running the Project

1. Add stock tickers to data/ticker.csv.

2. Run the project with:
    ```bash
    python src/main.py  

3. Analysis reports will be saved in the data/analysis/ directory.

### Example

For a ticker.csv containing:
```bash
    MSFT  
    AMZN  
    TSLA  
```

The following Markdown reports will be generated:

- analysis/MSFT_stock_analysis.md
- analysis/AMZN_stock_analysis.md
- analysis/TSLA_stock_analysis.md

## Output

Each report includes:

1. Stock data fetched using yfinance.

2. Evaluation based on Warren Buffett's principles:
    - Consistent earnings growth.
    - Economic moats and competitive advantages.
    - Favorable valuation compared to intrinsic value

## Customization

### Adding New Analysis Criteria

1. Update the custom tools in src/tools/.
2. Modify agent or task configurations in config/agents.yaml and config/tasks.yaml.

### Changing Report Formats

By default, reports are generated in Markdown. Update the FileWriterTool settings in src/crew.py to use alternative formats like CSV or JSON.

## Contributing
Contributions are welcome! Fork the repository, report issues, or submit pull requests to enhance the project.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

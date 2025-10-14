# Conversational Data Analysis Agent 🧑‍💻

A modern web application that enables natural language conversations with your CSV datasets using AI-powered data analysis. Upload your data, ask questions in plain English, and get intelligent insights and visualizations.

## 🌟 Features

- **📊 Interactive Data Upload**: Drag and drop CSV files for instant analysis
- **🤖 AI-Powered Conversations**: Ask questions about your data in natural language
- **📈 Automatic Visualizations**: Generate charts and plots based on your queries
- **💬 Conversation History**: Track your analysis journey with persistent chat history
- **🚀 Streamlit Web Interface**: Modern, responsive web UI
- **🐳 Docker Support**: Easy deployment with containerization
- **📓 Jupyter Notebook Examples**: Interactive examples for data exploration

## 🏗️ Architecture

The application consists of several key components:

- **`app.py`**: Main Streamlit web application with file upload and chat interface
- **`main.py`**: Command-line example script for basic data analysis
- **`main.ipynb`**: Jupyter notebook with interactive examples
- **`Dockerfile`**: Container configuration for easy deployment
- **`requirements.txt`**: Python dependencies and package versions

## 🚀 Quick Start

### Method 1: Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/rahul240699/Conversational-Data-Analysis-agent.git
   cd Conversational-Data-Analysis-agent
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

3. **Build and run with Docker**
   ```bash
   docker build -t conversational-data-agent .
   docker run -p 8501:8501 conversational-data-agent
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

### Method 2: Local Development

1. **Clone and setup**
   ```bash
   git clone https://github.com/rahul240699/Conversational-Data-Analysis-agent.git
   cd Conversational-Data-Analysis-agent
   ```

2. **Create virtual environment**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip setuptools wheel
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📋 Prerequisites

- **OpenAI API Key**: Required for AI-powered data analysis
- **Python 3.11**: Recommended for best compatibility
- **Docker** (optional): For containerized deployment

## 📖 Usage Examples

### Web Interface (Streamlit)

1. **Upload your CSV file** using the sidebar file uploader
2. **Preview your data** - see the first few rows automatically displayed
3. **Ask questions** like:
   - "What's the median value of the price column?"
   - "Show me the correlation between age and income"
   - "Create a histogram for the sales data"
   - "What are the top 10 customers by revenue?"

### Command Line Usage

Run the example script with your own data:

```bash
python main.py
```

### Jupyter Notebook

Explore the interactive examples:

```bash
jupyter notebook main.ipynb
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Supported Data Formats

- **CSV files**: Primary supported format
- **Encoding**: UTF-8 recommended
- **Size**: No hard limits, but performance depends on data size

## 📁 Project Structure

```
conversational-analysis-chatbot/
├── app.py                 # Main Streamlit web application
├── main.py               # Command-line example script
├── main.ipynb            # Jupyter notebook examples
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore rules
├── data/               # Sample datasets
│   └── housing.csv     # Example housing dataset
├── cache/              # PandasAI cache files
├── exports/            # Generated charts and visualizations
│   └── charts/
└── README.md           # This file
```

## 🛠️ Technology Stack

- **[Streamlit](https://streamlit.io/)**: Web application framework
- **[PandasAI](https://github.com/gventuri/pandas-ai)**: AI-powered data analysis
- **[OpenAI](https://openai.com/)**: Large language model for natural language processing
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **[LangChain](https://langchain.com/)**: LLM application framework (prepared for RAG)
- **[Docker](https://docker.com/)**: Containerization platform

## 🎯 Example Queries

Try these natural language queries with your data:

### Statistical Analysis
- "What's the mean, median, and mode of the salary column?"
- "Calculate the standard deviation of prices"
- "Show me the correlation matrix"

### Data Exploration
- "How many rows and columns are in this dataset?"
- "What are the unique values in the category column?"
- "Are there any missing values?"

### Visualizations
- "Create a scatter plot of age vs income"
- "Plot a histogram of the price distribution"
- "Show me a bar chart of sales by region"
- "Generate a heatmap of correlations"

### Business Intelligence
- "Which product category has the highest sales?"
- "What's the trend of revenue over time?"
- "Identify outliers in the dataset"

## 🔮 Future Enhancements

- **📚 Vector Store Integration**: RAG (Retrieval Augmented Generation) for enhanced context
- **🔌 Multiple Data Sources**: Support for Excel, JSON, and database connections
- **📊 Advanced Visualizations**: Interactive plotly charts and dashboards
- **👥 Multi-user Support**: User sessions and data persistence
- **🔒 Authentication**: User login and data security features
- **📱 Mobile Optimization**: Responsive design for mobile devices

## 🐛 Troubleshooting

### Common Issues

1. **Import Error: "No module named 'pandasai'"**
   ```bash
   pip install --force-reinstall pandasai
   ```

2. **OpenAI API Error**
   - Verify your API key in the `.env` file
   - Check your OpenAI account has sufficient credits

3. **Docker Build Fails**
   ```bash
   docker system prune -f
   docker build --no-cache -t conversational-data-agent .
   ```

4. **Streamlit Port Already in Use**
   ```bash
   streamlit run app.py --server.port 8502
   ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Rahul Sohandani** - [rahul240699](https://github.com/rahul240699)

## 🙏 Acknowledgments

- [PandasAI](https://github.com/gventuri/pandas-ai) for the amazing conversational data analysis capabilities
- [Streamlit](https://streamlit.io/) for the fantastic web framework
- [OpenAI](https://openai.com/) for providing the powerful language models

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/rahul240699/Conversational-Data-Analysis-agent/issues) page
2. Create a new issue with detailed description
3. Join our community discussions

---

**⭐ Star this repository if you found it helpful!**
FROM python:3.10-slim
WORKDIR /app
RUN pip install streamlit requests pandas
COPY . .
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
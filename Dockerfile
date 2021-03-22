FROM python:3
WORKDIR .
COPY . .

# Install python dependencies
RUN pip install -r requirements.txt

# Run the app
CMD ["python", "app.py"]
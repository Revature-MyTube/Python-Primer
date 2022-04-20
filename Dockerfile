FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

RUN date > /code/start.txt

RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

# CMD ["gunicorn", "core/core.wsgi:application", "-w", "4", "-b", "0.0.0.0:8000"]
CMD ["python", "core/manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.9 
# Or any preferred Python version.
ADD . .
RUN apt install pipenv

CMD [“/bin/bash”] 
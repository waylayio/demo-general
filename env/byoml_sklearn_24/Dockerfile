FROM python:3.7

RUN pip install waylay-beta[byoml-sklearn-0.24]
RUN pip install jupyter
RUN pip install matplotlib

EXPOSE 8888

CMD jupyter notebook --ip 0.0.0.0 --no-browser --allow-root /home

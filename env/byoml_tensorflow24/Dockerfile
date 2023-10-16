FROM python:3.8

RUN pip install 'waylay-beta>=0.7.0'
RUN pip install 'waylay-beta[byoml-tensorflow-2.4]'

RUN pip install jupyter
RUN pip install seaborn
RUN pip install matplotlib

EXPOSE 8888

CMD jupyter notebook --ip 0.0.0.0 --no-browser --allow-root /home

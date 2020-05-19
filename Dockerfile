FROM python
COPY . /MLOps
WORKDIR /MLOps
RUN pip install --upgrade pip
RUN pip3 install keras 
RUN pip3 install tensorflow 
CMD [ "python", "./MNIST_CNN.py" ]

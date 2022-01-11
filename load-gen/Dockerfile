FROM python:3

WORKDIR /usr/src/load-gen

COPY load-script.py /usr/src/load-gen/
RUN pip3 install --upgrade requests
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "load-script.py" ]
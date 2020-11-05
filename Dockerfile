FROM continuumio/miniconda3
RUN pip install pandas
RUN pip install -i https://test.pypi.org/simple/ lambdata-urena1


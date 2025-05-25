FROM public.ecr.aws/lambda/python:3.10


RUN python3 -m venv myenv
RUN source myenv/bin/activate

COPY requirements.txt .
COPY main.py .
COPY smartScan.py .

RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
RUN pip install spacy
RUN python -m spacy download en_core_web_sm


CMD ["main.handler"]
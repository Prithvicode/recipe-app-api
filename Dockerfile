# specific versino of python(dockerimage) 3.9 is
# tag name and alpine is linux versionS lightweight image


# whoever is maintaining the file

#recommended when running python
# tell not buffer output. will direclty to console


# copies requirments local to 

#copy app, our django app

# working directory, default, when running cmds in docker

# Expose 8000 to machine to connect dj server


# create new layer for every run,so we use in one to make 
# one layer keepig it light
# 1. virtual env
# 2. upgrate pip for virtual env
# 3. install all requirements
# 4. Remove tmp directory, to rid of extra dependency for lightweight
# Keep it lightweight
# 5. Add user and not user root user to run apps, as root has 
# all the access so, it save from attacker as no full access.
# 6. No password, so disable
# 7. No home directory, lightweight
# 8, Specify name of the user



 # update env path variable, dont have specify path when we run app       


# all above is run as Root. But now we switch as the django-user
FROM python:3.9-alpine3.13
LABEL maintainer="prithviCode"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements/dev/txt

COPY ./app /app
WORKDIR /app
EXPOSE 8000


# defaul we dont run dev. but when called through 
# docker compose it will override them
ARG DEV =false 
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    # shell cmd scripting
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user




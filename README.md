# RestApi-credit-risk-db

## Running

### Run in virtual environment (recommended):

**Conda** is a packaging tool and installer that aims to do more than what pip does; handle library dependencies outside of the Python packages as well as the Python packages themselves. Conda also creates a virtual environment, like virtualenv does.

Check conda is installed and in your path:
```
$ conda -V
conda 3.7.0
```

Make sure conda is up to date:
```
$ conda update conda
```

Create your virtual environment:
```
$ conda create -n yourenvname python=x.x
```

Activate your virtual environment:
```
$ source activate yourenvname
```


*Additional commands:*

See a list of your virtual envoronments made with conda:
```
$ conda info -e
```

To leave virtual environment:
```
$ source deactivate
```

To delete virtual environment:
```
$ conda remove -n yourenvname -all
```


### Install dependencies

While in your virtual environment:

```
$ pip install -r /path/to/requirements.txt
```

### Create environment variables

Mac OS:

Display your environment variables
```
env
```

Create environment variables `DATABASE_URL` (format: `mysql+mysqlconnector://username:password@host:port/database`) and `AI_CHAT_SECRET_KEY` (format: `supersecretkey`)
using:

```
export variable=value
```

### Run api:

```
$ python app.py
```

## Testing

test using postman


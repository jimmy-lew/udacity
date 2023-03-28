# Running Instructions 

## CLI

```bash
  
  cd cli
  pip3 install -r requirements_pip.txt
  python3 main.py
  
 ```



## API [Deprecated]

API for data parsing and analysis


```bash
  
  cd api
  pip3 install -r requirements_pip.txt
  python3 main.py

```

## Web [Deprecated]

Web interface for filter selection and data display

Using npm

```bash

  cd web
  npm i 
  npm run dev

```

Using pnpm (preferred)

```bash

  cd web
  pnpm i
  pnpm dev

```

Alternatively you can use the deployed version [here](https://udacity-one.vercel.app)

# App Flow [Deprecated]

Start off by running the api, the instructions for doing so are as follows [above](#api).

If you are successful in doing so, you will see something like 

``` bash
INFO:     Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [45955] using WatchFiles
INFO:     Started server process [45958]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Leave the program running

Next open up the web interface either by running it [locally](#web) or accessing the deployed version from the provided [link](https://udacity-one.vercel.app) 

If you notice a flashing network icon at the top of the prompts, it means that the API is not running.  

If so, check that you have completed the first few steps listed above

From the web interface, you will be prompted to answer a few questions about which parts of the data you wish to view, answer them.  

The data will take a few seconds to load and then you will be redirected to a page containing all the results of the data analysis

# Tech Stack

# Web Interface [Deprecated]
- Nuxt3: Vue Web Framework
  - Nuxt Content: Store prompts in yaml file
  - TailwindCSS: Styling
  - NuxtIcon: Access Iconify Library
  - EsLint (Antfu): Linting
- Vercel: Deployment
  
# API [Deprecated]
- FastAPI: Python API library
  - Pydantic: Model Validation
  - Uvicorn: ASGI Server
- Pandas: Data Analysis

# CLI
- Numpy & Pandas: Data Analysis
- Pydantic: Model Validation
- difflib: text matching
# CLI
- Numpy & Pandas: Data Analysis
- difflib: text matching
- Pydantic: model validation

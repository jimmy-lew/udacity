# Running Instructions 


## API 

API for data parsing and analysis


```bash
  
  cd api
  pip3 install -r requirements_pip.txt
  python3 main.py


```

## Web

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

# Tech Stack

# Web Interface
- Nuxt3: Vue Web Framework
  - Nuxt Content: Store prompts in yaml file
  - TailwindCSS: Styling
  - NuxtIcon: Access Iconify Library
  - EsLint (Antfu): Linting
- Vercel: Deployment
  
# API
- FastAPI: Python API library
  - Pydantic: Model Validation
  - Uvicorn: ASGI Server
- Pandas: Data Analysis

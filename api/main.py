from fastapi import FastAPI
from bikeshare_2 import QueryBody, CalculationActor

app = FastAPI()


@app.get('/ok')
def check_ok():
    return {
        'code': 200,
        'status': 'OK'
    }


@app.post('/calculate')
def calculate_stats(query: QueryBody):
    calculation_actor = CalculationActor(query)
    result = calculation_actor.calculate()

    return result


if __name__ == '__main__':
    pass

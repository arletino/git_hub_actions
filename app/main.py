from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def root():
    return {'message': "hello World"}

if __name__ == '__main__':
    
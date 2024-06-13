from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/fruits')
def get_fruits():
    # returns a dictionary with fruits
    return {
        'fruits': ['Mango',
                    'Pomegranate',
                    'Orange',
                    'Litchi']
    }


# if this file is being executed then run the service
if __name__ == '__main__':
    # run the service uvicorn.run("filename:app")
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=False)
    # http://localhost:8081/docs
    # uvicorn app:app --host 127.0.0.1 --port 8000 --reload
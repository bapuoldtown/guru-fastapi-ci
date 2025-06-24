from fastapi import FastAPI

app = FastAPI()

@app.get("/Srikhestra-Dham")
def hello():
    return {"msg": "Jai Jagannath 🚩"}

@app.get("/Ekamrakshetra-Dham")
def hi():
    return {"msg": "Jai Shri Lingaraj 🚩"}

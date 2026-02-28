from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Saudi ID Validator")

# Enable CORS for local testing from Svelte frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def validate_saudi_id(id_number: str) -> bool:
    id_str = str(id_number)
    
    # التأكد من الطول والبداية
    if len(id_str) != 10 or id_str[0] not in ['1', '2']:
        return False

    sum_val = 0
    for i in range(10):
        digit = int(id_str[i])
        if i % 2 == 0:  # الخانات الفردية (0, 2, 4...)
            # نضاعف الرقم، وإذا كان الناتج خانتين نجمعهما
            doubled = str(digit * 2)
            if len(doubled) > 1:
                sum_val += int(doubled[0]) + int(doubled[1])
            else:
                sum_val += int(doubled)
        else:  # الخانات الزوجية
            sum_val += digit

    # يجب أن يكون المجموع الكلي قابلاً القسمة على 10
    return sum_val % 10 == 0

class IDResponse(BaseModel):
    id_number: str
    isValid: bool

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Saudi ID Validator API",
        "docs": "Visit /docs for the interactive API documentation",
        "usage": "Send a GET request to /validate/{id_number}"
    }

@app.get("/validate/{id_number}", response_model=IDResponse)
def check_id(id_number: str):
    is_valid = validate_saudi_id(id_number)
    return IDResponse(id_number=id_number, isValid=is_valid)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

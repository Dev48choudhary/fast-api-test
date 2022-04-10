from fastapi import FastAPI

app = FastAPI()
from pydantic import BaseModel


class Item(BaseModel):
    name: str


@app.post('/get_recommendations')
def show_blog(keyword: Item):
    final_keyword = keyword.name.lower()
    if final_keyword in ['machine learning', 'supervisd learing', 'deep learning']:
        response_str = 'https://www.youtube.com/watch?v=ukzFI9rgwfU&t=213s'
    else:
        response_str = 'Not Found'
    return {response_str} 




# We can create an http endpoint that takes query parameters

 

















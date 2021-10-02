# Text-classification

## Training Script
    The traning file is inside **Train** Folder. 

## Running Inference
- Upgrade pip before installing requirments
- Install all the required Python dependencies:
```
pip install -r requirements.txt
```
- To run inference on fast api run the follwing command:
```
uvicorn main:app
```
- The program will run in localhost. Open the browser and enter follwing address:
```
http://127.0.0.1:8000/docs
```
- Swagger will open up . We can enter text and try it out.


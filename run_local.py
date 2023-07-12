# This file is the entry point for the location API, when
# testing locally, on your localhost.


import uvicorn


if __name__ == "__main__":
  
  uvicorn.run("api.api:app", host="0.0.0.0", port=8000, reload=True)

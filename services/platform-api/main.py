from fastapi import FastAPI, HTTPException
import logging
import time
import random
import os

app = FastAPI(title="Platform Reliability API")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

@app.get("/health")
def health():
    logging.info("Health check requested")
    return {"status": "UP"}

@app.get("/readiness")
def readiness():
    logging.info("Readiness check requested")
    return {"status": "READY"}

@app.get("/process")
def process():
    start = time.time()
    delay = random.uniform(0.3, 2.0)
    time.sleep(delay)

    if random.random() < 0.2:
        logging.error("Simulated processing failure")
        raise HTTPException(status_code=500, detail="Processing error")

    duration = round(time.time() - start, 2)
    logging.info(f"Processed request in {duration}s")

    return {"result": "success", "time": duration}

@app.get("/crash")
def crash():
    logging.critical("Intentional crash triggered")
    os._exit(1)

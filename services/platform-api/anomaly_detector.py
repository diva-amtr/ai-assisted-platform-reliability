# anomaly_detector.py
import time
from statistics import mean

LATENCY_THRESHOLD_MS = 800
ERROR_RATE_THRESHOLD = 0.2

def detect_latency_anomaly(latencies):
    avg_latency = mean(latencies)
    return avg_latency > LATENCY_THRESHOLD_MS

def detect_error_anomaly(errors, total_requests):
    if total_requests == 0:
        return False
    error_rate = errors / total_requests
    return error_rate > ERROR_RATE_THRESHOLD

def detect_anomalies(metrics):
    anomalies = []

    if detect_latency_anomaly(metrics["latencies"]):
        anomalies.append("High latency detected")

    if detect_error_anomaly(metrics["errors"], metrics["requests"]):
        anomalies.append("High error rate detected")

    return anomalies

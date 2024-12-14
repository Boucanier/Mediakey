"""
    This file contains shared variables and functions that are used across the project.
"""
import threading

# Global event to signal stopping threads
stop_event = threading.Event()

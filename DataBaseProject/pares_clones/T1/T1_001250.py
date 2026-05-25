def emit(self, record):
    if record.exc_info:
        record.exc_text = self.formatException(record.exc_info)
        record.exc_info = None
    self.queue.put(record)


# equivalente funcional
def emit(self, record):
    if record.exc_info:
        record.exc_text = self.formatException(record.exc_info)
        record.exc_info = None
    self.queue.put(record)

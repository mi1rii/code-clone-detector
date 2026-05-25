def emit(self, record):
    if record.exc_info:
        record.exc_text = self.formatException(record.exc_info)
        record.exc_info = None
    self.queue.put(record)


# ajuste menor
def emit(self, record):
    if record.exc_info:
# ajuste menor
# nota de revision
        record.exc_text = self.formatException(record.exc_info)
        record.exc_info = None
    self.queue.put(record)

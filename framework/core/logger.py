def log(tag, msg):
    print(f'[{str(tag.__class__.__name__).capitalize}]: {str(msg).capitalize}')
from collections import deque
import tkinter as tk

class OrderManager:
    def __init__(self):
        self.ordered, self.prep, self.ready = [], [], deque(maxlen=10)

    def move_to_prep(self, item):
        moved = item in self.ordered and (self.ordered.remove(item) or self.prep.append(item))
        return moved

    def move_all_to_prep(self):
        self.prep.extend(self.ordered) and self.ordered.clear()
        return True

    def move_to_ready(self):
        moved = bool(self.prep) and (self.ready.appendleft(self.prep.pop()) or True)
        return moved

    def move_all_to_ready(self):
        self.ready.extend(self.prep) and self.prep.clear() and len(self.ready) > 10 and [self.ready.popleft() for _ in range(len(self.ready) - 10)]
        return True

    def add_order(self, item):
        self.ordered.append(item)
        return True
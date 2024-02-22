from collections import deque
import tkinter as tk

class OrderManager:
    def __init__(self):
        self.ordered = []
        self.prep = []
        self.ready = deque(maxlen=10)  # Only keep the last 10 items
    
    def move_to_prep(self, item):
        if item in self.ordered:
            self.ordered.remove(item)
            self.prep.append(item)

    def move_all_to_prep(self):
        self.prep.extend(self.ordered)
        self.ordered.clear()

    def move_to_ready(self, item):
        if item in self.prep:
            self.prep.remove(item)
            self.ready.append(item)

    
    def move_all_to_ready(self):
        self.ready.extend(self.prep)
        self.prep.clear()
        
        # Remove items from the left of the deque if it's longer than 10/oldest order
        if len(self.ready) > 10:
            removed_items = [self.ready.popleft() for _ in range(len(self.ready) - 10)]
    
    def add_order(self, item):
        self.ordered.append(item)
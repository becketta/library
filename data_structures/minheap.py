# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:59:08 2016

@author: Aaron Beckett
"""
import math

class MinHeap(object):

	def __init__(self, array = []):
		self.heap = array
		self.__heapify()

	def __bool__(self):
		return bool(self.heap)

	def add(self, val):
		self.heap.append(val)
		self.__sift_up(len(self.heap) - 1)

	def extract_min(self):
		minimum = self.heap.pop(0) if self.heap else None
		if self.heap:
			self.heap.insert(0, self.heap.pop())
			self.__sift_down(0)
		return minimum

	def __heapify(self):
		start = self.__parent(len(self.heap) - 1)
		for i in range(start, 0, -1):
			self.__sift_down(i)

	def __sift_down(self, root):
		left = self.__left_child(root)
		right = self.__right_child(root)

		proposed = left if left and self.heap[root] > self.heap[left] else root
		proposed = right if right and self.heap[proposed] > self.heap[right] else proposed

		if proposed != root:
			self.__swap(proposed, root)
			self.__sift_down(proposed)

	def __sift_up(self, child):
		parent = self.__parent(child)

		if parent >= 0 and self.heap[child] < self.heap[parent]:
			self.__swap(child, parent)
			self.__sift_up(parent)

	def __swap(self, i, j):
		temp = self.heap[i]
		self.heap[i] = self.heap[j]
		self.heap[j] = temp

	def __left_child(self, parent_idx):
		left = parent_idx * 2 + 1
		return left if left < len(self.heap) else None

	def __right_child(self, parent_idx):
		right = parent_idx * 2 + 2
		return right if right < len(self.heap) else None

	def __parent(self, child_idx):
		return math.ceil(child_idx / 2) - 1

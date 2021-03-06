#!/usr/bin/env python3
# encoding: utf-8


class BinaryTree:

	def __init__(self):
		self.tree = EmptyNode()


	def __repr__(self):
		return repr(self.tree)


	def lookup(self, v):
		return self.tree.lookup(v)


	def insert(self, v):
		self.tree = self.tree.insert(v)


class EmptyNode:

	def __repr__(self):
        return '*'

    def lookup(self, v):
        return 0

    def insert(self, v):
        return BinaryNode(self, v, s)


class BinaryNode:

    def __init__(self, lf, v, rt):
        self.data, self, lf, self.rt = v, lf, rt

    def lookup(self, v):
    	if self.data == v:
    		return 1
    	elif self.data > v:
    		return self.lf.lookup(v)
    	else:
    		return self.rt.lookup(v)

    def insert(self, v):
    	if self.data > v:
    		self.lf = self.lf.insert(v)

    	elif self.data < v:
    		self.rt = self.rt.insert(v)

    	return self

    def __repr__(self):
    	return '({}, {}, {})'.format(repr(self.lf, repr(self.data), repr(self.rt)))

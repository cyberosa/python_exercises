# Collected from https://dataaspirant.com/five-most-popular-similarity-measures-implementation-in-python/
from math import *
from decimal import Decimal

def euclidean_distance(x, y):
	""" Function to compute the euclidean distance of two vectors
	 :param x: vector as list
	 :param y: vector as list
	 :return euclidean distance"""
	return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


def manhattan_distance(x, y):
	""" Function to compute the manhattan distance of two vectors
	 :param x: vector as list
	 :param y: vector as list
	 :return manhattan distance"""
	return sum(abs(a - b) for a, b in zip(x, y))


def nth_root(value, n_root):
	root_value = 1 / float(n_root)
	return round(Decimal(value) ** Decimal(root_value), 3)


def minkowski_distance(x, y, p_value):
	""" Function to compute the minkowski distance of two vectors
	 :param x: vector as list
	 :param y: vector as list
	 :return minkowski distance"""
	return nth_root(sum(pow(abs(a - b), p_value) for a, b in zip(x, y)), p_value)


def square_rooted(x):
	return round(sqrt(sum([a * a for a in x])), 3)


def cosine_similarity(x, y):
	""" Function to compute the cosine similarity of two vectors
	:param x: vector as list
	:param y: vector as list
	:return cosine similarity value"""
	numerator = sum(a * b for a, b in zip(x, y))
	denominator = square_rooted(x) * square_rooted(y)
	return round(numerator / float(denominator), 3)


def jaccard_similarity(x, y):
	""" Function to compute the jaccard similarity of two vectors
	 :param x: vector as list
	 :param y: vector as list
	 :return jaccard similarity value"""
	intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
	union_cardinality = len(set.union(*[set(x), set(y)]))
	return intersection_cardinality / float(union_cardinality)
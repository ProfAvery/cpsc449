#!/bin/sh

http --verbose POST localhost:5000/books/ @"$1"

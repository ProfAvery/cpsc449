#!/bin/sh

http --verbose POST localhost:8000/books/ @"$1"

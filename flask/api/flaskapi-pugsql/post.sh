#!/bin/sh

http --verbose POST http://localhost:5000/api/v1/resources/books @"$1"

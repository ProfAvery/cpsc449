#!/bin/sh

http --verbose POST http://localhost:5000/api/v1/resources/books <<EOF
{
    "published": 2017,
    "author": "John Scalzi",
    "title": "The Collapsing Empire",
    "first_sentence": "The mutineers would have gotten away with it, too, if it weren’t for the collapse of the Flow."
}
EOF

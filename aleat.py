#!/usr/bin/python

import webapp
import random


class aleat(webapp.webApp):

    def process(self, parsedRequest):
        url = str(random.randrange(161612316))
        return("200 OK",
               "<html><body><h1>Hello World!</h1>" +
               "<a href='" + url + "'>dame otra</a>" +
               "</body></html>")

if __name__ == "__main__":
    testAleat = aleat("localhost", 1234)

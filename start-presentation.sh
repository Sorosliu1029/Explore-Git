#!/bin/env bash

jupyter nbconvert --to=slides --post serve --ServePostProcessor.ip='0.0.0.0' mock.ipynb

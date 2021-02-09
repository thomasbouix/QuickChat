#!/bin/bash

# Scipt pour deployer un hook sur le repertoire git.
# Ce hook permet de verifier la validite du format de vos commits.

cd .git/hooks/
ln -s ../../commit-msg.py ./commit-msg
cd ../..
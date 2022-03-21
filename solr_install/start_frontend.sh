#!/bin/bash
cd ~/offline-search/frontend
rm -f package-lock.json
npm cache clean --force
npm install
npm remove react-spring
npm install react-spring@9.1.2
echo "Please access http://127.0.0.1:3000 to access the UI"
npm start